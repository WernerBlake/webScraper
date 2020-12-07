import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://quizlet.com/488125084/networking-a-top-down-approach-chapter-1-flash-cards/',
    ]

    def parse(self, response):
        for quote in response.css("div.SetPage-terms"):
            yield {
                'Term': quote.css("a.SetPageTerm-wordText span.TermText::text").getall(),
            }
            yield {
                'Definition': quote.css("a.SetPageTerm-definitionText span.TermText::text").getall(),
            }