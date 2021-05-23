import scrapy


class newspider(scrapy.Spider):
    name = "newspider"
    start_urls = ["https://www.bbc.com/"]


    def parse(self, response):
        links = []
        for news in response.css("div.media__content"):
            print(news)
            links.append("https://www.bbc.com" + news.css("a.media__link").attrib["href"])
            try:
                yield {
                    "title": news.css("a.media__link::text").get().strip().replace("\n", ""),
                    "link": "https://www.bbc.com" + news.css("a.media__link").attrib["href"]
                }
            except:
                yield {
                    "title": None,
                    "link": None
                }



