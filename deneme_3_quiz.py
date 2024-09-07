class Question :
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer) :
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    

q1 = Question("Soru 1",["a","b","c","d"],"c")
q2 = Question("Soru 2",["a","b","c","d"],"b")
q3 = Question("Soru 3",["a","b","c","d"],"a")
q4 = Question("Soru 4",["a","b","c","d"],"a")
q5 = Question("Soru 5",["a","b","c","d"],"c")

sorular = [q1,q2,q3,q4,q5]

# print(q1.checkAnswer("c"))
# print(q2.checkAnswer("b"))
# print(q3.checkAnswer("a"))
# print(q4.checkAnswer("b"))
# print(q5.checkAnswer("c"))

quiz = Quiz(sorular)


print(quiz.getQuestion().text)
print(quiz.getQuestion().answer)



