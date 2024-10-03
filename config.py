MAX_DEPTH = 5   # maximum click depth
MIN_DEPTH = 2   # minimum click depth
MAX_WAIT = 60   # maximum amount of time to wait between HTTP requests
MIN_WAIT = 15   # minimum amount of time allowed between HTTP requests
DEBUG = True    # set to True to enable useful console output

# use this single item list to test how a site responds to this crawler
# be sure to comment out the list below it.
#ROOT_URLS = ['https:///digg.com/']

ROOT_URLS = [
    'https://google.com',
    'https://youtube.com',
    'https://facebook.com',
    'https://yahoo.com',
    'https://wikipedia.org',
    'https://amazon.com',
    'https://twitter.com',
    'https://taobao.com',
    'https://bing.com',
    'https://msn.com',
    'https://weibo.com',
    'https://vk.com',
    'https://instagram.com',
    'https://yandex.ru',
    'https://ebay.com',
    'https://T.co',
    'https://mail.ru',
    'https://pinterest.com',
    'https://tmall.com',
    'https://netflix.com',
    'https://360.cn',
    'https://microsoft.com',
    'https://onclickads.net',
    'https://wordpress.com',
    'https://blogspot.com',
    'https://tumblr.com',
    'https://imgur.com',
    'https://sohu.com',
    'https://paypal.com',
    'https://stackoverflow.com',
    'https://aliexpress.com',
    'https://apple.com',
    'https://diply.com',
    'https://hpcc-page.cnc.ccgslb.com.cn',
    'https://github.com',
    'https://pornhub.com',
    'https://kat.cr',
    'https://ok.ru',
    'https://blogger.com',
    'https://office.com',
    'https://whatsapp.com',
    'https://craigslist.org',
    'https://alibaba.com',
    'https://outbrain.com',
    'https://jd.com',
    'https://xhamster.com',
    'https://dropbox.com',
    'https://go.com',
    'https://coccoc.com',
    'https://popads.net',
    'https://bongacams.com',
    'https://wikia.com',
    'https://twitch.tv',
    'https://wangzhanbao.cc',
    'https://adf.ly',
    'https://booking.com',
    'https://haosou.com',
    'https://bbc.co.uk',
    'https://adobe.com',
    'https://chase.com',
    'https://flipkart.com',
    'https://163.com',
    'https://quora.com',
    'https://espn.gns.go.com',
    'https://sogou.com',
    'https://nytimes.com',
    'https://bilibili.com',
    'https://txxx.com',
    'https://bbc.com',
    'https://ettoday.net',
    'https://dailymotion.com',
    'https://bankofamerica.com',
    'https://zillow.com',
    'https://salesforce.com',
    'https://so.com',
    'https://vice.com',
    'https://walmart.com',
    'https://reddit.com',
    'https://indeed.com',
    'https://soundcloud.com',
    'https://adnetworkperformance.com',
    'https://godaddy.com',
    'https://zhihu.com',
    'https://mediafire.com',
    'https://doubleclick.net',
    'https://wellsfargo.com',
    'https://globo.com',
    'https://etsy.com',
    'https://slideshare.net',
    'https://detail.tmall.com.danuoyi.tbcache.com',
    'https://yelp.com',
    'https://nametests.com',
    'https://avito.ru',
    'https://onlinesbi.com',
    'https://steamcommunity.com',
    'https://weather.com',
    'https://stackexchange.com',
    'https://detik.com',
    'https://uptodown.com',
    'https://gfycat.com',
    'https://torrentz.eu',
    'https://naver.jp',
    'https://9gag.com',
    'https://pixiv.net',
    'https://taringa.net',
    'https://bet365.com',
    'https://vimeo.com',
    'https://slither.io',
    'https://putlocker.is',
    'https://tripadvisor.com',
    'https://steampowered.com',
    'https://taboola.com',
    'https://hclips.com',
    'https://skype.com',
    'https://blogspot.in',
    'https://flickr.com',
    'https://feedly.com',
    'https://nih.gov',
    'https://udn.com',
    'https://foxnews.com',
    'https://washingtonpost.com',
    'https://deviantart.com',
    'https://youporn.com',
    'https://rdsa2012.com',
    'https://tistory.com',
    'https://mega.nz',
    'https://web.de',
    'https://github.io',
    'https://target.com',
    'https://youm7.com',
    'https://livejournal.com',
    'https://orange.fr',
    'https://wittyfeed.com',
    'https://opthw.xdwscache.speedcdns.com',
    'https://iqiyi.com',
    'https://wikihow.com',
    'https://leboncoin.fr',
    'https://gmx.net',
    'https://mozilla.org',
    'https://fbcdn.net',
    'https://upornia.com',
    'https://americanexpress.com',
    'https://popcash.net',
    'https://forbes.com',
    'https://allegro.pl',
    'https://wix.com',
    'https://spotify.com',
    'https://theladbible.com',
    'https://onet.pl',
    'https://wikimedia.org',
    'https://irctc.co.in',
    'https://hdfcbank.com',
    'https://webtretho.com',
    'https://files.wordpress.com',
    'https://capitalone.com',
    'https://xfinity.com',
    'https://blog.jp',
    'https://terraclicks.com',
    'https://roblox.com',
    'https://weebly.com',
    'https://pandora.com',
    'https://bestbuy.com',
    'https://hulu.com',
    'https://t-online.de',
    'https://imzog.com',
    'https://shutterstock.com',
    'https://onedio.com',
    'https://usps.com',
    'https://groupon.com',
    'https://paytm.com',
    'https://tuberel.com',
    'https://1688.com',
    'https://chaturbate.com',
    'https://bitauto.com',
    'https://about.com',
    'https://wordpress.org',
    'https://rediff.com',
    'https://2ch.net',
    'https://goodreads.com',
    'https://sourceforge.net',
    'https://trello.com',
    'https://tokopedia.com',
    'https://ups.com',
    'https://eksisozluk.com',
    'https://youtube-mp3.org',
    'https://kaskus.co.id',
    'https://battle.net',
    'https://pinimg.com',
    'https://xuite.net',
    'https://slickdeals.net',
    'https://businessinsider.com',
    'https://zendesk.com',
    'https://ruten.com.tw',
    'https://oracle.com',
    'https://mama.cn',
    'https://dssedc4qxg7o6.cloudfront.net',
    'https://seznam.cz',
    'https://exoclick.com',
    'https://hp.com',
    'https://blogspot.com.br',
    'https://archive.org',
    'https://icloud.com',
    'https://kinogo.co',
    'https://adplxmd.com',
    'https://fedex.com',
    'https://blastingnews.com',
    'https://sberbank.ru',
    'https://addthis.com',
    'https://slack.com',
    'https://telegraph.co.uk',
    'https://giphy.com',
    'https://cnnic.cn',
    'https://life.tw',
    'https://liputan6.com',
    'https://hurriyet.com.tr',
    'https://kinopoisk.ru',
    'https://badoo.com',
    'https://liveadexchanger.com',
    'https://tradeadexchange.com',
    'https://dell.com',
    'https://att.com',
    'https://mailchimp.com',
    'https://thepiratebay.se',
    'https://secureserver.net',
    'https://reimageplus.com',
    'https://nyaa.se',
    'https://gizmodo.com',
    'https://loading-delivery2.com',
    'https://sabah.com.tr',
    'https://ppomppu.co.kr',
    'https://ouo.io',
    'https://rambler.ru',
    'https://OPENLOAD.co',
    'https://scribd.com',
    'https://bukalapak.com',
    'https://intuit.com',
    'https://evernote.com',
    'https://lowes.com',
    'https://blackboard.com',
    'https://rutracker.org',
    'https://airbnb.com',
    'https://blogfa.com',
    'https://messenger.com',
    'https://citi.com',
    'https://digikala.com',
    'https://taleo.net',
    'https://themeforest.net',
    'https://bloomberg.com',
    'https://ask.fm',
    'https://gmanetwork.com',
    'https://freepik.com',
    'https://doublepimp.com',
    'https://billdesk.com',
    'https://sahibinden.com',
    'https://lifebuzz.com',
    'https://verizonwireless.com',
    'https://macys.com',
    'https://nba.com',
    'https://medium.com',
    'https://blkget.com',
    'https://likes.com',
    'https://siteadvisor.com',
    'https://4shared.com',
    'https://wsj.com',
    'https://alicdn.com',
    'https://extratorrent.cc',
    'https://impress.co.jp',
    'https://wp.com',
    'https://sh.st',
    'https://instructure.com',
    'https://bild.de',
    'https://box.com',
    'https://savefrom.net',
    'https://hatena.ne.jp',
    'https://wetransfer.com',
    'https://tabelog.com',
    'https://mediab.uy',
    'https://kickstarter.com',
    'https://acfun.tv',
    'https://jabong.com',
    'https://ck101.com',
    'https://ancestry.com',
    'https://ameba.jp',
    'https://cnblogs.com',
    'https://olx.pl',
    'https://disqus.com',
    'https://kohls.com',
    'https://zippyshare.com',
    'https://spiegel.de',
    'https://mashable.com',
    'https://hdzog.com',
    'https://vk.me',
    'https://kissanime.to',
    'https://zoho.com',
    'https://agar.io',
    'https://mercadolibre.com.ar',
    'https://subscene.com',
    'https://thesportbible.com',
    'https://rt.com',
    'https://surveymonkey.com',
    'https://ozock.com',
    'https://telegram.org',
    'https://thefreedictionary.com',
    'https://buzzlie.com',
    'https://upwork.com',
    'https://realtor.com',
    'https://thewatchseries.to',
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
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.127 Safari/537.36'

# allow multiple user agents
USER_AGENTS = [
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