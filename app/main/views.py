from unicodedata import category
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles,get_sources
from ..models import Source
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

    title = 'NEWSWAVE'
    return render_template('index.html', title = title,general = general_news,business=business,entertainment=Entertainment,health=health,sports=sports )

@main.route('/source/<source_id>')
def articles(id):
    '''
    function that returns articles from their sources.
    '''
    articles = get_articles(id)
    title = 'The hottest news right now'
    return render_template('articles.html', articles = articles, title = title)
