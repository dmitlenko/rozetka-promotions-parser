from scrapy import Request
from scrapy.exceptions import CloseSpider
import scrapy

class RozetkaSpider(scrapy.Spider):
    name = 'rozetka'
    allowed_domains = ['rozetka.com.ua']
    start_urls = ['https://rozetka.com.ua/ua/news-articles-promotions/promotions/']

    def parse(self, response):
        # get list of promotions
        discounts = response.css("rz-promotion-tile")
        
        # stop parsing if discounts is not found
        if not response.css("span.promo-tile__rest-quantity::text"):
            raise CloseSpider("Виконання завершено")

        # parse discounts
        for discount in discounts:
            # get quantity
            quantity = discount.css("span.promo-tile__rest-quantity::text").extract_first()

            # if quantity is valid then return the data
            if quantity:
                yield {
                    "title": discount.css("span.promo-tile__heading::text").extract_first().strip(),
                    "time": discount.css("time::text").extract_first().strip(),
                    "quantity": quantity.strip(),
                    "link": discount.css("a.promo-tile::attr('href')").extract_first(),
                    "image": discount.css("img.promo-tile__picture::attr('src')").extract_first()
                }        

        # get the next page url
        next_page_url = response.css("a.button.button--gray.button--medium.pagination__direction.pagination__direction--forward.ng-star-inserted::attr('href')").extract_first()

        # if next page url found then make a request to this page
        if next_page_url:
            yield scrapy.Request(url = response.urljoin(next_page_url), callback = self.parse)