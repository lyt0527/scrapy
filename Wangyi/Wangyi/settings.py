# -*- coding: utf-8 -*-

# Scrapy settings for Wangyi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Wangyi'

SPIDER_MODULES = ['Wangyi.spiders']
NEWSPIDER_MODULE = 'Wangyi.spiders'


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
CONCURRENT_REQUESTS_PER_IP = 40

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "_ntes_nnid=f2963dda672d88d2f22232a2a96f0589,1588127776908; _ntes_nuid=f2963dda672d88d2f22232a2a96f0589; WM_NI=Iq8oHhGX28zmtrIw7WgNGf3ZEMy%2FndDOOpA2Yp8mpxn0MnfyBeso6a%2F51ojuXnscgPkoRpq%2Bc24nlF89iG4M8QObQl90JS%2BUvEKkZgLjLUrGP3aHXjvog8rIuPTo2Y%2FKc1g%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb1bb7ef799aa8cef68f28a8fa3d85e968b9aaaae4ab68bab95e263f58b8ca7f32af0fea7c3b92a8baff890cb648588fed9f967b8ae8798b65da5928987b2528793b7d0ed7088918191c43a9bb0f88ef374aef0838fe57382bbbd90b56bedebff90e97f9cb2bd84e65ca9b19e91f421a1eefc8fef4efce7a7a8b747fc8f8183d468fbf086b4aa5fb69b858cd96d90b684b6f14d94edafa9db62b6b1a9d9f143b7909c90b153ed95add2e637e2a3; WM_TID=WMQfB4L86HxBUEEURAI%2BU7EPtM3vVWAo; NTESwebSI=D95D14E3922E8F5D8070C097BFE8FB3E.hz-subscribe-web-docker-cm-online-rpqqn-8gfzd-exh2j-7797b5r94cg-8081",
        "Host": "dy.163.com",
        "Referer": "http://dy.163.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Wangyi.middlewares.WangyiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Wangyi.middlewares.WangyiDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Wangyi.pipelines.WangyiPipeline': 300,
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
