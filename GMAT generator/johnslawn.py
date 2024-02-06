from fractions import Fraction
from random import randint, choice, shuffle, sample

question_template = "John's front lawn is 2/5 the size of his back lawn.  If John mows 1/2 of his front lawn and 3/4 of his back lawn, what fraction of his lawn is left unmowed?"

correct_answer = Fraction(9,28)
wrong_answers = [Fraction(19,28), Fraction(3,4), Fraction(1,4), Fraction(9,20)]


language_pool = [
{
"owner":"John",
"pronoun":"his",
"compare_term":"size",
"subsections": ["lawn","front lawn", "back lawn"],
"verb": "mows",
"neg_result": "is left unmowed",
"pos_result": "is mowed"
},

{
"owner":"Acme Co",
"pronoun":"its",
"compare_term":"size",
"subsections": ["total staff (service + warehouse)","service staff", "warehouse staff"],
"verb": "gives a raise to",
"neg_result": "were not given a raise",
"pos_result": "were given a raise"
},
{
"owner":"Suze",
"pronoun":"her",
"compare_term":"size",
"subsections": ["comic book collection","first edition comic book collection", "reissued comic book collection"],
"verb": "reads",
"neg_result": "is still unread",
"pos_result": "has she read"
},
{
"owner":"Marcus",
"pronoun":"his",
"compare_term":"amount",
"subsections": ["two total paychecks","first paycheck", "second paycheck"],
"verb": "invests",
"neg_result": "are left uninvested",
"pos_result": "has been invested"
},
{
"owner":"Alex",
"pronoun":"her",
"compare_term":"amount",
"subsections": ["total downloaded podcast queue","number of downloaded business podcasts", "sports podcasts"],
"verb": "listens to",
"neg_result": "has she not yet listened to",
"pos_result": "has she listened to"
},
{
"owner":"Team X",
"pronoun":"their",
"compare_term":"number",
"subsections": ["games","home games", "away games"],
"verb": "wins",
"neg_result": "are losses",
"pos_result": "are wins"
},
]


counter = 0
answer_key = {}
for i in range(20):
	# variation = counter%3
	variation = 2
	counter +=1
	setting_count = counter%6
	setting_dict = language_pool[setting_count]
	owner = setting_dict['owner']
	pronoun = setting_dict['pronoun']
	total = setting_dict['subsections'][0]
	group_a = setting_dict['subsections'][1]
	group_b = setting_dict['subsections'][2]
	compare_term = setting_dict['compare_term']
	verb = setting_dict['verb']
	neg_result = setting_dict["neg_result"]
	pos_result = setting_dict['pos_result']
	subset_ratio = Fraction(randint(2,5),randint(3,10)*2)
	first_subset_frac = Fraction(randint(1,5),randint(6,10))
	second_subset_frac = Fraction(randint(1,5),randint(6,10))
	first_of_tot = Fraction(subset_ratio.numerator,(subset_ratio.numerator+subset_ratio.denominator))
	second_of_tot = Fraction(subset_ratio.denominator,(subset_ratio.numerator+subset_ratio.denominator))
	first_amt = subset_ratio.numerator*first_subset_frac
	second_amt = subset_ratio.denominator*second_subset_frac
	tot = subset_ratio.numerator+subset_ratio.denominator
	total_pos = (first_amt+second_amt)/tot
	total_neg = 1-total_pos


	if variation == 0:
		
		correct_ans = total_neg
		answers = [correct_ans, total_pos, first_amt%1, 1-subset_ratio, first_subset_frac*second_subset_frac]
		for i,answer in enumerate(answers):
			if answer in answers[:i]:
				new_num = answer.numerator +1
				new_denom = answer.denominator +1
				answer = Fraction(new_num,new_denom)
		answer_key[counter] = correct_ans
		shuffle(answers)
		print(f"{counter}. {owner}'s {group_a} is {subset_ratio} the {compare_term} of {pronoun} {group_b}.  If {owner} {verb} {first_subset_frac} of {pronoun} {group_a} and {second_subset_frac} of {pronoun} {group_b}, what fraction of {pronoun} {total} {neg_result}?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")
		# print(f"{first_amt=}  {second_amt=}  {tot=}  {total_pos=}  {total_neg=}")
		# print("\n\n\n")
	if variation == 1:
		correct_ans = total_pos
		answers = [correct_ans, total_neg, first_amt%1, 1-subset_ratio, first_subset_frac*second_subset_frac]
		for i,answer in enumerate(answers):
			if answer in answers[:i]:
				new_num = answer.numerator +1
				new_denom = answer.denominator +1
				answer = Fraction(new_num,new_denom)
		answer_key[counter] = correct_ans
		shuffle(answers)
		print(f"{counter}. {owner}'s {group_a} is {first_of_tot} of {pronoun} total {total} and the rest is {pronoun} {group_b}.  If {owner} {verb} {first_subset_frac} of {pronoun} {group_a} and {second_subset_frac} of {pronoun} {group_b}, what fraction of {pronoun} {total} {pos_result}?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")
		# print(f"{first_amt=}  {second_amt=}  {tot=}  {total_pos=}  {total_neg=}")
		# print("\n\n\n")
	if variation == 2:
		correct_ans = Fraction(total_pos.numerator,total_neg.numerator)
		group_ratio = f"{subset_ratio.numerator} to {subset_ratio.denominator}"
		answers = [correct_ans, total_neg, first_amt%1, 1-subset_ratio, first_subset_frac*second_subset_frac]
		for i,answer in enumerate(answers):
			if answer in answers[:i]:
				new_num = answer.numerator +1
				new_denom = answer.denominator +1
				answer = Fraction(new_num,new_denom)
		answer_key[counter] = f"{correct_ans.numerator} to {correct_ans.denominator}"
		shuffle(answers)
		for i,answer in enumerate(answers):
			answers[i] = f"{answer.numerator} to {answer.denominator}"
		print(f"{counter}. The ratio of {owner}'s {group_a} to {pronoun} {group_b} is {group_ratio}.  If {owner} {verb} {first_subset_frac} of {pronoun} {group_a} and {second_subset_frac} of {pronoun} {group_b}, what is the ratio of {pronoun} {total} that {pos_result} to the total that {neg_result}?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")
		# print(f"{first_amt=}  {second_amt=}  {tot=}  {total_pos=}  {total_neg=}")
		# print("\n\n\n")


print("ANSWER KEY")
for key in answer_key:
	print(f"{key}. {answer_key[key]}")