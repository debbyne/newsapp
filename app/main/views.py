from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_sources,search_article
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #getting latest news
    trending_news = get_news('trending')
    general_news= get_news('general')
    politics = get_news('politics')
    business = get_news('business')
    Entertainment = get_news('entertainment')
    health = get_news('health')
    sports = get_news('sports')

    sources = get_sources()
    search_articles = request.args.get('query')
    title = 'Home-News Wave,Telling it as it is'
    if search_article:
        return redirect(url_for('search',name=search_article))
    else:
        return render_template('index.html', title = title, trending=trending_news general=general_news,politics=politics,business=business,entertainment=Entertainment,health=health,sports=sports )

@main.route('/articles/<source_id>')
def source(source_id):
    '''
    function that returns articles from their sources.
    '''
    articles = get_sources(source_id)
    title = articles[0].article_source['name'] + ' | Newswave'

    return render_template('articles.html', articles = articles, title = title)

@main.route('/search/<name>')
def search(name):
        '''
        View function to display the search results
        '''
        terms = name.split(' ')
        query = '+'.join(terms)
        articles_present = search_article(query)
        title = 'Search Results | Newswave'
        
        return render_template('search.html',title = title, articles = articles_present )