import scrapy


class OnzonespiderSpider(scrapy.Spider):
    name = "onzonespider"
    allowed_domains = ["www.ozone.bg"]
    start_urls = ["https://www.ozone.bg/mobilni-ustroistva/smartfoni/"]

    def parse(self, response):
        phones = response.css('div.col-xs-3')
        for phone in phones:

            phone_url = phone.css('a.product-box').attrib['href']

            yield response.follow(phone_url, callback=self.parse_book_page)
            # yield {
            #     'model': phone.css('span.title::text').get(),
            #     'price': phone.css("span.regular-price span.price::text").get()
            # }

        next_page = response.css('a.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_book_page(self, response):
        yield {
            'name': response.css("div.col-xs-5 h1::text").get(),
            'processor': response.css("ul.attribute-list > li:first-child span::text").get(),
            'screen size': response.css("ul.attribute-list > li:nth-child(2) span::text").get(),
            'RAM': response.css("ul.attribute-list > li:nth-child(4) span::text").get(),
            "HDD" : response.css("ul.attribute-list > li:nth-child(5) span::text").get(),
            'old_price': response.css("div.price-box p.old-price span.price::text").get(),
            'special_price':  response.css("div.price-box p.special-price span.price::text").get(),
        }