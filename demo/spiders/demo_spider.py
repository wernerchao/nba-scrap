# name: an attribute specifying a unique name to identify the spider
# start_urls: an attribute listing the URLs the spider will start from
# parse(): a method of the spider responsible for processing a Response object downloaded from the URL and returning scraped data

from scrapy import Spider
from scrapy.selector import Selector
from demo.items import DemoItem

class Demo_Spider(Spider):
    name = 'demo_spider'
    allowed_urls = ['www.teamrankings.com']
    start_urls = ['https://www.teamrankings.com/nba/stat/offensive-efficiency?date=2016-06-20' ]

    def parse(self, response):
        rows = response.xpath('//*[@id="html"]/body/div[2]/div[1]/div[2]/main/table/tbody/tr').extract()

        for row in rows:
            Rank = Selector(text=row).xpath('//td[1]/text()')[0].extract()
            Team = Selector(text=rows[i]).xpath('//td[2]/text()')[0].extract()
            Year_2015 = Selector(text=rows[i]).xpath('//td[3]/text()')[0].extract()
            Last_3 = Selector(text=rows[i]).xpath('//td[4]/text()')[0].extract()
            Last_1 = Selector(text=rows[i]).xpath('//td[5]/text()')[0].extract()
            Home = Selector(text=rows[i]).xpath('//td[6]/text()')[0].extract()
            Away = Selector(text=rows[i]).xpath('//td[7]/text()')[0].extract()
            Year_2014 = Selector(text=rows[i]).xpath('//td[8]/text()')[0].extract()

            item = BudgetItem()
            item['RDate'] = RDate
            item['Title'] = Title
            item['PBudget'] = PBudget
            item['DomesticG'] = DomesticG
            item['WorldwideG'] = WorldwideG

            yield item