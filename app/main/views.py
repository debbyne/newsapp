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
    print(general_news[0].source_name)
    return render_template('index.html', title = title,general = general_news,business=business,entertainment=Entertainment,health=health,sports=sports )

# @main.route('/Source/<source_id>')
# def Source(category):
#     '''
#     function that returns articles from their sources.
#     '''
#     Sources = get_sources(category)
#     title = 'The hottest news right now'

#     return render_template('index.html', Sources=Sources, title = title)
