from flask import render_template
from app import app
from .requests import get_news,get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting the sources
    sources = get_news()
    print(sources)

    title = 'News Updates'
    return render_template('index.html', title = title, sources = sources )

@app.route('/search/<source_id>')
def sourceArticles(source_id):
    '''
    Function that displays the articles from a particluar source.
    '''
    article_results = get_articles(source_id)

    title =  source_id

    return render_template("article.html",title = title, articles = article_results)