import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):

    def __init__(self):
        consumer_key = 'fQAd4AySyC2MHcvJtPOrjjIZy'
        consumer_secret = 'QI1JZT4brFlHSG2oTUcAfgfLCDyH4Ddr7yLt2u9kPoQ6naaI7z'
        access_token = '4216952913-H3HM9UzHTuLmC3WN2BWsQ9DD7xGLDmDNXIJGU7I'
        access_token_secret = 'Hd1mGWDdPQvzlb0Aqx4rMBBZREh1MiBck9DpiPN1wspdM'

        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+:\ / \ / \S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        # print('\nTweet is: \n', tweet, '\n', analysis.sentiment)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=10):
        tweets = []

        try:
            fetched_tweets = self.api.search(q=query, count=count)

            for tweet in fetched_tweets:
                parsed_tweet = {}

                parsed_tweet['text'] = tweet.text
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            return tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))


def main():
    api = TwitterClient()
    final_tweets = []

    tweets_sensex = api.get_tweets(query='Sensex', count=20000)
    ptweets_sensex = [tweet for tweet in tweets_sensex if tweet['sentiment'] == 'positive']
    pos = (100 * len(ptweets_sensex)) / len(tweets_sensex)
    # print("Positive tweets percentage: {} %".format(100 * len(ptweets_sensex) / len(tweets_sensex)))
    ntweets_sensex = [tweet for tweet in tweets_sensex if tweet['sentiment'] == 'negative']
    neg = (100 * len(ntweets_sensex)) / len(tweets_sensex)
    # print("Negative tweets percentage: {} %".format(100 * len(ntweets_sensex) / len(tweets_sensex)))
    neutweets_sensex = [tweet for tweet in tweets_sensex if tweet['sentiment'] == 'neutral']
    neu = (100 * (len(tweets_sensex) - len(ptweets_sensex) - len(ntweets_sensex)) / len(tweets_sensex))
    # print("Neutral tweets percentage: {} % ".format(100 * (len(tweets_sensex) - len(ptweets_sensex) -
    # len(ntweets_sensex)) / len(tweets_sensex)))

    sensex = (pos - neg + 1) / 200
    # print(sensex)

    for t in tweets_sensex:
        final_tweets.append(t['text'])
    # print('---------------------------------------------------------------------')

    tweets_nifty = api.get_tweets(query='Nifty', count=20000)
    ptweets_nifty = [tweet for tweet in tweets_nifty if tweet['sentiment'] == 'positive']
    pos = (100 * len(ptweets_nifty)) / len(tweets_nifty)
    # print("Positive tweets percentage: {} %".format(100 * len(ptweets_nifty) / len(tweets_nifty)))
    ntweets_nifty = [tweet for tweet in tweets_nifty if tweet['sentiment'] == 'negative']
    neg = (100 * len(ntweets_nifty)) / len(tweets_nifty)
    # print("Negative tweets percentage: {} %".format(100 * len(ntweets_nifty) / len(tweets_nifty)))
    neutweets_nifty = [tweet for tweet in tweets_nifty if tweet['sentiment'] == 'neutral']
    neu = (100 * (len(tweets_nifty) - len(ptweets_nifty) - len(ntweets_nifty)) / len(tweets_nifty))
    # print("Neutral tweets percentage: {} % ".format(100 * (len(tweets_nifty) - len(ptweets_nifty) -
    # len(ntweets_nifty)) / len(tweets_nifty)))

    nifty = (pos - neg + 1) / 200

    for t in tweets_nifty:
        final_tweets.append(t['text'])

    # print('---------------------------------------------------------------------')

    tweets_BlueChip = api.get_tweets(query='BlueChip', count=20000)
    ptweets_BlueChip = [tweet for tweet in tweets_BlueChip if tweet['sentiment'] == 'positive']
    pos = (100 * len(ptweets_BlueChip)) / len(tweets_BlueChip)
    # print("Positive tweets percentage: {} %".format(100 * len(ptweets_BlueChip) / len(tweets_BlueChip)))
    ntweets_BlueChip = [tweet for tweet in tweets_BlueChip if tweet['sentiment'] == 'negative']
    neg = (100 * len(ntweets_BlueChip)) / len(tweets_BlueChip)
    # print("Negative tweets percentage: {} %".format(100 * len(ntweets_BlueChip) / len(tweets_BlueChip)))
    neutweets_BlueChip = [tweet for tweet in tweets_BlueChip if tweet['sentiment'] == 'neutral']
    neu = (100 * (len(tweets_BlueChip) - len(ptweets_BlueChip) - len(ntweets_BlueChip)) / len(tweets_BlueChip))
    # print("Neutral tweets percentage: {} % ".format(100 * (len(tweets_BlueChip) - len(ptweets_BlueChip) -
    # len(ntweets_BlueChip)) / len(tweets_BlueChip)))
    bluechip = (pos - neg + 1) / 200

    for t in tweets_BlueChip:
        final_tweets.append(t['text'])

    # print('---------------------------------------------------------------------')

    tweets_BSE = api.get_tweets(query='BSE', count=20000)
    ptweets_BSE = [tweet for tweet in tweets_BSE if tweet['sentiment'] == 'positive']
    pos = (100 * len(ptweets_BSE)) / len(tweets_BSE)
    # print("Positive tweets percentage: {} %".format(100 * len(ptweets_BSE) / len(tweets_BSE)))
    ntweets_BSE = [tweet for tweet in tweets_BSE if tweet['sentiment'] == 'negative']
    neg = (100 * len(ntweets_BSE)) / len(tweets_BSE)
    # print("Negative tweets percentage: {} %".format(100 * len(ntweets_BSE) / len(tweets_BSE)))
    neutweets_BSE = [tweet for tweet in tweets_BSE if tweet['sentiment'] == 'neutral']
    neu = (100 * (len(tweets_BSE) - len(ptweets_BSE) - len(ntweets_BSE)) / len(tweets_BSE))
    # print("Neutral tweets percentage: {} % ".format(100 * (len(tweets_BSE) - len(ptweets_BSE) -
    # len(ntweets_BSE)) / len(tweets_BSE)))
    bse = (pos - neg + 1) / 200

    for t in tweets_BSE:
        final_tweets.append(t['text'])

    # print('---------------------------------------------------------------------')

    tweets_Equity = api.get_tweets(query='Equity', count=20000)
    ptweets_Equity = [tweet for tweet in tweets_Equity if tweet['sentiment'] == 'positive']
    pos = (100 * len(ptweets_Equity)) / len(tweets_Equity)
    # print("Positive tweets percentage: {} %".format(100 * len(ptweets_Equity) / len(tweets_Equity)))
    ntweets_Equity = [tweet for tweet in tweets_Equity if tweet['sentiment'] == 'negative']
    neg = (100 * len(ntweets_Equity)) / len(tweets_Equity)
    # print("Negative tweets percentage: {} %".format(100 * len(ntweets_Equity) / len(tweets_Equity)))
    neutweets_Equity = [tweet for tweet in tweets_Equity if tweet['sentiment'] == 'neutral']
    neu = (100 * (len(tweets_Equity) - len(ptweets_Equity) - len(ntweets_Equity)) / len(tweets_Equity))
    # print("Neutral tweets percentage: {} % ".format(100 * (len(tweets_Equity) - len(ptweets_Equity) -
    # len(ntweets_Equity)) / len(tweets_Equity)))
    equity = (pos - neg + 1) / 200

    for t in tweets_Equity:
        final_tweets.append(t['text'])

    # print('---------------------------------------------------------------------')

    tweets_IndianShareMarket = api.get_tweets(query='IndianShareMarket', count=20000)
    ptweets_IndianShareMarket = [tweet for tweet in tweets_IndianShareMarket if tweet['sentiment'] == 'positive']
    pos = (100 * len(ptweets_IndianShareMarket)) / len(tweets_IndianShareMarket)
    # print("Positive tweets percentage: {} %".format(100 * len(ptweets_IndianShareMarket) / len(tweets_IndianShareMarket)))
    ntweets_IndianShareMarket = [tweet for tweet in tweets_IndianShareMarket if tweet['sentiment'] == 'negative']
    neg = (100 * len(ntweets_IndianShareMarket)) / len(tweets_IndianShareMarket)
    #print("Negative tweets percentage: {} %".format(100 * len(ntweets_IndianShareMarket) / len(tweets_IndianShareMarket)))
    neutweets_IndianShareMarket = [tweet for tweet in tweets_IndianShareMarket if tweet['sentiment'] == 'neutral']
    neu = (100 * (len(tweets_IndianShareMarket) - len(ptweets_IndianShareMarket) - len(ntweets_IndianShareMarket)) / len(
        tweets_IndianShareMarket))
    #print("Neutral tweets percentage: {} % ".format(100 * (len(tweets_IndianShareMarket) - len(ptweets_IndianShareMarket) -len(ntweets_IndianShareMarket)) / len(tweets_IndianShareMarket)))

    indiansharemarket = (pos - neg + 1) / 200

    for t in tweets_IndianShareMarket:
        final_tweets.append(t['text'])

    # print('---------------------------------------------------------------------')

    tweets_IndianStockMarket = api.get_tweets(query='IndianStockMarket', count=20000)
    ptweets_IndianStockMarket = [tweet for tweet in tweets_IndianStockMarket if tweet['sentiment'] == 'positive']
    pos = (100 * len(ptweets_IndianStockMarket)) / len(tweets_IndianStockMarket)
    #print("Positive tweets percentage: {} %".format(100 * len(ptweets_IndianStockMarket) / len(tweets_IndianStockMarket)))
    ntweets_IndianStockMarket = [tweet for tweet in tweets_IndianStockMarket if tweet['sentiment'] == 'negative']
    neg = (100 * len(ntweets_IndianStockMarket)) / len(tweets_IndianStockMarket)
    # print("Negative tweets percentage: {} %".format(100 * len(ntweets_IndianStockMarket) / len(tweets_IndianStockMarket)))
    neutweets_IndianStockMarket = [tweet for tweet in tweets_IndianStockMarket if tweet['sentiment'] == 'neutral']
    neu = (100 * (len(tweets_IndianStockMarket) - len(ptweets_IndianStockMarket) - len(ntweets_IndianStockMarket)) / len(tweets_IndianStockMarket))
    # print("Neutral tweets percentage: {} % ".format(100 * (len(tweets_IndianStockMarket) - len(ptweets_IndianStockMarket) - len(ntweets_IndianStockMarket)) / len(tweets_IndianStockMarket)))

    indianstockmarket = (pos - neg + 1) / 200

    for t in tweets_IndianStockMarket:
        final_tweets.append(t['text'])

    # print('---------------------------------------------------------------------')

    tweets_NationalStockExchange = api.get_tweets(query='NationalStockExchange', count=20000)
    ptweets_NationalStockExchange = [tweet for tweet in tweets_NationalStockExchange if
                                     tweet['sentiment'] == 'positive']
    pos = (100 * len(ptweets_NationalStockExchange)) / len(tweets_NationalStockExchange)
    # print("Positive tweets percentage: {} %".format(100 * len(ptweets_NationalStockExchange) / len(tweets_NationalStockExchange)))
    ntweets_NationalStockExchange = [tweet for tweet in tweets_NationalStockExchange if
                                     tweet['sentiment'] == 'negative']
    neg = (100 * len(ntweets_NationalStockExchange)) / len(tweets_NationalStockExchange)
    #print("Negative tweets percentage: {} %".format(100 * len(ntweets_NationalStockExchange) / len(tweets_NationalStockExchange)))
    neutweets_NationalStockExchange = [tweet for tweet in tweets_NationalStockExchange if
                                       tweet['sentiment'] == 'neutral']
    neu = (100 * (len(tweets_NationalStockExchange) - len(ptweets_NationalStockExchange) - len(
        ntweets_NationalStockExchange)) / len(tweets_NationalStockExchange))
    #print("Neutral tweets percentage: {} % ".format(100 * (len(tweets_NationalStockExchange) - len(ptweets_NationalStockExchange) - len(ntweets_NationalStockExchange)) / len(tweets_NationalStockExchange)))
    nationalstockexchange = (pos - neg + 1) / 200

    for t in tweets_NationalStockExchange:
        final_tweets.append(t['text'])

    #print('---------------------------------------------------------------------')

    tweets_NSE = api.get_tweets(query='NSE', count=20000)
    ptweets_NSE = [tweet for tweet in tweets_NSE if tweet['sentiment'] == 'positive']
    pos = (100 * len(ptweets_NSE)) / len(tweets_NSE)
    #print("Positive tweets percentage: {} %".format(100 * len(ptweets_NSE) / len(tweets_NSE)))
    ntweets_NSE = [tweet for tweet in tweets_NSE if tweet['sentiment'] == 'negative']
    neg = (100 * len(ntweets_NSE)) / len(tweets_NSE)
    #print("Negative tweets percentage: {} %".format(100 * len(ntweets_NSE) / len(tweets_NSE)))
    neutweets_NSE = [tweet for tweet in tweets_NSE if tweet['sentiment'] == 'neutral']
    neu = (100 * (len(tweets_NSE) - len(ptweets_NSE) - len(ntweets_NSE)) / len(tweets_NSE))
    #print("Neutral tweets percentage: {} % ".format(100 * (len(tweets_NSE) - len(ptweets_NSE) - len(ntweets_NSE)) / len(tweets_NSE)))
    nse = (pos - neg + 1) / 200

    for t in tweets_NSE:
        final_tweets.append(t['text'])

    #print('---------------------------------------------------------------------')

    tweets_IndianRupee = api.get_tweets(query='IndianRupee', count=20000)
    ptweets_IndianRupee = [tweet for tweet in tweets_IndianRupee if tweet['sentiment'] == 'positive']
    pos = (100 * len(ptweets_IndianRupee)) / len(tweets_IndianRupee)
    #print("Positive tweets percentage: {} %".format(100 * len(ptweets_IndianRupee) / len(tweets_IndianRupee)))
    ntweets_IndianRupee = [tweet for tweet in tweets_IndianRupee if tweet['sentiment'] == 'negative']
    neg = (100 * len(ntweets_IndianRupee)) / len(tweets_IndianRupee)
    #print("Negative tweets percentage: {} %".format(100 * len(ntweets_IndianRupee) / len(tweets_IndianRupee)))
    neutweets_IndianRupee = [tweet for tweet in tweets_IndianRupee if tweet['sentiment'] == 'neutral']
    neu = (100 * (len(tweets_IndianRupee) - len(ptweets_IndianRupee) - len(ntweets_IndianRupee)) / len(
        tweets_IndianRupee))
    #print("Neutral tweets percentage: {} % ".format(100 * (len(tweets_IndianRupee) - len(ptweets_IndianRupee) - len(ntweets_IndianRupee)) / len(tweets_IndianRupee)))
    indianrupee = (pos - neg + 1) / 200

    for t in tweets_IndianRupee:
        final_tweets.append(t['text'])

    # print('---------------------------------------------------------------------')

    tweets_StockTrading = api.get_tweets(query='StockTrading', count=20000)
    ptweets_StockTrading = [tweet for tweet in tweets_StockTrading if tweet['sentiment'] == 'positive']
    pos = (100 * len(ptweets_StockTrading)) / len(tweets_StockTrading)
    #print("Positive tweets percentage: {} %".format(100 * len(ptweets_StockTrading) / len(tweets_StockTrading)))
    ntweets_StockTrading = [tweet for tweet in tweets_StockTrading if tweet['sentiment'] == 'negative']
    neg = (100 * len(ntweets_StockTrading)) / len(tweets_StockTrading)
    #print("Negative tweets percentage: {} %".format(100 * len(ntweets_StockTrading) / len(tweets_StockTrading)))
    neutweets_StockTrading = [tweet for tweet in tweets_StockTrading if tweet['sentiment'] == 'neutral']
    neu = (100 * (len(tweets_StockTrading) - len(ptweets_StockTrading) - len(ntweets_StockTrading)) / len(
        tweets_StockTrading))
    #print("Neutral tweets percentage: {} % ".format(100 * (len(tweets_StockTrading) - len(ptweets_StockTrading) - len(ntweets_StockTrading)) / len(tweets_StockTrading)))
    stocktrading = (pos - neg + 1) / 200

    for t in tweets_StockTrading:
        final_tweets.append(t['text'])

    # print('---------------------------------------------------------------------')

    tweets_bombaystockexchange = api.get_tweets(query='BombayStockExchange', count=20000)
    ptweets_bombaystockexchange = [tweet for tweet in tweets_bombaystockexchange if tweet['sentiment'] == 'positive']
    pos = (100 * len(ptweets_bombaystockexchange)) / len(tweets_bombaystockexchange)
    # print("Positive tweets percentage: {} %".format(100 * len(ptweets_bombaystockexchange) /
    # len(tweets_bombaystockexchange)))
    ntweets_bombaystockexchange = [tweet for tweet in tweets_bombaystockexchange if tweet['sentiment'] == 'negative']
    neg = (100 * len(ntweets_bombaystockexchange)) / len(tweets_bombaystockexchange)
    # print("Negative tweets percentage: {} %".format(100 * len(ntweets_bombaystockexchange) /
    # len(tweets_bombaystockexchange)))
    neutweets_bombaystockexchange = [tweet for tweet in tweets_bombaystockexchange if tweet['sentiment'] == 'neutral']
    neu = (100 * (len(tweets_bombaystockexchange) - len(ptweets_bombaystockexchange) - len(ntweets_bombaystockexchange)) / len(
        tweets_bombaystockexchange))
    # print("Neutral tweets percentage: {} % ".format(100 * (len(tweets_bombaystockexchange)
    # - len(ptweets_bombaystockexchange) - len(ntweets_bombaystockexchange)) / len(tweets_bombaystockexchange)))
    bombaystockexchange = (pos - neg + 1) / 200

    for t in tweets_bombaystockexchange:
        final_tweets.append(t['text'])

    # print('---------------------------------------------------------------------')
    twittersentimentscore = ((sensex + nifty + bluechip + bse + equity + indiansharemarket + indianstockmarket +
                             indianrupee + nationalstockexchange + nse + bombaystockexchange) * 100) / 11
    # print(twittersentimentscore)
    # print(newsapi())
    # print(final_tweets)
    return twittersentimentscore, final_tweets


if __name__ == "__main__":
    main()
