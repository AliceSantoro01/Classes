class Question:
    def __init__ (self):
        self._text = ""
        self._answer = ""

    def setText(self, questionText):
        self._text = questionText
    
    def setAnswer (self, correct_answer):
        self._answer = correct_answer

    def checkAnswer (self, given_answer):
        return given_answer.lower() == self._answer.lower()
    
    def display (self):
        print(self._text)

    def ask_question (self):
        self.display()
        answer = input ("Write the answer: ")
        return self.checkAnswer(answer)
    



class ChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self._choices = []
    

    def addChoice(self, choice, correct):       

        """Add a choice with the associated boolean value"""

        self._choices.append (choice)
        if correct:
            choiceString = str(len(self._choices))
            self.setAnswer(choiceString)


    def display (self):
        super().display()
        for i in range (len(self._choices)):
            choiceNumber = i + 1
            print ("%d: %s" % (choiceNumber, self._choices[i]))
    



class FillInQuestion(Question):
    def __init__(self):
        super().__init__()

    def display(self):
        showed_question = self._text.split("_")
        showed_question [1] = "_"*len(self._answer)
        showed_question = "".join(showed_question)
        print(showed_question)




class MultiChoiceQuestion(ChoiceQuestion):
    def __init__(self):
        super().__init__()
        self._correct_choices_num_option = []


    def addChoice(self, choice, correct):
        self._choices.append(choice)
        if correct:
            self._correct_choices_num_option.append(len(self._choices))


    def checkAnswer(self, given_answer):
        answer_components = given_answer.split(" ")                                         
        answer_components = [int(num_option) for num_option in answer_components]     
        return all (guess in self._correct_choices_num_option for guess in answer_components) and len(answer_components) == len(self._correct_choices_num_option)

    def ask_question(self):
        self.display()
        answer = input("It is possible that there are multiple correct answers. In this case, you need to indicate all of them. Write the number or numbers corresponding to the answers you want to give, separated by spaces.")
        return self.checkAnswer(answer)
    



class AnyCorrectChoiceQuestion(ChoiceQuestion):
    def __init__(self):
        super().__init__()
        self._correct_choices_num_option = []


    def addChoice(self, choice, correct):
        self._choices.append(choice)
        if correct:
            self._correct_choices_num_option.append(len(self._choices))        


    def checkAnswer(self, given_answer):
        answer_components = given_answer.split(" ")
        answer_components = [int(num_option) for num_option in answer_components ]
        return any(guess in self._correct_choices_num_option for guess in answer_components)

    def ask_question(self):
        self.display()
        answer = input("It is possible that there are multiple correct answers. In this case, you need to indicate at least one. Write the number or numbers corresponding to the answers you want to give, separated by spaces.")
        return self.checkAnswer(answer)
    



class NumericQuestion(Question):
    def __init__ (self):
        super().__init__()

    def checkAnswer (self, response):
        return abs (float(self._answer) - float(response)) <= 0.01
    



def test_questions():
    questions = []

    q1 = FillInQuestion()
    q1.setText("Italian singer nicknamed La tigre di Cremona _Mina_")
    q1.setAnswer("Mina")
    questions.append(q1)
   
    

    q2 = MultiChoiceQuestion()
    q2.setText("Which of the following are songs by TOOL?")
    q2.addChoice("The misshapen steed",False)
    q2.addChoice("Arluck", False)
    q2.addChoice("Lateralus", True)
    q2.addChoice("Parabola", True)
    questions.append(q2)
   
    

    q3 = AnyCorrectChoiceQuestion()
    q3.setText("Which of the following are songs by Blind Guardian or Sevdaliza?")
    q3.addChoice("And then there was silence", True)
    q3.addChoice("In the aeroplane over the sea ",False)
    q3.addChoice("Humana",True)
    q3.addChoice("Dust it off", False)
    questions.append(q3)
   
    

    q4 = NumericQuestion()
    q4.setText("1 + 1?")
    q4.setAnswer("2")
    questions.append(q4)
    
    

    
    correct_answers = 0
    for question in questions:
        if question.ask_question():
            correct_answers += 1
    
    
    print("You answered correctly to " +str(correct_answers) +  " out of " +str(len(questions)))
    if correct_answers == len(questions):
        print("Way to go!")
    elif correct_answers >= (len(questions))/2:
        print("Yay!")
    else:
        print("Shoot.")


test_questions()