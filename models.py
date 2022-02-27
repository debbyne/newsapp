class Source:
    '''
    Class that defines sources of the articles
    
    '''
    def __init__(self,source_id,source_name,source_url):
        self.source_id=source_id
        self.source_name=source_name
        self.source_url=source_name
        
class articles:
    '''
    class that defines articles
    '''
    def __init__(self,article_image_url,article_source,article_title,article_author,article_description,time_published):
        self.article_image_url=article_image_url
        self.article_source=article_source
        self.article_title=article_title
        self.article_author=article_author
        self.article_description=article_description
        self.time_published=time_published