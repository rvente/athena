from transformers import pipeline
from abstract_classes import Summarizer

class NeuralTextSummarizer(Summarizer):
  """"""
  def __init__(self):
    self.__summarizer = pipeline("summarization")
    
  def summarize(self, text: str) -> str:
    """returns summary given text"""


    # truncate to first 2500 tokens: model limitation
    (a,) = self.__summarizer(text[:2500])

    # f(text) = [{"summary_text" : "This is a text summary"}]
    # so we need to get the string out of this return structure

    # TODO: take care of errors or empty summaries
    return a['summary_text'].strip().replace(' .','.')

if __name__ == '__main__':
  s = NeuralTextSummarizer()
  while True:
    try:
      input('Go?')
      ARTICLE = "\n".join(open('article.txt').readlines())
    except Exception as e:
      print(e)
      continue
    print(s.summarize(ARTICLE))
