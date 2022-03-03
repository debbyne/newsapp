from unicodedata import category
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles,get_sources
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #getting latest news
    general_news= get_sources('general')
    business = get_sources('business')
    Entertainment = get_sources('entertainment')
    health = get_sources('health')
    sports = get_sources('sports')

    search_articles = request.args.get('query')
    title = 'NEWSWAVE'
    # if search_article:
    #     return redirect(url_for('main.search',name=search_article))
    # else:
    return render_template('index.html', title = title,general=general_news,business=business,entertainment=Entertainment,health=health,sports=sports )

@main.route('/articles/<source_id>')
def source(source_id):
    '''
    function that returns articles from their sources.
    '''
    articles = get_sources(source_id)
    title = 'The hottest news right now'

    return render_template('articles.html', articles = articles, title = title)

# @main.route('/search/<name>')
# def search(name):
#         '''
#         View function to display the search results
#         '''
#         terms = name.split(' ')
#         query = '+'.join(terms)
#         articles_present = search_article()
#         title = 'Search Results | Newswave'
        
#         return render_template('search.html',title = title, articles = articles_present )
@main.route('/trial')
def trial_source():
    '''
    function that returns articles from their sources.
    '''
    articles = get_articles()
    title = 'The hottest news right now'

    return render_template('trial.html', articles = articles, title = title)