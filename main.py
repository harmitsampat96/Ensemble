from newsSentimentAnalysis import newsapi
from twitterSentimentAnalysis import main
from technicalAnalysis import technicalanalysis
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# plt.rcParams["figure.figsize"] = (10, 2)


def get_analysis(stock):
    y_test, y_predict_svr, y_predict_mlp, Date_test = technicalanalysis(stock)
    twitter_sentiment_value, final_tweets = main()
    news_sentiment_value, title, desc = newsapi(stock)

    final_value = []
    for i in range(len(y_test)):
        final_value.append(0.44*y_predict_svr[i] + 0.44*y_predict_mlp[i] + 0.06*twitter_sentiment_value + 0.06*news_sentiment_value)

    score = r2_score(y_test, final_value) * 100

    # print(final_value)
    #print("Final tweets: ", final_tweets)
    #print('R Square Error:', r2_score(y_test, final_value) * 100)

    final = list(final_value)

    final = final[-300:]
    y_average = sum(final) / float(len(final))

    last_value = sum(final[-30:]) / float(len(final[-30:]))

    if last_value > y_average:
        n = 1
        print('Buy the stock')
    elif last_value < y_average:
        n = -1
        print('Sell the stock')
    else:
        n = 0
        print('Hold the stock')

    print(score)

    return final_value, news_sentiment_value, twitter_sentiment_value, score, n


def get_tweets():
    twitter_sentiment_value, final_tweets = main()
    return final_tweets


get_analysis('Oracle')




