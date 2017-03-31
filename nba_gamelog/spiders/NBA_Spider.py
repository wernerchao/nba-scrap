# name: an attribute specifying a unique name to identify the spider
# start_urls: an attribute listing the URLs the spider will start from
# parse(): a method of the spider responsible for processing a Response object downloaded from the URL and returning scraped data

from scrapy import Request
from scrapy import Spider
from scrapy.selector import Selector
from nba_gamelog.items import NBA_Item

class NBA_Spider(Spider):
    name = 'NBA_Spider'
    allowed_urls = ['www.nba.com']
    start_urls = ['http://www.nba.com/gameline/20160226/']

    def parse(self, response): 
        for href in response.css("a.recapAnc::attr('href')")[0:1]:
            url = response.urljoin(href.extract())
            yield Request(url, callback = self.parse_item) 
        # for period in range(1,15): 
        #     url = self.lineup_pattern % (self.date, self.date, period, self.season) 
        #     yield Request(url, callback=self.parse_lineups)


    def parse_item(self, response):
        rows = response.xpath('//*[@id="nbaGITeamStats"]/tr').extract()

        for row in rows:
            player = Selector(text=row).xpath('//td[1]/a/text()').extract()
            pos = Selector(text=row).xpath('//td[2]/text()').extract()
            _min = Selector(text=row).xpath('//td[3]/text()').extract()
            FGM_A = Selector(text=row).xpath('//td[4]/text()').extract()
            _3PM_A = Selector(text=row).xpath('//td[5]/text()').extract()
            FTM_A = Selector(text=row).xpath('//td[6]/text()').extract()
            plus_minus = Selector(text=row).xpath('//td[7]/text()').extract()
            OFF = Selector(text=row).xpath('//td[8]/text()').extract()
            DEF = Selector(text=row).xpath('//td[9]/text()').extract()
            TOT = Selector(text=row).xpath('//td[10]/text()').extract()
            AST = Selector(text=row).xpath('//td[11]/text()').extract()
            PF = Selector(text=row).xpath('//td[12]/text()').extract()
            ST = Selector(text=row).xpath('//td[13]/text()').extract()
            TO = Selector(text=row).xpath('//td[14]/text()').extract()
            BS = Selector(text=row).xpath('//td[15]/text()').extract()
            BA = Selector(text=row).xpath('//td[16]/text()').extract()
            PTS = Selector(text=row).xpath('//td[17]/text()').extract()

            item = NBA_Item()
            item['player'] = player
            item['pos'] = pos
            item['_min'] = _min
            item['FGM_A'] = FGM_A
            item['_3PM_A'] = _3PM_A
            item['FTM_A'] = FTM_A
            item['plus_minus'] = plus_minus
            item['OFF'] = OFF
            item['DEF'] = DEF
            item['TOT'] = TOT
            item['AST'] = AST
            item['PF'] = PF
            item['ST'] = ST
            item['TO'] = TO
            item['BS'] = BS
            item['BA'] = BA
            item['PTS'] = PTS

            player_2 = Selector(text=row).xpath('//td[1]/a/text()').extract()
            pos_2 = Selector(text=row).xpath('//td[2]/text()').extract()
            _min_2 = Selector(text=row).xpath('//td[3]/text()').extract()
            FGM_A_2 = Selector(text=row).xpath('//td[4]/text()').extract()
            _3PM_A_2 = Selector(text=row).xpath('//td[5]/text()').extract()
            FTM_A_2 = Selector(text=row).xpath('//td[6]/text()').extract()
            plus_minus_2 = Selector(text=row).xpath('//td[7]/text()').extract()
            OFF_2 = Selector(text=row).xpath('//td[8]/text()').extract()
            DEF_2 = Selector(text=row).xpath('//td[9]/text()').extract()
            TOT_2 = Selector(text=row).xpath('//td[10]/text()').extract()
            AST_2 = Selector(text=row).xpath('//td[11]/text()').extract()
            PF_2 = Selector(text=row).xpath('//td[12]/text()').extract()
            ST_2 = Selector(text=row).xpath('//td[13]/text()').extract()
            TO_2 = Selector(text=row).xpath('//td[14]/text()').extract()
            BS_2 = Selector(text=row).xpath('//td[15]/text()').extract()
            BA_2 = Selector(text=row).xpath('//td[16]/text()').extract()
            PTS_2 = Selector(text=row).xpath('//td[17]/text()').extract()

            item['player_2'] = player_2
            item['pos_2'] = pos_2
            item['_min_2'] = _min_2
            item['FGM_A_2'] = FGM_A_2
            item['_3PM_A_2'] = _3PM_A_2
            item['FTM_A_2'] = FTM_A_2
            item['plus_minus_2'] = plus_minus_2
            item['OFF_2'] = OFF_2
            item['DEF_2'] = DEF_2
            item['TOT_2'] = TOT_2
            item['AST_2'] = AST_2
            item['PF_2'] = PF_2
            item['ST_2'] = ST_2
            item['TO_2'] = TO_2
            item['BS_2'] = BS_2
            item['BA_2'] = BA_2
            item['PTS_2'] = PTS_2
            yield item


# player = Field()
# pos = Field()
# min = Field()
# FGM_A = Field()
# _3PM_A = Field()
# FTM_A = Field()
# plus_minus = Field()
# OFF = Field()
# DEF = Field()
# TOT = Field()
# AST = Field()
# PF = Field()
# ST = Field()
# TO = Field()
# BS = Field()
# BA = Field()
# PTS = Field()

# <td id="nbaGIBoxNme" class="b"><a href="/playerfile/marvin_williams/index.html">M. Williams</a></td>
# <td class="nbaGIPosition">F</td>
# <td>34:53</td>
# <td>9-13</td>
# <td>5-9</td>
# <td>3-4</td>
# <td>+1</td>
# <td>2</td>
# <td>11</td>
# <td>13</td>
# <td>1</td>
# <td>2</td>
# <td>1</td>
# <td>1</td>
# <td>2</td>
# <td>0</td>
# <td>26</td>
