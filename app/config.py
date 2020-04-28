import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = 'cd613b4357b64293bb888c20c9aa8cea'
    NEWS_API_BASE_URL = 'http://newsapi.org/v2/sources?&apiKey={}'
    NEWS_API_ARTICLES_URL = 'http://newsapi.org/v2/{}?sources={}&apiKey={}'
    # NEWS_API_KEY = os.environ.get('NEWS_API_KEY')



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
'development':DevConfig,
'production':ProdConfig
}