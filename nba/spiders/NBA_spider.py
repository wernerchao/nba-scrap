# name: an attribute specifying a unique name to identify the spider
# start_urls: an attribute listing the URLs the spider will start from
# parse(): a method of the spider responsible for processing a Response object downloaded from the URL and returning scraped data

from scrapy import Spider
from scrapy.selector import Selector
from nba.items import NBA_Item

class NBA_Spider(Spider):
    name = 'NBA_spider'
    allowed_urls = ['www.teamrankings.com']
    start_urls = ['https://www.teamrankings.com/nba/stat/offensive-efficiency?date=%d-06-20' % i for i in range(2005, 2016)]

    def parse(self, response):
        rows = response.xpath('//*[@id="html"]/body/div[2]/div[1]/div[2]/main/table/tbody/tr').extract()

        for row in rows:
            Rank = Selector(text=row).xpath('//td[1]/text()').extract()
            Team = Selector(text=row).xpath('//td[2]/a/text()').extract()
            Current_Yr_Off = Selector(text=row).xpath('//td[3]/text()').extract()
            Last_3 = Selector(text=row).xpath('//td[4]/text()').extract()
            Last_1 = Selector(text=row).xpath('//td[5]/text()').extract()
            Home = Selector(text=row).xpath('//td[6]/text()').extract()
            Away = Selector(text=row).xpath('//td[7]/text()').extract()
            Last_Yr_Off = Selector(text=row).xpath('//td[8]/text()').extract()

            item = NBA_Item()
            item['Rank'] = Rank
            item['Team'] = Team
            item['Current_Yr_Off'] = Current_Yr_Off
            item['Last_3'] = Last_3
            item['Last_1'] = Last_1
            item['Home'] = Home
            item['Away'] = Away
            item['Last_Yr_Off'] = Last_Yr_Off
            yield item


# u'<tr>
# \r\n\t\t\t
# <td class="rank text-center" data-sort="1">1</td>
# \r\n\t\t\t\t
# <td class="text-left nowrap" data-sort="Golden State">
#     <a href="https://www.teamrankings.com/nba/team/golden-state-warriors">Golden State</a>
# </td>
# \r\n\t\t\t\t
# <td class="text-right" data-sort="1.10002">1.100</td>
# \r\n\t\t\t\t
# <td class="text-right" data-sort="0.970742">0.971</td>
# \r\n\t\t\t\t
# <td class="text-right" data-sort="0.946557">0.947</td>
# \r\n\t\t\t\t
# <td class="text-right" data-sort="1.11977">1.120</td>
# \r\n\t\t\t\t
# <td class="text-right" data-sort="1.07907">1.079</td>
# \r\n\t\t\t\t
# <td class="text-right" data-sort="1.07459">1.075</td>
# \r\n\t\t\t</tr>'