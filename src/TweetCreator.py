# -*- coding: utf-8 -*-
#Need Encapsulation!!
#Ask Steve about how python documentation is done

import datetime
import randrange
from PathFinder import PathFinder
from Enum import Enum


class qCardTypes(Enum):

    def __init__(self):
        super(qCardTypes, self).__init__()
        self.FILLBLANK
        self.QUESTION


class TweetCreator:

    def __init__(self):
        self = self
        self.__choose__qCard()
        self.__find__aCardNo()
        self.__find__qCardType()
        self.__choose__aCards()
        self.__create__tweetStr()
        self.__encode__tweetStr()

    def __choose__qCard(self):
        date = datetime.date
        month = date.month
        if month == 12:
            if randrange(1, 2) == 1:
                finder = PathFinder("Questions.txt")
                infile = open(finder.getPath())
                qCards = infile.readlines()
                CardNo = randrange(0, len(qCards))
                self.__qCard = qCards[CardNo]
            else:
                finder = PathFinder("Holiday Expansion Questions.txt")
                infile = open(finder.getPath())
                qCards = infile.readlines()
                CardNo = randrange(0, len(qCards))
                self.__qCard = qCards[CardNo]
        else:
            finder = PathFinder("Questions.txt")
            infile = open(finder.getPath())
            qCards = infile.readlines()
            CardNo = randrange(0, len(qCards))
            self.__qCard = qCards[CardNo]

    def __find__aCardNo(self):
        found = False
        for i in range(2, 6):
            search = "{p" + i + "}"
            if self.__qCard.find(search) != -1:
                self.__qCard = self.__qCard.replace(search, "")
                self.__aCardNo = i
                found = True
        if found is False:
            self.__aCardNo = 1

    def __find__qCardType(self):
        if self.__qCard.find("_") != -1:
            self.__qCardType = qCardTypes.FILLBLANK
        else:
            self.__qCardType = qCardTypes.QUESTION

    def __getAnswerCard():
        date = datetime.date
        month = date.month
        if month == 12:
            if randrange(1, 2) == 1:
                finder = PathFinder("Answers.txt")
                infile = open(finder.getPath())
                aCards = infile.readlines()
                CardNo = randrange(0, len(aCards))
                __aCard = aCards[CardNo]
            else:
                finder = PathFinder("Holiday Expansion Answers.txt")
                infile = open(finder.getPath())
                aCards = infile.readlines()
                CardNo = randrange(0, len(aCards))
                __aCard = aCards[CardNo]
        else:
            finder = PathFinder("Answers.txt")
            infile = open(finder.getPath())
            aCards = infile.readlines()
            CardNo = randrange(0, len(aCards))
            __aCard = aCards[CardNo]
        return __aCard

    def __choose__aCards(self):
        self.__aCards = []
        for i in range(self.__aCardNo):
            self.__aCards = self.__aCards + [self.__getAnswerCard()]

    def __create__tweetStr(self):
        if self.__qCardType == qCardTypes.FILLBLANK:
            splitQCard = self.__qCard.split("_")
            for i in range(self.__aCardNo):
                self.__tweetStr = splitQCard[i] + self.__aCards[i]
        else:
            self.__tweetStr = self.__qCard + "\n" + self.__aCards[0]
            if self.__aCardNo != 1:
                for i in range(self.__aCardNo - 1):
                    self.__tweetStr = self.__tweetStr + self.__aCards[i + 1]

    def __encode__tweetStr(self):
        self.__tweetStr = self.__tweetStr.replace("\u00F1", "ñ")
        self.__tweetStr = self.__tweetStr.replace("\u00ED", "í")
        self.__tweetStr = self.__tweetStr.replace("[LINE]", "\n")

    def getTweetStr(self):
        return self.__tweetStr