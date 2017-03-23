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
        rows = response.xpath('//*[@id="DataTables_Table_0"]').extract()
        # //*[@id="mw-content-text"]/table


        for i in range(1, 10481, 2):
            RDate = Selector(text=rows[i]).xpath('//td[2]/a/text()').extract()[0]
            # //*[@id="DataTables_Table_0"]/tbody/tr[1]/td[1]

            Title = Selector(text=rows[i]).xpath('//td[3]/b/a/text()').extract()[0]
            PBudget = Selector(text=rows[i]).xpath('//td[4]/text()').extract()[0]
            DomesticG = Selector(text=rows[i]).xpath('//td[5]/text()').extract()[0]
            WorldwideG = Selector(text=rows[i]).xpath('//td[6]/text()').extract()[0]


            item = BudgetItem()
            item['RDate'] = RDate
            item['Title'] = Title
            item['PBudget'] = PBudget
            item['DomesticG'] = DomesticG
            item['WorldwideG'] = WorldwideG

            yield item

