

from abc import ABC, abstractmethod


def Converter(args):
    @abstractmethod
    def convert(self, dataFrame, *args) -> list:
        pass

    def print(self, objects: list):
        for obj in objects:
            print(obj.describe())
    pass
