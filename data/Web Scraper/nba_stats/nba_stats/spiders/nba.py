# -*- coding: utf-8 -*-
import scrapy
from ..items import NbaStatsItem

class NbaSpider(scrapy.Spider):
    name = 'nba'
    year = 2018
    start_urls = ['https://www.basketball-reference.com/leagues/NBA_2019_rookies.html#rookies::none']

    def parse(self, response):
        items = NbaStatsItem()
        
        player_name = response.css('.right+ .left a').css('::text').extract()
        player_age = response.css('.left+ .right').css('::text').extract()
        player_gp = response.css('.right:nth-child(6)').css('::text').extract()
        player_total_3pa = response.css('.right:nth-child(11)').css('::text').extract()
        player_total_stl = response.css('.right:nth-child(17)').css('::text').extract()
        player_total_blk = response.css('.right:nth-child(18)').css('::text').extract()
        player_total_tov = response.css('.right:nth-child(19)').css('::text').extract()
        player_fgp = response.css('.right:nth-child(22)').css('::text').extract()
        player_3pp = response.css('.right:nth-child(23)').css('::text').extract()
        player_ftp = response.css('.right:nth-child(24)').css('::text').extract()
        player_ppg = response.css('.right:nth-child(26)').css('::text').extract()
        player_rpg = response.css('.right:nth-child(27)').css('::text').extract()
        player_apg = response.css('.right:nth-child(28)').css('::text').extract()
        
        items['player_name'] = player_name 
        items['player_age'] = player_age 
        items['player_gp'] = player_gp 
        items['player_total_3pa'] = player_total_3pa 
        items['player_total_stl'] = player_total_stl
        items['player_total_blk'] = player_total_blk
        items['player_total_tov'] = player_total_tov 
        items['player_fgp'] = player_fgp
        items['player_3pp'] = player_3pp
        items['player_ftp'] = player_ftp
        items['player_ppg'] = player_ppg
        items['player_rpg'] = player_rpg 
        items['player_apg'] = player_apg
        
        yield items
        
        next_page = 'https://www.basketball-reference.com/leagues/NBA_'+str(NbaSpider.year)+'_rookies.html#rookies::none'
        
        if NbaSpider.year > 2008:
            NbaSpider.year = NbaSpider.year - 1
            yield response.follow(next_page, callback = self.parse)
    
    
    
    
    
    