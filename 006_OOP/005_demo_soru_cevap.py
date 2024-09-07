class Question :
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer) :
        return self.answer == answer

    
class Quiz :
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

        # self.displayQuestion()   # başka bir fonksiyonda (loadQuestion) göstrildi. Daha kullanışlı
    
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






q1 = Question("en iyi progralama dili", ["c#","c","ptyhon","php"], "php")
q2 = Question("mardinin plaka kodu kaçtır ?", ["34","44","47","49"], "47")
q3 = Question("türkiyenin başkenti", ["ankara","istanbul","şırnak","izmir"], "ankara")
questions = [q1,q2,q3]

# Quiz oluşturulmadan önce test edildi
# print(q1.checkAnswer("c"), q2.checkAnswer("47"), q3.checkAnswer("izmir"))

quiz = Quiz(questions)
# question = quiz.questions[quiz.questionIndex]  # getQuestion(self): daha kullanışlı
# question = quiz.getQuestion()  # displayQuestion daha kullanışlı
# print(question.text)

# quiz.displayQuestion()

quiz.loadQuestion()
