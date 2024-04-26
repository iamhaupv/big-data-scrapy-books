import scrapy


class ScrapybooksSpider(scrapy.Spider):
    name = "ScrapyBooks"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        book = response.xpath('//div[@class="side_categories"]/ul/li/a/@href').getall()
        yield{ "book": book}
        books = response.xpath('//div[@class="side_categories"]/ul/li/ul/li/a/@href').getall()
        for bookItem in books:
            yield{
                "bookURL": bookItem
            }
