# Python 3.4+
from abc import ABC, abstractmethod

class Summarizer(ABC):
    @abstractmethod
    def summarize(self, text: str):
        pass
        
class Tagger(ABC):
    @abstractmethod
    def extract_tags(self, text: str):
        pass
