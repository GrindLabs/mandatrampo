import scrapy
from scrapy import Request


from mandatrampo.loaders import JobIntera


class InteraSpider(scrapy.Spider):
    name = 'intera'
    allowed_domains = ['byintera.com']
    start_urls = ['https://vagas.byintera.com/']

    def parse(self, response):
        for el in response.xpath('//div[@data-id="90e5c1d"]//h3[@class="elementor-post__title"]/a'):
            job = JobIntera(selector=el)
            job.add_xpath('title', 'text()')
            job.add_xpath('url', '@href')
            job.add_xpath('company', 'text()')
            job.add_value('sponsor', 'Intera')
            job.add_value('sponsor_logo', response.xpath(
                '//head/link[@sizes="192x192"]/@href').extract())
            yield Request(url=job.get_output_value('url'), callback=self.parse_logo, meta=dict(job=job))

    def parse_logo(self, response):
        job = response.meta['job']
        job.add_value('company_logo', response.xpath(
            '//div[@class="elementor-image"]/img/@src').extract())
        yield job.load_item()
