import scrapy
from PhamVanHauBooks.items import PhamVanHauBooksItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ScrapybooksSpider(scrapy.Spider):
    name = "ScrapyBooks"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        # Trích xuất các liên kết đến trang chi tiết của từng cuốn sách
        book_links = response.css('article.product_pod h3 a::attr(href)').getall()
        for book_link in book_links:
            yield response.follow(book_link, callback=self.parse_book)

        # Tiếp tục theo dõi các trang tiếp theo nếu có
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        item = PhamVanHauBooksItem()
        item['bookURL'] = response.url
        item['name'] = response.css('h1::text').get()
        item['price'] = response.css('p.price_color::text').get()
        item['img'] = response.css('div.item.active img::attr(src)').get()
        # Trích xuất phần tử p có class chứa thông tin về số lượng sao
        star_element = response.xpath('//p[contains(@class, "star-rating")]')
        
        # Kiểm tra class của phần tử p để xác định số lượng sao
        star_class = star_element.xpath('@class').get()
        
        # Xác định số lượng sao dựa trên class
        if 'One' in star_class:
            item['rating'] = 1
        elif 'Two' in star_class:
            item['rating'] = 2
        elif 'Three' in star_class:
            item['rating'] = 3
        elif 'Four' in star_class:
            item['rating'] = 4
        elif 'Five' in star_class:
            item['rating'] = 5
        else:
            item['rating'] = None  # Trường hợp không xác định được số lượng sao
        yield item