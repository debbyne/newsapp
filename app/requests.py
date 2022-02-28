from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='')
sources = newsapi.get_sources()
print (sources)