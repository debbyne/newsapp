from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles,get_sources,search_article
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    print('githfn')
    #getting latest news
    trending_news = get_articles('trending')
    general_news= get_articles('general')
    politics = get_articles('politics')
    business = get_articles('business')
    Entertainment = get_articles('entertainment')
    health = get_articles('health')
    sports = get_articles('sports')

    sources = get_sources()
    search_articles = request.args.get('query')
    title = 'Home-News Wave,Telling it as it is'
    # if search_article:
    #     return redirect(url_for('main.search',name=search_article))
    # else:
    return render_template('index.html', title = title, trending=trending_news,general=general_news,politics=politics,business=business,entertainment=Entertainment,health=health,sports=sports )

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
        articles_present = search_article()
        title = 'Search Results | Newswave'
        
        return render_template('search.html',title = title, articles = articles_present )