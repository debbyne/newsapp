import os

class Config:
    
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey=API_KEY'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ARTICLE_BASE_URL ='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'





class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}