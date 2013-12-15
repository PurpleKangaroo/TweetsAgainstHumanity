import os
import sys
#this class needs work
#Use the Java PathFinder class as a model


class PathFinder:

    def __init__(self, fileName):
        self.findPathString(fileName)

    def __findPathString(self, fileName):
        PathString = ""
        PathString = os.path.dirName(sys.argv[0])
        location = PathString.index['src']
        PathString = PathString[:location]
        self.__PathString = PathString + fileName

    def getPath(self):
        return self.__PathString