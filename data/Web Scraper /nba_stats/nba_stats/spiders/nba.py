# -*- coding: utf-8 -*-
import scrapy
from ..items import NbaStatsItem

class NbaSpider(scrapy.Spider):
    name = 'nba'
    year = 2018
    start_urls = ['https://www.basketball-reference.com/leagues/NBA_2019_rookies.html#rookies::none']

    def parse(self, response):
        items = NbaStatsItem()
        
        for n in response.css('.right+ .left a').css('::text').extract():
            items['player_name'][n] = n
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
        
        #for n in range(len(player_name)):
            #items['player_name'][n] = player_name[n] 
            items['player_age'][n] = player_age[n] 
            items['player_gp'][n] = player_gp[n] 
            items['player_total_3pa'][n] = player_total_3pa[n] 
            items['player_total_stl'][n] = player_total_stl[n] 
            items['player_total_blk'][n] = player_total_blk[n] 
            items['player_total_tov'][n] = player_total_tov[n] 
            items['player_fgp'][n] = player_fgp[n] 
            items['player_3pp'][n] = player_3pp[n] 
            items['player_ftp'][n] = player_ftp[n] 
            items['player_ppg'][n] = player_ppg[n] 
            items['player_rpg'][n] = player_rpg[n] 
            items['player_apg'][n] = player_apg[n] 
        
        yield items
        
        next_page = 'https://www.basketball-reference.com/leagues/NBA_'+str(NbaSpider.year)+'_rookies.html#rookies::none'
        
        #if NbaSpider.year > 2008:
            #NbaSpider.year = NbaSpider.year - 1
            #yield response.follow(next_page, callback = self.parse)
    
    
    
    
    
    