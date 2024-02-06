from fractions import Fraction
from random import randint, choice, shuffle, sample

question_template = "The ratio of roses to tulips in a bouquet is 3 to 5. If 2 roses are added to the bouquet and 6 tulips are removed, the new ratio of roses to tulips is 5 to 6. How many tulips were in the bouquet to begin with?"
wrong_answers = [15, 20, 25, 35]
right_answer = 30

language_pool = [
{
"total":"bag of marbles",
"items": ["red marbles", "blue marbles"],
"generic": "marbles"
},
{
"total":"basket of fruits",
"items": ["bananas", "oranges"],
"generic": "fruits"
},

{
"total":"high school classroom",
"items": ["sophomores", "juniors"],
"generic":"students"
},

{
"total":"dog show lineup",
"items": ["poodles", "terriers"],
"generic": "dogs"
},

{
"total":"suitcase",
"items": ["left socks", "right socks"],
"generic":"socks"
}
]

counter = 0
answer_key = {}
for i in range(20):
	counter +=1
	num1 = randint(2,5)
	denom1 = randint(num1+1,10)
	total_denom = num1+denom1
	hidden_mult = randint(2,6)
	orig_num = num1*hidden_mult
	orig_denom = denom1*hidden_mult
	orig_total = orig_num + orig_denom
	num_of_tot = Fraction(orig_num,orig_total)
	setting_choice = counter%5
	setting_dict = language_pool[setting_choice]
	total = setting_dict["total"]
	item_a = setting_dict["items"][0]
	item_b = setting_dict["items"][1]
	generic = setting_dict["generic"]
	variation = counter%3

	if variation == 0:
		add = randint(2,8)
		subtract = randint(2,5)
		new_num = orig_num + add
		new_denom = orig_denom - subtract
		new_ratio = Fraction(new_num,new_denom)
		new_numerator = new_ratio.numerator
		new_denominator = new_ratio.denominator
		answers = []
		correct_ans = orig_num
		wrong_spread = [-5,-4,-3,-2,-1,1,2,3,4,5,6]
		wrongs = sample(wrong_spread,k=4)
		answers.append(correct_ans)
		for wrong in wrongs:
			answers.append(correct_ans+num1*wrong)
		for i,answer in enumerate(answers):
			if answer <= 0:
				answers[i] +=20
		for i, answer in enumerate(answers):
			if answer in answers[:i]:
				answers[i]+=2
		answers = sorted(answers)
		answer_key[counter] = correct_ans
		print(f"{counter}. The ratio of {item_a} to {item_b} in a {total} is {num1} to {denom1}. If {add} {item_a} are added to the {total} and {subtract} {item_b} are removed, the new ratio of {item_a} to {item_b} is {new_numerator} to {new_denominator}. How many {item_a} were in the {total} to begin with?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")

	if variation == 1:
		add = randint(2,8)
		multiply = randint(2,4)
		if multiply == 2:
			mult_lang = "doubled"
		if multiply == 3:
			mult_lang = "tripled"
		if multiply == 4:
			mult_lang = "increased by 300%"
		new_num = orig_num + add
		new_denom = orig_denom*multiply
		new_ratio = Fraction(new_num,new_denom)
		new_numerator = new_ratio.numerator
		new_denominator = new_ratio.denominator
		answers = []
		correct_ans = orig_denom
		wrong_spread = [-5,-4,-3,-2,-1,1,2,3,4,5,6]
		wrongs = sample(wrong_spread,k=4)
		answers.append(correct_ans)
		for wrong in wrongs:
			answers.append(correct_ans+num1*wrong)
		for i,answer in enumerate(answers):
			if answer <= 0:
				answers[i] +=20
		for i, answer in enumerate(answers):
			if answer in answers[:i]:
				answers[i]+=2
		answers = sorted(answers)
		answer_key[counter] = correct_ans
		print(f"{counter}. In a {total}, {num_of_tot} of the {generic} are {item_a} and the rest are {item_b}. If {add} {item_a} are added to the {total} and the number of {item_b} is {mult_lang}, the new ratio of {item_a} to {item_b} is {new_numerator} to {new_denominator}. How many {item_b} were in the {total} to begin with?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")

	if variation == 2:
		add = randint(2,8)
		subtract = randint(2,5)
		new_num = orig_num + add
		new_denom = orig_denom - subtract
		new_ratio = Fraction(new_num,new_denom)
		new_numerator = new_ratio.numerator
		new_denominator = new_ratio.denominator
		answers = []
		correct_ans = f'{new_numerator} to {new_denominator}'
		wrongs = [f'{new_denominator} to {new_numerator}',f'{orig_num} to {orig_total}', f'{orig_total} to {orig_num}', f'{orig_total} to {new_denominator}']
		answers.append(correct_ans)
		answers.extend(wrongs)
		shuffle(answers)
		for i,answer in enumerate(answers):
			if answer in answers[:i]:
				answers[i] = "1 to 100"
		answer_key[counter] = correct_ans
		print(f"{counter}. The ratio of {item_a} to {item_b} in a {total} is {num1} to {denom1}. {add} {item_a} are added to the {total} and {subtract} {item_b} are removed. If there are now {new_num} {item_a} in the {total}, what is the new ratio of {item_a} to {item_b}?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")


print("ANSWER KEY")
for key in answer_key:
	print(f"{key}. {answer_key[key]}")