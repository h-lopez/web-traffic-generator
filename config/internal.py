MAX_DEPTH = 2   # maximum click depth
MIN_DEPTH = 1   # minimum click depth
MAX_WAIT = 30   # maximum amount of time to wait between HTTP requests
MIN_WAIT = 10   # minimum amount of time allowed between HTTP requests
DEBUG = True    # set to True to enable useful console output

# use this single item list to test how a site responds to this crawler
# be sure to comment out the list below it.
#ROOT_URLS = ['https:///digg.com/']

ROOT_URLS = [
    'http://fs.acme.corp',
    # fs.acme.corp hosts sftpgo on port 8080 in addition to nginx port 80
    'http://fs.acme.corp:8080',
    'http://nms.acme.corp',
    'http://speed.acme.corp',
	]


# items can be a URL 'https://t.co' or simple string to check for 'amazon'
blacklist = [
	'https://t.co',
	't.umblr.com',
	'messenger.com',
	'itunes.apple.com',
	'l.facebook.com',
	'bit.ly',
	'mediawiki',
	'.css',
	'.ico',
	'.xml',
	'intent/tweet',
	'twitter.com/share',
	'signup',
	'login',
	'dialog/feed?',
	'.png',
	'.jpg',
	'.json',
	'.svg',
	'.gif',
	'zendesk',
	'clickserve'
	]

# must use a valid user agent or sites will hate you
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Safari/537.36'

# allow multiple user agents
USER_AGENT = [
    # firefox on windows
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0',
    # firefox on linux
    'Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0',
    # safari on macOS
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15',
    # IE11 on windows
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    # edge on windows
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.2651.74',
    # chrome on windows
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Safari/537.36',
]