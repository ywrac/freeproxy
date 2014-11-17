# -*- coding: utf-8 -*-
import scrapy
from freeproxy.items import FreeproxyItem

class AtsushiSpider(scrapy.Spider):
    name = "atsushi"
    allowed_domains = ["www.freeproxylists.net"]
    start_urls = (
        "http://www.freeproxylists.net/?c=&pt=&pr=&a[]=0&a[]=1&a[]=2&u=90",
    )

    def parse(self, response):
        proxylist = response.xpath('//tr[@class="Even"]')
        item = FreeproxyItem()
        for proxy in proxylist:
            item['ip'] = proxy.xpath('./td[0]').extract()
            item['port'] = proxy.xpath('./td[1]').extract()
            yield item
