import scrapy


class newspider(scrapy.Spider):
    name = "newspider"
    start_urls = ["https://www.bbc.com/"]

    def parse(self, response):
        xp = "//div[@class='media__content']//a[@class='media__link']/@href"
        return (scrapy.Request(url, callback=self.parseArticle) if url.startswith("htt") else scrapy.Request("https://www.bbc.com/" +url , callback=self.parseArticle)  for url in response.xpath(xp).extract())


    def parseArticle(self, response):

        if response is not None:
            try:
                yield {
                    "title": response.css("h1::text").get(),
                    "link": response.xpath("//meta[@property='og:url']/@content").get(),
                    "author": response.xpath(
                        "//a[@class='author-unit__text b-font-family-serif']/text()").get().replace("By ", ""),
                    "article_text": "\n".join(
                        response.xpath('//div[@class="ssrcss-18snukc-RichTextContainer e5tfeyi1"]/p/text()').extract())
                }
            except:
                yield {
                    "title": response.css("h1::text").get(),
                    "link": response.xpath("//meta[@property='og:url']/@content").get(),
                    "author": None,
                    "article_text": "\n".join(
                        response.xpath('//div[@class="ssrcss-18snukc-RichTextContainer e5tfeyi1"]/p/text()').extract())
                }
