import datetime
import urllib.request, json
from .models import articles, Source
from datetime import date

api_key = None
base_url = None
articles_url=None
def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url=app.config['ARTICLE_BASE_URL']
def get_articles(id):
    '''
    function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(id,api_key)

    with urllib.request.urlopen(articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['sources']:
            articles_results_list = get_articles_response['sources']
            articles_results=process_articles_results(articles_results_list)

    return articles_results
def process_articles_results(articles_results_list):
    """
    Function that process the list of article from the request.
    """
    articles_results = []
    for individual_article in articles_results_list:
        title = individual_article.get('title')
        description = individual_article.get('description')
        url = individual_article.get('url')
        urlToImage = individual_article.get('urlToImage')
        publishedAt = individual_article.get('publishedAt')
        # convert date from json to string and backto my specific  format
        publishing_date = datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
        publishedAt = publishing_date.strftime('%d.%m.%Y')
        article_object = articles(title, description, url, urlToImage, publishedAt,publishing_date)
        articles_results.append(article_object)
    return articles_results

def get_sources(category):
    '''
    function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results=process_sources_results(sources_results_list)

    return sources_results
def process_sources_results(sources_results_list):
    """
    Function that process the list of sources from the request.
    """
    sources_results = []
    for individual_sources in sources_results_list:
        source_name=individual_sources.get('name')
        source_url = individual_sources.get('url')
        source_id=individual_sources.get('id')
        description=individual_sources.get('description')

        source_object = Source(source_id,source_name,source_url,description)
        sources_results.append(source_object)
    return sources_results
# def search_article():
#     pass