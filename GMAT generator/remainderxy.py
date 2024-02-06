from fractions import Fraction
from random import randint, choice, shuffle, sample

question_template = "When positive integer x is divided by 5, the remainder is 3; and when x is divided by 7, the remainder is 4.  When positive integer y is divided by 5, the remainder is 3; and when y is divided by 7, the remainder is 4.  If x > y, which of the following must be a factor of x-y?"

temp_answers = [12,15,20,28,35]
temp_correct = 35
source = "Official mba.com focus test"


def find_primes_to_y(x,y=500):
	factors = []
	if x>y:
		for i in range(2,y):
			if x%i == 0:
				factors.append(i)
	else:
		for i in range(2,int(x**.5)+1):
			if x%i ==0:
				factors.append(i)
				factors.append(int(x/i))
	return factors


answer_key = {}
counter =0
for i in range(20):
	counter+=1
	variation = 0
	if variation ==0:
		w = randint(2,50)
		z = randint(w,100)
		div1=randint(2,11)
		div2=randint(div1,15)
		total = z-w
		factors=find_primes_to_y(total)
		factors.append(total)
		answers = [12,15,20,28,35]
		correct_ans = 35
		answer_key[counter] = correct_ans
		question_text = f"{counter}. When positive integer z is divided by {div1}, the remainder is {z%div1}; and when z is divided by {div2}, the remainder is {z%div2}.  When positive integer w is divided by {div1}, the remainder is {w%div1}; and when w is divided by {div2}, the remainder is {w%div2}.  If z > w, which of the following must be a factor of z-w?"
		print(question_text)
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")
		print(f"{z=}{w=}{total=} {factors=}")
		print("\n\n\n")

print("ANSWER KEY")
for key in answer_key:
	print(f"{key}. {answer_key[key]}")