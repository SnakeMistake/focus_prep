from fractions import Fraction
from random import randint, choice, shuffle,sample

question_template = "If a certain toy store's revenue in November was 2/5 of its revenue in December and its revenue in January was 1/4 of its revenue in November, then the store's revenue in December was how many times the average (arithmetic mean) of its revenues in November and January?"
orig_question = "Online Exclusive <01065>"
wrong_ans=[Fraction(1,4),Fraction(1,2),Fraction(2,3),2]
right_ans=4


language_pool = [
{
"owner":"restaurant's",
"windows": ["March","April", "May"],
"stuff": "revenue",
"possessive": "its",
"generic_window": "months",
"unit": "USD"
},
{
"owner":"stock's",
"windows": ["Q1","Q2", "Q3"],
"stuff": "average price per share",
"possessive": "its",
"generic_window": "quarters",
"unit": ""
},
{
"owner":"truck driver's",
"windows": ["the trip from A to B","the trip from B to C", "the trip from C to D"],
"stuff": "mileage driven",
"possessive": "his",
"generic_window": "trips",
"unit": "miles"
},
{
"owner":"manufacturing company's",
"windows": ["the United States","Canada", "Mexico"],
"stuff": "number of facilities",
"possessive": "its",
"generic_window": "countries",
"unit":"facilities"
},
{
"owner":"journalist's",
"windows": ["2003","2004", "2005"],
"stuff": "number of publications",
"possessive": "their",
"generic_window": "years",
"unit":"publications"
},
]

counter = 0
answer_key = {}
for i in range(20):
	counter +=1
	c = randint(1,5)
	a = randint(c+1,7)
	b = randint(a+1,15)
	total = a+b+c
	a_of_b = Fraction(a,b)
	b_of_c = Fraction(b,c)
	b_of_a = Fraction(b,a)
	a_of_c = Fraction(a,c)
	c_of_a = Fraction(c,a)
	c_of_b = Fraction(c,b)
	c_p_of_a = int(round(c/a,2)*100)
	b_p_of_c = round((b/c)*100,3)
	c_of_tot = Fraction(c,total)
	a_to_b = f"{a_of_b.numerator} to {a_of_b.denominator}"
	b_to_c = f"{b_of_c.numerator} to {b_of_c.denominator}"
	b_to_a = f"{b_of_a.numerator} to {b_of_a.denominator}"
	total_avg = Fraction((a+b+c),3)
	avg_a_b = Fraction(a+b,2)
	avg_b_c = Fraction(b+c,2)
	avg_c_a = Fraction(a+c,2)
	a_of_avg = Fraction(a,total_avg)
	c_of_avg = Fraction(c,total_avg)
	range_a_c = c-a
	
	setting_count = counter%5
	setting_dict = language_pool[setting_count]
	owner =setting_dict['owner']
	window1 =setting_dict['windows'][0]
	window2 = setting_dict['windows'][1]
	window3 = setting_dict['windows'][2]
	stuff =setting_dict['stuff']
	possessive = setting_dict['possessive']
	generic_window = setting_dict['generic_window']
	unit = setting_dict['unit']
	
	variation = counter%3

	if variation == 0:
		correct_ans = Fraction(b,avg_c_a)
		answers = [correct_ans,1/correct_ans,avg_a_b,avg_c_a,1/avg_c_a]
		answers = sorted(answers)
		answer_key[counter] = correct_ans
		for i,answer in enumerate(answers):
			if answer in answers[:i]:
				answers[i] += Fraction(1,8)
		print(f"{counter}. If a certain {owner} {stuff} in {window1} was {a_of_b} of {possessive} {stuff} in {window2} and {possessive} {stuff} in {window3} was {c_of_a} of {possessive} {stuff} in {window1}, then the {owner} {stuff} in {window2} was how many times the average (arithmetic mean) of {possessive} {stuff} in {window1} and {window3}?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")

	if variation ==1:
		correct_ans = a_of_c
		answers = [correct_ans,1/correct_ans,avg_c_a,c_of_avg,1/c_of_avg]
		for i,answer in enumerate(answers):
			if answer in answers[:i]:
				answers[i] += Fraction(1,8)
		for i,answer in enumerate(answers):
			answers[i] = f"{answer.numerator} to {answer.denominator}"
		correct_ans = f'{a_of_c.numerator} to {a_of_c.denominator}'
		answer_key[counter] = correct_ans
		shuffle(answers)
		print(f"{counter}. If a certain {owner} {stuff} in {window3} was {c_of_b} of {possessive} {stuff} in {window2} and {possessive} {stuff} in {window1} was {a_of_avg} of the average (arithmetic mean) of {possessive} {stuff} in all three {generic_window} combined, then what was the ratio of {owner} {stuff} in {window1} to the  {owner} {possessive} {stuff} in {window3}?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")

		
	if variation ==2:
		correct_ans = c_of_tot
		answers = [correct_ans,1-correct_ans,c_of_b,c_of_avg,1-c_of_avg]
		answers = sorted(answers)
		answer_key[counter] = correct_ans
		for i,answer in enumerate(answers):
			if answer in answers[:i]:
				answers[i] += Fraction(1,8)
		print(f"{counter}. If a certain {owner} {stuff} in {window1} was {a_of_b} of {possessive} {stuff} in {window2} and {possessive} {stuff} in {window3} was {c_p_of_a}%  of {possessive} {stuff} in {window1}, then the {owner} {stuff} in {window3} was approximately what fraction of {possessive} total {stuff} in all three {generic_window}?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")


print("ANSWER KEY")
for key in answer_key:
	print(f"{key}. {answer_key[key]}")