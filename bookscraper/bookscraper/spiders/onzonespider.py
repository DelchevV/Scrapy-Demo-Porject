import scrapy


class OnzonespiderSpider(scrapy.Spider):
    name = "onzonespider"
    allowed_domains = ["www.ozone.bg"]
    start_urls = ["https://www.ozone.bg/mobilni-ustroistva/smartfoni/"]

    def parse(self, response):
        phones = response.css('div.col-xs-3')
        for phone in phones:
            yield{
                'model': phone.css('span.title::text').get(),
            }

        next_page = response.css('a.next').attrib['href']
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
