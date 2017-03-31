# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class NBA_Item(Item):
    # define the fields for your item here like:
    player = Field()
    pos = Field()
    _min = Field()
    FGM_A = Field()
    _3PM_A = Field()
    FTM_A = Field()
    plus_minus = Field()
    OFF = Field()
    DEF = Field()
    TOT = Field()
    AST = Field()
    PF = Field()
    ST = Field()
    TO = Field()
    BS = Field()
    BA = Field()
    PTS = Field()

    player_2 = Field()
    pos_2 = Field()
    _min_2 = Field()
    FGM_A_2 = Field()
    _3PM_A_2 = Field()
    FTM_A_2 = Field()
    plus_minus_2 = Field()
    OFF_2 = Field()
    DEF_2 = Field()
    TOT_2 = Field()
    AST_2 = Field()
    PF_2 = Field()
    ST_2 = Field()
    TO_2 = Field()
    BS_2 = Field()
    BA_2 = Field()
    PTS_2 = Field()

