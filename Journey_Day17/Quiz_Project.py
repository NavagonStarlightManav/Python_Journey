question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

que_data = [
    {
    "type": "boolean",
     "difficulty": "hard",
     "category": "History",
     "question": "Japan was part of the Allied Powers during World War I",
     "correct_answer": "True", "incorrect_answers": ["False"]
    },

            {"type": "boolean", "difficulty": "hard", "category": "History",
             "question": "The fourth funnel of the RMS Titanic was fake designed to make the ship look more powerful and symmetrical.",
             "correct_answer": "True", "incorrect_answers": ["False"]},

            {"type": "boolean", "difficulty": "hard", "category": "History",
             "question": "The USS Missouri (BB-63) last served in the Korean War.",
             "correct_answer": "False", "incorrect_answers": ["True"]},

            {"type": "boolean", "difficulty": "hard", "category": "History",
             "question": "The man that shot Alexander Hamilton was named Aaron Burr.",
             "correct_answer": "True", "incorrect_answers": ["False"]},

            {"type": "boolean", "difficulty": "hard", "category": "History",
             "question": "Joseph Stalin&#039;s real name was Ioseb Bessarionis dze Dzugashvili.",
             "correct_answer": "True", "incorrect_answers": ["False"]}
]

question_bank = []


class QuestionModel:

    def __init__(self, q_text, q_answer):
        self.text = q_text

        self.answer = q_answer


for item in question_data:
    question = item["text"]
    answer = item["answer"]
    ques = QuestionModel(question, answer)
    question_bank.append(ques)


class QuizBrain:
    def __init__(self, q_list):
        self.Question_number = 0
        self.Question_list = q_list
        self.score = 0

    def still_has_Questions(self):
        return self.Question_number < len(self.Question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"You guessed correctly sir ")
            self.score += 1
        else:
            print(f"You guessed incorrectly sir")
        print(f"The current score is {self.score}/{self.Question_number}")
        print("\n")

    def next_question(self):
        print("Sir be ready to answer some great questions")
        current_item = self.Question_list[self.Question_number]
        self.Question_number += 1
        user_answer = input(f"Q){self.Question_number}: {current_item.text} True/False")
        self.check_answer(user_answer, current_item.answer)


quiz_start = QuizBrain(question_bank)

while quiz_start.still_has_Questions():
    quiz_start.next_question()

print(f"you guessed correctly sir{quiz_start.score}")
