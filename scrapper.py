import scrapy


class Scrapper(scrapy.Spider):
    name = 'unsplashspider'
    start_urls = ['https://unsplash.com/s/photos/mountains']
    custom_settings = {'FEED_FORMAT': 'csv', 'FEED_URI': 'data.csv'}

    def parse(self, response):
        results = response.xpath(
            '//a[@class="_2Mc8_"]/@href')
        print(f'results: {results.getall()}')
        for url in response.xpath('//a[@class="_2Mc8_"]/@href'):
            yield {'url_image': url.get()}
