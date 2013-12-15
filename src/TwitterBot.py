# -*- coding: utf-8 -*-
'''A class of object that acts as a twitterbot.'''
import time
import Tweet


class Twitterbot:
    #Constructor
    def __init__(self, minutes):
        self = self
        self.__freqency = frequency

    def __createTweet():
        tweet = Tweet()
        return tweet

    def __getTweetStr(self):
        tweet = self.__createTweet()
        while len(tweet.getTweetStr()) > 140:
            tweet = self.__createTweet()
        if len(tweet.getTweetStr() < 137):
            tweetStr = tweet.getTweetStr() + "#CAH"
            return tweetStr
        else:
            tweetStr = tweet.getTweetStr()
            return tweetStr

    def __tweet(self, tweetStr):
        #dont know how to get this on twitter Ask Steve

    def run(self):
        #Infinate loop
        while True:
            tweetStr = self.__getTweetStr()
            self.__tweet(tweetStr)
            time.sleep(self.__frequency * 60)
