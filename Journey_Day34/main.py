from quiz_brain import QuizBrain, question_bank
from user_interface import QuizInterface

quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)

# A QuizBrain object is created to manage the quiz logic and is passed into QuizInterface  The interface then uses this object to
# fetch questions and check answers, while managing the GUI separately. This clean separation makes the code modular and easier to maintain