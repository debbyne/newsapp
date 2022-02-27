from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='fc6938396cae425589db02011d0a5ee3')
sources = newsapi.get_sources()
print (sources)