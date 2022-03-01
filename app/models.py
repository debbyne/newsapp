class Source:
    '''
    Class that defines sources of the articles
    
    '''
    def __init__(self,source_id,source_name,source_url,description):
        self.source_id=source_id
        self.source_name=source_name
        self.source_url=source_url
        self.description=description
        
class articles:
    '''
    class that defines articles
    '''
    def __init__(self,article,urlToImage,article_source,article_title,article_author,article_description,publishedAt,publishingDate,):
        self.urlToImage=urlToImage
        self.article_source=article_source
        self.article_title=article_title
        self.article_author=article_author
        self.article_description=article_description
        self.publishedAt=publishedAt
        self.publishingDate=publishingDate