from transformers import pipeline
from abstract_classes import Summarizer

class NeuralTextSummarizer(Summarizer):
  def __init__(self):
    self.__summarizer = pipeline("summarization")
    #self.__summarizer = lambda x: [{"summary_text" : "hllo"}]
    
  def summarize(self, text):
    (a,) = self.__summarizer(text[:2500])
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
