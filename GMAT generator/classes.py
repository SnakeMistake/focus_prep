class Question():
	def __init__(self,text,answers,data={}):
		self.text = text
		self.answers = answers
		self.data = data
	def ask(self):
		text = self.text
		answers = self.answers
		print(text)
		MC = {
		0:"A",
		1:"B",
		2:"C",
		3:"D",
		4:"E"
		}
		for i,item in enumerate(answers):
			print(f"{MC[i]}. {item}")

class QuestionSet():
	def __init__(self,questions,data={}):
		self.questions = questions
		self.data = data


mc_test = Question("What's the right answer?",[0,1,2,3,4])
mc_test.ask()
print(mc_test.data)