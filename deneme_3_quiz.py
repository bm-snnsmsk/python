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
    
    def displayQuestion(self):
        soru = self.getQuestion()
        print(f"Soru {self.questionIndex + 1} : {soru.text}")

        for i in soru.choices :
            print("- ",i)
        
        answer = input("cevabınız :")
        # print(soru.checkAnswer(answer))
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self, answer) :
        soru = self.getQuestion()
        if soru.checkAnswer(answer) :
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self) : ## for döngüsüne gerek kalmadan döngüdeymiş gibi sürekli yeni bir soru getirir
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else :
            self.displayProgress()
            self.displayQuestion()

    def showScore(self) :
        print(f"Quiz bitti. Puanınız : {self.score}")
    
    def displayProgress(self) :
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        if questionNumber > totalQuestion :
            print(f"quiz bitti..Puanınız : {self.score}")
        else :
            print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))
    

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

quiz.loadQuestion()





