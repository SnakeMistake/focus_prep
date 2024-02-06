from random import randint, choice, shuffle, sample


question_template = "At his regular hourly rate, Don had estimated the labor cost of a repair job as $336 and he was paid that amount. However, the job took 4 hours longer than he had estimated and, consequently, he earned $2 per hour less than his regular hourly rate. What was the time Don had estimated for the job, in hours?"
correct_answer = 24
incorrect_answers = [28,16,14,12]



counter = 0
answer_key = {}
for i in range(20):
	counter +=1
	factor_pool = [2,2,2,2,2,3,3,3,3,3,5,5,5,7,7]
	rate_pool = sample(factor_pool,k=randint(1,2))
	rate = 1
	for item in rate_pool:
		rate*=item
	unit_pool = sample(factor_pool,k=2)
	units =1
	for item in unit_pool:
		units*=item
	total = rate*units
	new_rate = rate
	while new_rate == rate:
		new_rate_factors = rate_pool
		new_rate_factors.extend(unit_pool)
		new_rate_pool = sample(new_rate_factors,k=(randint(1,2)))
		new_rate = 1
		for item in new_rate_pool:
			new_rate*=item
	new_units = int(total/new_rate)
	unit_diff = new_units-units
	rate_diff = new_rate-rate


	




	variation = counter%2

	if variation == 0:
		correct_ans = units
		answers = [correct_ans]
		unit_pool.extend([2,2,3,3,5])
		for i in range(4):
			wrong = correct_ans
			while wrong in answers:
				wrong = 1
				wrong_factors = sample(unit_pool,k=randint(2,3))
				for item in wrong_factors:
					wrong*=item
			answers.append(wrong)
		if rate_diff <0:
			rate_diff_lang ="less"
			unit_diff_lang = "longer"
		else:
			rate_diff_lang ="more"
			unit_diff_lang = "fewer"
		unit_diff = abs(unit_diff)
		rate_diff = abs(rate_diff)
		answers = sorted(answers)
		answer_key[counter] = correct_ans


		print(f"{counter}. At his regular hourly rate, Steve estimated the labor cost of a construction job as ${total}. However, the job took {unit_diff} hours {unit_diff_lang} than he had estimated and, consequently, he earned ${rate_diff} per hour {rate_diff_lang} than his normal rate per hour. What was the time Steve had estimated for the job, in hours?")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")


		# print(f"{rate=}  {units=}  {total=}  {new_rate=}  {new_units=} {unit_diff=} {rate_diff=}")
		print("\n\n\n")
	if variation == 1:
		correct_ans = rate
		answers = [correct_ans]
		rate_pool.extend([2,2,3,3,5])
		for i in range(4):
			wrong = correct_ans
			while wrong in answers:
				wrong = 1
				wrong_factors = sample(rate_pool,k=randint(1,3))
				for item in wrong_factors:
					wrong*=item
			answers.append(wrong)
		if rate_diff <0:
			price_diff ="less"
			price_explanation= "He negotiated a better price from the distributor in a bulk order"
			stuff_diff = "more"
		else:
			price_diff ="more"
			price_explanation= "He unfortunately had to pay a premium for a rush order"
			stuff_diff = "fewer"
		unit_diff = abs(unit_diff)
		rate_diff = abs(rate_diff)
		answers = sorted(answers)
		answer_key[counter] = correct_ans


		print(f"{counter}. Dennis budgeted to spend ${total} for the purchase of bulk crates of candy at a retailer. {price_explanation} and bought {unit_diff} {stuff_diff} crates than originally planned. As a result, he paid ${rate_diff} per crate {price_diff} than he would have at the original retailer. What was the original price per crate Dennis budgeted to spend??")
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")


		# print(f"{rate=}  {units=}  {total=}  {new_rate=}  {new_units=} {unit_diff=} {rate_diff=}")
		print("\n\n")

print("ANSWER KEY")
for key in answer_key:
	print(f"{key}. {answer_key[key]}")