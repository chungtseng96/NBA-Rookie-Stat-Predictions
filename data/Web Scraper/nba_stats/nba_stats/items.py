# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NbaStatsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    player_name = scrapy.Field()
    player_age = scrapy.Field()
    player_gp = scrapy.Field()
    player_total_3pa = scrapy.Field()
    player_total_stl = scrapy.Field()
    player_total_blk = scrapy.Field()
    player_total_tov = scrapy.Field()
    player_fgp = scrapy.Field()
    player_3pp = scrapy.Field()
    player_ftp = scrapy.Field()
    player_ppg = scrapy.Field()
    player_rpg = scrapy.Field()
    player_apg = scrapy.Field()
    pass
