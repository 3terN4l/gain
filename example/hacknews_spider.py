from gain import Css, Item, Parser, Spider, Xpath


class Post(Item):
    title = Css('.title a')
    url = Css('.title a', 'href')
    points = Css('.subtext .score')

    def save(self):
        print(self.results)


class User(Item):
    username = Css('.username')
    karma = Xpath('//[@class=karma]')

    def save(self):
        print(self.results)


class MySpider(Spider):
    start_url = 'https://news.ycombinator.com/'
    follow_rules = ['/news?p=\d+', ]
    parsers = [Parser('/item?id=\d+', Post),
               Parser('/user?id=\w+', User)]


MySpider.run()
