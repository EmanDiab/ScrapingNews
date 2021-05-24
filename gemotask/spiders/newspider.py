import scrapy
from gemotask.items import GemotaskItem

class newspider(scrapy.Spider):
    name = "newspider"
    start_urls = ["https://www.bbc.com/"]

    def parse(self, response):
        xp = "//div[@class='media__content']//a[@class='media__link']/@href"
        return (scrapy.Request(url, callback=self.parseArticle) if url.startswith("htt") else scrapy.Request("https://www.bbc.com/" +url , callback=self.parseArticle)  for url in response.xpath(xp).extract())


    def parseArticle(self, response):
        item = GemotaskItem()
        if response is not None:
            try:
                item["title"] = response.css("h1::text").get()
                item["link"] = response.xpath("//meta[@property='og:url']/@content").get()
                item["author"] = response.xpath(
                        "//a[@class='author-unit__text b-font-family-serif']/text()").get().replace("By ", "")
                item["article_text"] = "\n".join(
                        response.xpath('//div[@class="ssrcss-18snukc-RichTextContainer e5tfeyi1"]/p/text()').extract())
                yield item
            except:
                item["title"] = response.css("h1::text").get()
                item["link"] = response.xpath("//meta[@property='og:url']/@content").get()
                item["author"] = None
                item["article_text"] = "\n".join(
                    response.xpath('//div[@class="ssrcss-18snukc-RichTextContainer e5tfeyi1"]/p/text()').extract())
                yield item

