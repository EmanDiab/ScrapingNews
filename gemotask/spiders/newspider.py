import scrapy


class newspider(scrapy.Spider):
    name = "newspider"
    start_urls = ["https://www.bbc.com/"]

    def parse(self, response):
        links = []
        for news in response.css("div.media__content"):
            print(news)

            try:
                yield {
                    "title": news.css("a.media__link::text").get().strip().replace("\n", ""),
                    "link": "https://www.bbc.com" + news.css("a.media__link").attrib["href"],
                    "": links.append("https://www.bbc.com" + news.css("a.media__link").attrib["href"])
                }
            except:
                yield {
                    "title": None,
                    "link": None
                }
        for link in links:
            next_page = scrapy.Request(link)
            if next_page is not None:
                yield response.follow(response.urljoin(link), callback=self.parseArticle)

    def parseArticle(self, response):

        if response is not None:
            yield {
                "article_text": "\n".join(
                    response.xpath('//div[@class="ssrcss-18snukc-RichTextContainer e5tfeyi1"]/p/text()').extract())

            }
