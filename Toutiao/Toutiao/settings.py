# -*- coding: utf-8 -*-

# Scrapy settings for Toutiao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Toutiao'

SPIDER_MODULES = ['Toutiao.spiders']
NEWSPIDER_MODULE = 'Toutiao.spiders'


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
  'Cookie': '__tasessionId=hzul0s99p1574901981240; csrftoken=52a0e8851f34031af33d21c24749fc70; tt_webid=6764152452570924558; td_cookie=3234295447; tt_webid=6764152452570924558; sso_uid_tt=7caf3f68c9546c16cf13d128f67be448; toutiao_sso_user=a75dcee9a359656676fdb775b41fe669; sid_guard=48020d04f67b1e3171417e8e6dab4e6a%7C1574902266%7C5184000%7CMon%2C+27-Jan-2020+00%3A51%3A06+GMT; uid_tt=7cc1a8d32a7459ad5a4b0354855f925b; sid_tt=48020d04f67b1e3171417e8e6dab4e6a; sessionid=48020d04f67b1e3171417e8e6dab4e6a; s_v_web_id=9643dd2d18f520c807ee9d1457289f40; WEATHER_CITY=%E5%8C%97%E4%BA%AC\
            referer: https://graph.qq.com/oauth2.0/show?which=Login&display=pc&client_id=100290348&response_type=code&state=442a29b6jqFQqXF6b25lX3Nuc6FToKFO2TRodHRwczovL3Nzby50b3V0aWFvLmNvbS9hdXRoL2xvZ2luX3N1Y2Nlc3MvP3NlcnZpY2U9oVYBoUkAoUQAoUEYoU0YoUivd3d3LnRvdXRpYW8uY29toVIEolBMAKZBQ1RJT06goUy-aHR0cHM6Ly9zc28udG91dGlhby5jb20vbG9naW4voVTZIDczYjVlYTg4NGZmNWVlY2QwOTQ5NzBmZjU2NzYwYjAy&redirect_uri=https%3A%2F%2Fapi.snssdk.com%2Fauth%2Flogin_success&scope=get_user_info,add_share,add_t,add_pic_t,get_info,get_other_info,get_fanslist,get_idollist,add_idol,get_repost_list'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Toutiao.middlewares.ToutiaoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'Toutiao.middlewares.ToutiaoDownloaderMiddleware': 543,
   'Toutiao.middlewares.GetFailedUrl' : 543
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Toutiao.pipelines.ToutiaoPipeline': 300,
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
