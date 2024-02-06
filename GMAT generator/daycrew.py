from fractions import Fraction
from random import randint, choice, shuffle, sample

q_template = "At a school fundraiser, each member of the AV club sold 2/3 as many raffle tickets as each member of the chess club. If the AV club has 3/5 as many members as the chess club, what fraction of all the tickets sold by the two clubs were sold by the AV club?"
wrong_ans=[Fraction(2,5),Fraction(1,2),Fraction(3,5),Fraction(4,7)]
right_ans=[Fraction(2,7)]




language_pool = [
{
"loc":"At a school fundraiser",
"groups": ["the AV club","the chess club"],
"ctg_word": "member",
"pl_ctg_word":"members",
"prep": "of",
"action": "sold",
"prt_action": "sold",
"object_a": "raffle tickets",
"generic_groups":"clubs",
},
{
"loc":"In a certain pet store",
"groups": ["the round tank", "the square tank"],
"ctg_word": "fish",
"pl_ctg_word": "fish",
"prep":"in",
"action": "ate",
"prt_action": "eaten",
"object_a": "food pellets",
"generic_groups":"tanks of fish",
},

{
"loc":"In the 2006 academic year",
"groups": ["University A", "University B"],
"ctg_word": "enrollment officer",
"pl_ctg_word": "officers",
"prep":"in",
"action": "reviewed",
"prt_action": "reviewed",
"object_a": "applications",
"generic_groups":"universities",
},

{
"loc":"On an archeological dig",
"groups": ["Team X", "Team Y"],
"ctg_word": "worker",
"pl_ctg_word": "workers",
"prep":"from",
"action": "unearthed",
"prt_action": "unearthed",
"object_a": "fossils",
"generic_groups":"teams",
},
{
"loc":"On an exam",
"groups": ["the short response section", "the multiple choice section"],
"ctg_word": "problem",
"pl_ctg_word": "problems",
"prep":"in",
"action": "contributed",
"prt_action": "contributed",
"object_a": "points",
"generic_groups":"problem types",
},
{
"loc":"In a clothing store",
"groups": ["the children's department", "the adult department"],
"ctg_word": "transaction",
"pl_ctg_word": "sales",
"prep":"in",
"action": "cost an average of",
"prt_action": "accounted for",
"object_a": "sales dollars",
"generic_groups":"departments",
},
]

counter = 0
answer_key = {}
for i in range(20):
	counter +=1
	num1 = randint(1,5)
	denom1 = randint(num1+1,7)
	stem_frac1 = Fraction(num1,denom1)
	stem_tot_1 = num1 + denom1 
	stem_frac1_ratio = f"{stem_frac1.numerator} to {stem_frac1.denominator}"
	stem_frac1_backwards = f"{stem_frac1.denominator} to {stem_frac1.numerator}"
	num2 = randint(num1+1,8)
	denom2 = randint(num2+1,10)
	stem_frac2 = Fraction(num2,denom2)
	stem_frac2_ratio = f"{stem_frac2.numerator} to {stem_frac2.denominator}"
	stem_frac2_comp = 1-stem_frac2
	stem_tot_2 = num2 + denom2
	a_mem_from_tot = Fraction(num2,stem_tot_2)
	b_mem_from_tot = 1-a_mem_from_tot
	setting_count = counter%6
	setting_dict = language_pool[setting_count]
	loc = setting_dict['loc']
	group_a = setting_dict['groups'][0]
	group_b = setting_dict['groups'][1]
	action = setting_dict['action']
	prt_action = setting_dict['prt_action']
	prep = setting_dict["prep"]
	ctg_word = setting_dict['ctg_word']
	pl_ctg_word = setting_dict['pl_ctg_word']
	object_a = setting_dict['object_a']
	generic_groups = setting_dict['generic_groups']
	objects_in_a = (stem_frac1*stem_frac2)
	obj_in_a_ratio = f"{objects_in_a.numerator} to {objects_in_a.denominator}"
	objects_a_comp = 1-objects_in_a
	objects_a_comp_ratio = f"{objects_a_comp.numerator} to {objects_a_comp.denominator}"
	objects_a_reverse_ratio =f"{objects_a_comp.denominator} to {objects_a_comp.numerator}"
	total_objects = objects_in_a +1
	fraction_obj_a = objects_in_a / total_objects
	fraction_obj_b = 1-fraction_obj_a
	ratio_ans = fraction_obj_a/fraction_obj_b
	ratio_ans_rat = f"{ratio_ans.denominator} to {ratio_ans.numerator}"
	ratio_ans_backwards_rat = f"{ratio_ans.numerator} to {ratio_ans.denominator}"
	ratio_a_b = (1/objects_in_a)%1
	ratio_of_a_to_b = f"{ratio_a_b.numerator} to {ratio_a_b.denominator}"
	if ratio_a_b == 0:
		ratio_a_b = Fraction(randint(1,5),randint(6,10))
	
	rand_answer_num = num1-randint(0,num1-1)
	rand_answer_denom = denom1 + randint(1,3)
	variation = counter%4



	if variation == 0:
		answers = sorted([objects_in_a,objects_a_comp,Fraction(rand_answer_num,rand_answer_denom),fraction_obj_a,ratio_a_b])
		for i,answer in enumerate(answers):
			if answer in answers[:i]:
				answers[i] += Fraction(1,10)

		answer_key[counter] = fraction_obj_a
		print(f"{counter}.  {loc}, each {ctg_word} {prep} {group_a} {action} {stem_frac1} as many {object_a} as each {ctg_word} {prep} {group_b}. If {group_a} has {stem_frac2} as many {pl_ctg_word} as {group_b}, what fraction of all the {object_a} {prt_action} by the two {generic_groups} were {prt_action} by the {pl_ctg_word} {prep} {group_a}?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")

	if variation ==1:
		correct_answer = int(round(float(fraction_obj_b)*100))
		answers = [correct_answer]
		wrong_spread = [-5,-4,-3,-2,-1,1,2,3,4,5,6]
		wrongs = sample(wrong_spread,k=4)
		for wrong in wrongs:
			answers.append(correct_answer+(randint(5,10)*wrong))
		for i,answer in enumerate(answers):
			if answer <= 0:
				answers[i] = abs(answer)
			if answer >= 100:
				answers[i] = answer%100
		for i, answer in enumerate(answers):
			if answer in answers[:i]:
				answers[i]+=5
		answers = sorted(answers)
		answer_key[counter] = f"{correct_answer}%"
		print(f"{counter}.  {loc}, each {ctg_word} {prep} {group_a} {action} {stem_frac1} as many {object_a} as each {ctg_word} {prep} {group_b}. If {group_a} has {stem_frac2} as many {pl_ctg_word} as {group_b}, approximately what percent of all the {object_a} {prt_action} by the two {generic_groups} were {prt_action} by the {pl_ctg_word} {prep} {group_b}?")
		print(f"A. {answers[0]}%\nB. {answers[1]}%\nC. {answers[2]}%\nD. {answers[3]}%\nE. {answers[4]}%")
		print("\n\n")

	if variation == 2:
		answers = ([obj_in_a_ratio,objects_a_comp_ratio,ratio_ans_backwards_rat,stem_frac1_ratio,ratio_ans_rat])
		answer_key[counter] = ratio_ans_rat
		for i, answer in enumerate(answers):
			if answer in answers[:i]:
				answers[i] = "1 to 1"
		shuffle(answers)
		print(f"{counter}.  {loc}, each {ctg_word} {prep} {group_a} {action} {stem_frac1} as many {object_a} as each {ctg_word} {prep} {group_b}. If {group_a} made up {a_mem_from_tot} of the total {pl_ctg_word} and {group_b} made up the rest, what is the ratio of {object_a} {prt_action} by {group_b} to the {object_a} {prt_action} by {group_a}?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")

	if variation == 3:
		answer_key[counter] = stem_frac1_ratio
		answers = ([stem_frac1_ratio,stem_frac2_ratio,ratio_ans_backwards_rat,ratio_ans_rat,stem_frac1_backwards])
		for i, answer in enumerate(answers):
			if answer in answers[:i]:
				answers[i] = "1 to 1"
		shuffle(answers)
		print(f"{counter}. {loc}, there were two {generic_groups}: {group_a} had {stem_frac2} as many {pl_ctg_word} as {group_b}. {fraction_obj_a} of the total {object_a} {prt_action} by the two {generic_groups} were {prt_action} by the {pl_ctg_word} {prep} {group_a}. What is the ratio of {object_a} {prt_action} per {ctg_word} {prep} {group_a} to the {object_a} {prt_action} per {ctg_word} {prep} {group_b}?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")





print("ANSWER KEY")
for key in answer_key:
	print(f"{key}. {answer_key[key]}")