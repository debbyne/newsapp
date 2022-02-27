import unittest
from app import article
def setUp(self):
        '''
        Set up method to run before each test
        '''
        self.new_article = article('https://ichef.bbci.co.uk/news/1024/branded_news/636D/production/_123435452_sberbank.jpg',
        id": "bbc-news","name": "BBC News","Russia central bank urges calm amid cash run fears","https://www.facebook.com/bbcnews"",
        "The Bank of Russia says it has enough liquidity to 'function smoothly' despite new sanctions","2022-02-27T13:02:11Z",
        "An image alleged to be the display schematic for the iPhone 14 Pro series has emerged online, offering us a look at the true size of the pill-shaped and circular cutout design expected to debut on th… [+2624 chars]")
def __init__(self):
        '''
        to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_article,article))