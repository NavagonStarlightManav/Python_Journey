import requests
import html
from Question_model import *

parameters={
    "amount": 10,
    "type": "boolean",
}

response=requests.get(url="https://opentdb.com/api.php?",params=parameters)
response.raise_for_status()

data=response.json()

question_data=data['results']

question_bank = []


for item in question_data:
    question = item["question"]
    answer = item["correct_answer"]
    ques = QuestionModel(question, answer)
    question_bank.append(ques)


class QuizBrain:
    def __init__(self, q_list):
        self.Question_number = 0
        self.Question_list = q_list
        self.score = 0

    def still_has_Questions(self):
        return self.Question_number <= len(self.Question_list)-1

    def check_answer(self, user_answer):

        if user_answer.lower() == self.current_question.answer.lower():
            self.score+=1
            return True
        else:
            return False

    def next_question(self):
        print("Sir be ready to answer some great questions")
        self.current_question = self.Question_list[self.Question_number]
        self.Question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q {self.Question_number}: {q_text} True/False"
