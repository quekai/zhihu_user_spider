# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class User_info_Item(scrapy.Item):
    #     包含用户主要信息
    name = scrapy.Field()
    headline = scrapy.Field()
    avatar_url = scrapy.Field()
    follower_count = scrapy.Field()
    gender = scrapy.Field()
    id = scrapy.Field()
    is_advertiser = scrapy.Field()
    url_token = scrapy.Field()
    url = scrapy.Field()
    user_type = scrapy.Field()
    images = scrapy.Field()



