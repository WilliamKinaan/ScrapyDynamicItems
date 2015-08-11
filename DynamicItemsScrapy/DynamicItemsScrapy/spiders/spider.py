from scrapy.spiders import Spider
from scrapy.selector import Selector
from DynamicItemsScrapy.items import Website

class spider(Spider):
    name = "dynamicItemsSpider"
    allowed_domains = ["dmoz.org"]
    start_urls=["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/","http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []
        for site in sites:
            item = Website()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)
        return items