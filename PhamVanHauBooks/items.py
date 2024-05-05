# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhamVanHauBooksItem(scrapy.Item):
    bookURL = scrapy.Field()
    img = scrapy.Field()
    rating = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    title = scrapy.Field()
    number_of_reviews = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()