from newsapi.newsapi_client import NewsApiClient
from textblob import TextBlob


# Init
def newsapi(stock):
    # newsapi_symbol = input("Enter a symbol")
    newsapi = NewsApiClient(api_key='861ff0ffbaaa4eaa9571ce516cc5e088')

    all_articles = newsapi.get_everything(q=stock,
                                          language='en',
                                          sort_by='publishedAt',
                                          page_size=100)

    sources = newsapi.get_sources()

    title = []
    desc = []

    i = 1
    pos, neg, neu = 0, 0, 0

    for article in all_articles['articles']:
        a = str(article['content'])
        title.append(str(article['title']) + ' : \n' + str(article['description']))
        # desc.append(str(article['description']))
        b = article['source']
        c = article['publishedAt']
        # print(i, a)
        i += 1

        analysis = TextBlob(a)
        if analysis.sentiment.polarity > 0:
            # print('\nPositive:\n', a)
            # print('The source is:', b['name'])
            # print('It was published at:', c)
            pos += 1

        elif analysis.sentiment.polarity == 0:
            # print('\nNeutral:\n', a)
            # print('The source is:', b['name'])
            # print('It was published at:', c)
            neu += 1

        else:
            # print('\nNegative:\n', a)
            # print('The source is:', b['name'])
            # print('It was published at:', c)
            neg += 1

    # print(title)

    total = pos + neg + neu
    pos_news, neg_news, neu_news = pos/total, neg/total, neu/total

    if pos_news - neg_news > 0:
        # print('\nThe net value of News is: ', (pos_news - neg_news + 1)/2)
        output = ((pos_news - neg_news + 1)*100)/2
    else:
        # print("\nThe net value of News is: ", (pos_news - neg_news + 1)/2)
        output = ((pos_news - neg_news + 1)*100)/2
    # print(output)
    return output, title, desc


def get_articles(stock):
    newsapi = NewsApiClient(api_key='861ff0ffbaaa4eaa9571ce516cc5e088')

    all_articles = newsapi.get_everything(q=stock,
                                          language='en',
                                          sort_by='publishedAt',
                                          page_size=100)

    print(all_articles)

    return all_articles


# get_articles('bank of baroda')
