#!/usr/bin/python

#
# written by @eric_capuano
# https://github.com/ecapuano/web-traffic-generator
#
# published under MIT license :) do what you want.
#

# 20170714 shyft ADDED python 2.7 and 3.x compatibility and generic config
# 20200225 rarawls ADDED recursive, depth-first browsing, color stdout
from __future__ import print_function
from bs4 import BeautifulSoup

import asyncio
import aiohttp

import random
import requests
import re
import time

import sys
import os
import importlib.util

try:
    # import config

    # new implementation expects a file to be passed via command-line argument
    # tool then loads that file as the config and is passed along to the rest of the code

    # get file name from command line argument
    file_path = sys.argv[1]
    module_name = os.path.splitext(os.path.basename(file_path))[0]

    # load file and import it as config
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    config = importlib.util.module_from_spec(spec)

    # makes config module available to the rest of the tool
    spec.loader.exec_module(config)

except ImportError:

    class ConfigClass:  # minimal config incase you don't have the config.py
        MAX_DEPTH = 10  # dive no deeper than this for each root URL
        MIN_DEPTH = 3   # dive at least this deep into each root URL
        MAX_WAIT = 10   # maximum amount of time to wait between HTTP requests
        MIN_WAIT = 5    # minimum amount of time allowed between HTTP requests
        DEBUG = False    # set to True to enable useful console output

        # use this single item list to test how a site responds to this crawler
        # be sure to comment out the list below it.
        #ROOT_URLS = ["https://digg.com/"]
        ROOT_URLS = [
            "https://www.reddit.com"
        ]

        # items can be a URL "https://t.co" or simple string to check for "amazon"
        blacklist = [
            'facebook.com',
            'pinterest.com'
        ]

        # must use a valid user agent or sites will hate you
        USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    config = ConfigClass
except Exception as err:
    print(err)
    exit()


class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    PURPLE = '\033[95m'
    NONE = '\033[0m'


def debug_print(message, color=Colors.NONE):
    """ A method which prints if DEBUG is set """
    if config.DEBUG:
        print(color + message + Colors.NONE)


def hr_bytes(bytes_, suffix='B', si=False):
    """ A method providing a more legible byte format """

    bits = 1024.0 if si else 1000.0

    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(bytes_) < bits:
            return "{:.1f}{}{}".format(bytes_, unit, suffix)
        bytes_ /= bits
    return "{:.1f}{}{}".format(bytes_, 'Y', suffix)

async def download_resource(session, resource_url):
    """
    downloads files asyncronously
    """
    try:
        async with session.get(resource_url) as response:
            if response.status == 200:
                # Discard content after fetching
                _ = await response.read()
                # print(f'Successfully downloaded: {resource_url}')
    except Exception as err:
        pass
        # print(f'error downloading {resource_url}: {err}')

async def download_resources_async(resource_urls):
    """
    asyncio entry point to create task(s) and schedule downloads
    """
    # Asynchronously download all resources
    async with aiohttp.ClientSession() as session:
        tasks = [download_resource(session, resource_url) for resource_url in resource_urls]
        await asyncio.gather(*tasks)


def do_request(url, user_agent = config.USER_AGENT):
    """ A method which loads a page """

    global data_meter
    global good_requests
    global bad_requests

    debug_print("  Requesting page...".format(url))

    headers = {'user-agent': user_agent}

    try:
        r = requests.get(url, headers=headers, timeout=5)
    except:
        # Prevent 100% CPU loop in a net down situation
        time.sleep(30)
        return False

    page_size = len(r.content)
    data_meter += page_size

    status = r.status_code

    if (status != 200):
        bad_requests += 1
        debug_print("  Response status: {}".format(r.status_code), Colors.RED)
        if (status == 429):
            debug_print(
                "  We're making requests too frequently... sleeping longer...")
            config.MIN_WAIT += 10
            config.MAX_WAIT += 10
    else:
        good_requests += 1

    debug_print("  Good requests: {}".format(good_requests))
    debug_print("  Bad reqeusts: {}".format(bad_requests))

    # once it's determined request was good, proceed with downloading all the content
    parsed_page = BeautifulSoup(r.content, 'html.parser')

    # tags we give a shit about
    tags = [
        'img',
        # 'script',
        # 'style',
    ]

    # find all the tags we care about in the page
    page_tags = parsed_page.find_all([tags])

    # we'll hold the urls in this array
    resource_urls = []

    for tag in page_tags:
        resource_url = tag.get('src')

        # normalize formatting since html allows relative links
        if resource_url:
            if(resource_url.startswith('//')):
                resource_url = 'https:' + resource_url
            elif(resource_url.startswith('/')):
                resource_url = url + resource_url
            elif(not resource_url.startswith('http')):
                resource_url = f'{url}/{resource_url}'

            # once normalized, append to resource list
            resource_urls.append(resource_url)

    debug_print("  Found elements: {}".format(len(resource_urls)))

    # too slow, swapped out with asyncio implementation
    '''
    for resource_url in resource_urls:
        try:
            response = requests.get(resource_url, headers = headers, timeout = 5, stream = True)
            data_meter += len(response.content)
            debug_print("  DOWNLOADING: {}".format(resource_url))

        except Exception as error:
            debug_print("  ERROR: {}".format(error))
    '''

    # one issue with asyncio implementation is that i cant get it to reliably grab filesizes of what it retrieves...
    # oh well,
    asyncio.run(download_resources_async(resource_urls))

    debug_print("  Page size: {}".format(hr_bytes(page_size)))
    debug_print("  Data meter: {}".format(hr_bytes(data_meter)))

    return r


def get_links(page):
    """ A method which returns all links from page, less blacklisted links """

    pattern = r"(?:href\=\")(https?:\/\/[^\"]+)(?:\")"
    links = re.findall(pattern, str(page.content))
    valid_links = [link for link in links if not any(
        b in link for b in config.blacklist)]
    return valid_links


def recursive_browse(url, depth):
    """ A method which recursively browses URLs, using given depth """
    # Base: load current page and return
    # Recursively: load page, pick random link and browse with decremented depth

    debug_print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    debug_print(
        "Recursively browsing [{}] ~~~ [depth = {}]".format(url, depth))

    # if the USER_AGENT variable is a list, pick a random one
    if isinstance(config.USER_AGENT, list):
        session_user_agent = random.choice(config.USER_AGENT)
    # otherwise pass along the variable normally (legacy behavior)
    else:
        session_user_agent = config.USER_AGENT

    debug_print("  Session User Agent: {}".format(session_user_agent))

    if not depth:  # base case: depth of zero, load page

        do_request(url, session_user_agent)
        return

    else:  # recursive case: load page, browse random link, decrement depth

        page = do_request(url, session_user_agent)  # load current page

        # give up if error loading page
        if not page:
            debug_print(
                "  Stopping and blacklisting: page error".format(url), Colors.YELLOW)
            config.blacklist.append(url)
            return

        # scrape page for links not in blacklist
        debug_print("  Scraping page for links".format(url))
        valid_links = get_links(page)
        debug_print("  Found {} valid links".format(len(valid_links)))

        # give up if no links to browse
        if not valid_links:
            debug_print("  Stopping and blacklisting: no links".format(
                url), Colors.YELLOW)
            config.blacklist.append(url)
            return

        # sleep and then recursively browse
        sleep_time = random.randrange(config.MIN_WAIT, config.MAX_WAIT)
        debug_print("  Pausing for {} seconds...".format(sleep_time))
        time.sleep(sleep_time)

        recursive_browse(random.choice(valid_links), depth - 1)


if __name__ == "__main__":

    # Initialize global variables
    data_meter = 0
    good_requests = 0
    bad_requests = 0

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Traffic generator started")
    print("https://github.com/ecapuano/web-traffic-generator")
    print("Diving between 3 and {} links deep into {} root URLs,".format(
        config.MAX_DEPTH, len(config.ROOT_URLS)))
    print("Waiting between {} and {} seconds between requests. ".format(
        config.MIN_WAIT, config.MAX_WAIT))
    print("This script will run indefinitely. Ctrl+C to stop.")

    while True:

        debug_print("Randomly selecting one of {} Root URLs".format(
            len(config.ROOT_URLS)), Colors.PURPLE)

        random_url = random.choice(config.ROOT_URLS)
        depth = random.choice(range(config.MIN_DEPTH, config.MAX_DEPTH))

        recursive_browse(random_url, depth)

