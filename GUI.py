from flask import Flask, render_template, request
from main import get_analysis, get_tweets
from newsSentimentAnalysis import newsapi, get_articles
import datetime

# from Jinchart.jinchart import doughnutchart

app = Flask(__name__)

# register the filter
# app.jinja_env.filters['doughnutchart'] = doughnutchart

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC',
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC',
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC',
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC',
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/forecast', methods=['POST', 'GET'])
def forecast():

    if request.method == 'POST':
        stock = request.form['stock']

        final_value, final_tweets, news_sentiment_value, twitter_sentiment_value, score, date = get_analysis(stock)

        # example chart
        # lines_of_code_written = {'labels': ['January', 'February', 'March'], "Jacques": [3400, 5700, 9800],
        #                          "Thomas": [4100, 1700, 2800]}

        return render_template(
            "forecast.html",
            stock=stock,
            title='Stock price forecast',
            max=1000,
            labels=labels,
            values=final_value,
            tweets=final_tweets,
            sentiment_news=news_sentiment_value,
            sentiment_twitter=twitter_sentiment_value,
            score=score,
            # loc=lines_of_code_written
        )


@app.route('/tweets')
def tweet():

    final_tweets = get_tweets()

    return render_template(
        "tweets.html",
        stock='Bank of Baroda',
        title='Stock price forecast',
        tweets=final_tweets
    )


@app.route('/news/<name>')
def news(name):

    if name == 'BOB':
        all_articles = get_articles('Bank of Baroda')
        name = 'Bank of Baroda'
    elif name == 'Colgate':
        all_articles = get_articles('Colgate')
        name = 'Colgate'
    elif name == 'NIFTY':
        all_articles = get_articles('NIFTY')
        name = 'NIFTY'
    elif name == 'JSW':
        all_articles = get_articles('JSW steel')
        name = 'JSW steel'
    elif name == 'Oracle':
        all_articles = get_articles('Oracle')
        name = 'Oracle'
    elif name == 'Bosch':
        all_articles = get_articles('Bosch')
        name = 'Bosch'
    elif name == 'REL':
        all_articles = get_articles('Reliance')
        name = 'Reliance'
    else:
        all_articles = get_articles(name)

    return render_template(
        "news.html",
        stock=name,
        title='Stock price forecast',
        articles=all_articles['articles']
    )


@app.route('/test', methods=['POST', 'GET'])
def test():

    if request.method == 'POST':
        stock = request.form['stock']

        final_value, news_sentiment_value, twitter_sentiment_value, score, n = get_analysis(stock)

        base = datetime.date.today()
        dates = [base - datetime.timedelta(days=x) for x in range(0, 30)]
        dates.reverse()

        return render_template(
            "template.html",
            stock=stock,
            title='Stock price forecast',
            max=20000,
            labels=dates,
            values=final_value[-30:],
            sentiment_news=news_sentiment_value,
            sentiment_twitter=twitter_sentiment_value,
            score=score,
            n=n
            # loc=lines_of_code_written
        )


if __name__ == "__main__":
    app.run(debug=True)
