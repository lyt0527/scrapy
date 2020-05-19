# -*- coding: utf-8 -*-

# Scrapy settings for kandian project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'kandian'

SPIDER_MODULES = ['kandian.spiders']
NEWSPIDER_MODULE = 'kandian.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  "Cookie": "SINAGLOBAL=222.84.126.73_1574669744.664798; Apache=222.84.126.73_1574669744.664799; SUB=_2A25w3-AqDeRhGeVH71ES8SrNyTyIHXVTrVbirDV_PUJbm9BeLWKgkW9NT0ZAXQno9CYsH583-33rx2fX25N8Q013; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWJgo18YGLl.VUAv..RSpUQ5JpX5KzhUgL.Foe4She0eKBpeo52dJLoI0qLxKBLBonLBKzLxKBLBonL12BLxKBLBonL12zLxKML1-2L1hBLxKqL1KnLB-qLxKBLB.BLBK5t; ULV=1574670480217:1:1:1:222.84.126.73_1574669744.664799:; U_TRS1=000000ed.97a81e9a2.5ddb9091.462bef12; U_TRS2=000000ed.97b31e9a2.5ddb9091.27880e91; UM_distinctid=16ea535ce9c3c9-0b284fe1114047-3a3a5d0c-15f900-16ea535ce9d133; __gads=Test; CNZZDATA1261995448=869208448-1574726531-%7C1574731931; CNZZDATA5847902=cnzz_eid%3D1889717851-1574726494-%26ntime%3D1574731894; CNZZDATA1278178973=521825001-1574726340-%7C1574731740; UOR=mp.sina.com.cn,k.sina.com.cn,spr_auto_trackid_7aed00f9534d5b79:1574735320667; CNZZDATA5661630=cnzz_eid%3D783896589-1574725677-%26ntime%3D1574732837; CNZZDATA1264476941=1754544531-1574725696-%7C1574732810; CNZZDATA5581086=cnzz_eid%3D1314876077-1574725730-%26ntime%3D1574732873; CNZZDATA5581080=cnzz_eid%3D1356435430-1574725798-%26ntime%3D1574732906; CNZZDATA1260051864=2090945156-1574725816-%7C1574732809; CNZZDATA5581074=cnzz_eid%3D948452737-1574725845-%26ntime%3D1574733001"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'kandian.middlewares.KandianSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'kandian.middlewares.KandianDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'kandian.pipelines.KandianPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
