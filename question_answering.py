from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from torch import torch
import time

tokenizer = AutoTokenizer.from_pretrained(
  "bert-large-uncased-whole-word-masking-finetuned-squad")
model = AutoModelForQuestionAnswering.from_pretrained(
  "bert-large-uncased-whole-word-masking-finetuned-squad")

print('Model loaded')
t1 = time.time()
text = "\n".join(open('article.txt').readlines())
questions = [
  "What's the job?",
  "What tools are used",
  "How much experience is needed?"
]

def answer_question(question: str) -> None:
  inputs = tokenizer.encode_plus(
    question, text, add_special_tokens=True, return_tensors="pt")
  input_ids = inputs["input_ids"].tolist()[0]

  answer_start_scores, answer_end_scores = model(**inputs)

  # Get the most likely beginning of answer with the argmax of the score
  answer_start = torch.argmax(answer_start_scores)
  # Get the most likely end of answer with the argmax of the score
  answer_end = torch.argmax(answer_end_scores) + 1

  answer = tokenizer.convert_tokens_to_string(
    tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))

  print(f"Question: {question}")
  print(f"Answer: {answer}\n")


for question in questions:
  answer_question(question)

t2 = time.time()
print(t2-t1)
while True:
  q = input("Ask me anything\t")
  answer_question(q)
