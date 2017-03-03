# name: an attribute specifying a unique name to identify the spider
# start_urls: an attribute listing the URLs the spider will start from
# parse(): a method of the spider responsible for processing a Response object downloaded from the URL and returning scraped data

from scrapy import Spider
from scrapy.selector import Selector
from demo.items import DemoItem

class Demo_Spider(Spider):
    name = 'demo_spider'
    allowed_urls = ['en.wikipedia.org']
    start_urls = ['''https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films''' ]
    temp = response.xpath('//*[@id="mw-content-text"]/table[1]/tr').extract()

