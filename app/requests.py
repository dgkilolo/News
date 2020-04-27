from app import app 
import urllib.request,json
from .models import News,Articles

# News = news.News
# Articles = news.Articles


# Getting api key
api_key = None


# Getting the news base url
source_base_urls = None


def configure_request(app):
    global api_key,source_base_urls, articles_base_urls
    api_key = app.config['NEWS_API_KEY']
    source_base_urls = app.config["NEWS_API_BASE_URL"]
    articles_base_urls = app.config['NEWS_API_ARTICLES_URL']


# Getting the articles base url
# articles_base_urls = app.config['NEWS_API_ARTICLES_URL']

def process_results(news_results):
  '''
  processes the results and transforms them into a list

  args:
    news_results: a dictionary containing sources details
  returns:
    a list of source objects
  '''

  process_results = []
  
  for source_item in news_results:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    category = source_item.get('category')
    url = source_item.get('url')

    source_object = News(id,name,description,category,url)
    process_results.append(source_object)

  return process_results

def get_news():
  '''
  Function that gets the json response from our url request.
  '''
  source_base_url = source_base_urls.format(api_key)
  print(source_base_url)

  with urllib.request.urlopen(source_base_url) as url:
    sources_data = url.read()
    sources_response = json.loads(sources_data)

    source_results = None

    if sources_response['sources']:
      sources_result_list = sources_response['sources']
      sources_results = process_results(sources_result_list)

  return sources_results

def get_articles(source_id):
  '''
  Function that gets the json response from the source url
  '''
  article_url = articles_base_urls.format('top-headlines', source_id, api_key)
  print(article_url)
  with urllib.request.urlopen(article_url) as url:
    article_data = url.read()
    articles_response = json.loads(article_data)

    if articles_response['articles']:
      article_list = articles_response['articles']

      article_result_list = []

      for article in article_list:
        author = article.get('author')
        title = article.get('title')
        descriptions = article.get('description')
        publishedAt = article.get('publishedAt')
        url = article.get('url')
        content = article.get('content')
        urlToImage = article.get('urlToImage')

        articles_object = Articles(author,title,descriptions,publishedAt,url,content,urlToImage)
        article_result_list.append(articles_object)
  return  article_result_list

