from random import sample, randint, shuffle, choice
from fractions import Fraction
from itertools import combinations

def exp(x): 
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s)) 
    return x.translate(res) 

source = "PS 205 (OG 2022)"
exponentdict = {
0:"\u2070",
1:"\u00B9",
2:"\u00b2",
3:"\u00b3",
4:"\u2074",
5:"\u2075",
6:"\u2076",
7:"\u2077",
8:"\u2078",
9:"\u2079",
10:"\u00B9\u2070",
11:"\u00B9\u00B9",
12:"\u00B9\u00b2",
13:"\u00B9\u00b3",
14:"\u00B9\u2074",
15:"\u00B9\u2075",
16:"\u00B9\u2076",
17:"\u00B9\u2077",
18:"\u00B9\u2078",
19:"\u00B9\u2079",
20:"\u00b2\u2070",
21:"\u00b2\u00B9",
22:"\u00b2\u00b2",
23:"\u00b2\u00b3",
24:"\u00b2\u2074",
25:"\u00b2\u2075",
26:"\u00b2\u2076",
27:"\u00b2\u2077",
28:"\u00b2\u2078",
29:"\u00b2\u2079",
30:"\u00b3\u2070",
31:"\u00b3\u00B9",
32:"\u00b3\u00b2",
33:"\u00b3\u00b3",
34:"\u00b3\u2074",
35:"\u00b3\u2075",
36:"\u00b3\u2076",
37:"\u00b3\u2077",
38:"\u00b3\u2078",
39:"\u00b3\u2079",
40:"\u2074\u2070",
}

question_template = f"If n=3{exponentdict[8]}-2{exponentdict[8]}, which of the following is NOT a factor of n?"
alt_question_template = "If n=3^-2^8, which of the following is NOT a factor of n?"
correct_answer = 35
incorrect_answers = [97, 65, 13, 5]

def double_factorial(x):
	if x%2 == 0:
		start = 2
	else:
		start = 3
	product = 1
	factors = []
	for i in range(start,x+1,2):
		product *= i
		factors.append(i)
	return product,factors

	return product, factors

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

def find_easy_factors(base1,base2,exp):
		factors = []
		while exp%2 ==0:
			factor1 = int(base1**(exp/2) + base2**(exp/2))
			factor2 = int(base1**(exp/2) - base2**(exp/2))
			factors.append(factor1)
			if factor2 != 1:
				factors.append(factor2)
			exp /=2
		return factors

def exponent_factorial(base,exp):
	string = ""
	total = 0
	for i in range(exp-1):
		string += f"{base}{exponentdict[exp-i]} + "
		total += base**(exp-i)
	string += f"{base}"
	total += base
	return string, total


counter = 0
answer_key = {}
for i in range(20):
	counter+=1
	variation = counter%4

	if variation ==0:
		base2 = randint(2,4)
		base1 = randint(base2+1,9)
		exp= choice([4,8,16,32])
		total = base1**exp - base2**exp
		square_factors = sorted(find_easy_factors(base1,base2,exp))
		total_factors = find_primes_to_y(total)
		easy_factors = square_factors[:4]
		more_easy_factors = []
		for item in easy_factors:
			more_easy_factors.extend(find_primes_to_y(item,100))
		easy_factors.extend(more_easy_factors)
		easy_factors = sorted(list(set(easy_factors)))
		for combo in combinations(easy_factors[:4],r=2):
			combo_factor = combo[0]*combo[1]
			if combo_factor <= 200:
				more_easy_factors.append(combo_factor)
		easy_factors.extend(more_easy_factors)
		easy_factors = sorted(list(set(easy_factors)))
		if len(easy_factors) >= 4:
			answers = sample(easy_factors[:6],k=4)
		else:
			answers = easy_factors
			answers.append(1)
			answers.append(total)
		non_factor = 2
		while len(answers)<5:
			non_factor+=1
			if non_factor not in total_factors:
				break
		correct_answer = non_factor*choice(answers)
		answers.append(correct_answer)
		answers = sorted(answers)[::-1]
		answer_key[counter] = correct_answer
		question_text = f"{counter}. If n={base1}{exponentdict[exp]}-{base2}{exponentdict[exp]}, which of the following is NOT a factor of n?"
		print(question_text)
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")
		# print(f"{total=} {easy_factors=} {total_factors=} {non_factor=} {square_factors=}")
		# print("\n\n\n")

	if variation ==1:
		factors = sample([2,2,2,2,3,3,3,3,5,7,11],k=4)
		total = 1
		for factor in factors:
			total *= factor
		exp = randint(2,6)
		factor_counts = {}
		for factor in factors:
			factor_counts[factor] = factors.count(factor)*exp
		non_factors = []
		for i in range(2,40):
			if total%i !=0:
				non_factors.append(i)
		wrong1=f'{choice(non_factors)}{exponentdict[randint(1,8)]}'
		wrong2=f'{factors[1]}{exponentdict[factor_counts[factors[1]]+1]}'
		wrong3=f'{factors[3]*factors[2]}{exponentdict[factor_counts[factors[3]]+2]}'
		wrong4=f'{factors[2]}{exponentdict[factor_counts[factors[2]]+3]}'
		correct_sample = sample(factors,k=randint(1,3))
		correct_base =1
		for factor in correct_sample:
			correct_base *= factor
		correct_ans1=f'{correct_base}{exponentdict[min(factor_counts.values())]}'
		correct_ans2_base = choice(factors)
		correct_ans2=f'{correct_ans2_base}{exponentdict[factor_counts[correct_ans2_base]]}'
		correct_ans = choice([correct_ans1,correct_ans2])
		answers = [wrong1,wrong2,wrong3,wrong4,correct_ans]
		shuffle(answers)
		answer_key[counter] = correct_ans
		question_text = f"{counter}. If n={total}{exponentdict[exp]}, and n divided by k is an integer, which of the following could be a value of k?"
		print(question_text)
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")
		# print(f"{total=} {factors=} {factor_counts=} {non_factors=}")
		# print("\n\n\n")
	if variation ==2:
		base = randint(5,20)
		exp = randint(4,15)
		# exp_fact,total = exponent_factorial(base,exp)
		exp_plus = f"{base}{exponentdict[exp]} + {base}{exponentdict[exp-1]}"
		exp_minus = f"{base}{exponentdict[exp]} - {base}{exponentdict[exp-1]}"
		total_plus = base**exp + base**(exp-1)
		total_minus = base**exp - base**(exp-1)
		setup = choice([exp_plus,exp_minus])
		if setup == exp_plus:
			total = total_plus
			known_factors = [base,base+1]
		else:
			total = total_minus
			known_factors = [base,base-1]
		extra_factors = []
		for factor in known_factors:
			extra_factors.extend(find_primes_to_y(factor,100))
		known_factors.extend(extra_factors)
		total_factors = find_primes_to_y(total)
		non_factors = []
		for i in range(2,100):
			if i not in total_factors:
				non_factors.append(i)
		wrongs = sample(non_factors[:10],k=4)
		correct_pool = [known_factors[0], known_factors[1],known_factors[0]*known_factors[1]]
		correct_pool.extend(known_factors[2:])
		correct_ans = choice(correct_pool)
		answers = [wrongs[0],wrongs[1],wrongs[2],wrongs[3],correct_ans]
		answers = sorted(answers)
		answer_key[counter] = correct_ans
		question_text = f"{counter}. If n={setup}, then n must be a multiple of which of the following?"
		print(question_text)
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")
		# print(f"{total=} {base=} {total_factors=} {known_factors=} {correct_pool=} {non_factors=}")
		# print("\n\n\n")
	if variation == 3:
		base1 = randint(8,25)
		base2 = base1-2
		setup = f'({base1}!!) - ({base2}!!)'
		factors = [base1-1,base2]
		base1_2fact,base1_2fact_factors=double_factorial(base1)
		base2_2fact,base2_2fact_factors=double_factorial(base2)
		total = base1_2fact - base2_2fact
		factors.extend(find_primes_to_y(base1-1))
		factors.extend(find_primes_to_y(base2))
		correct_pool = [base1-1, choice(base2_2fact_factors)*choice(base2_2fact_factors),(base1-1)*min(base2_2fact_factors)]
		total_factors = find_primes_to_y(total,500)
		non_factors = []
		for i in range(2,50):
			if i not in total_factors:
				non_factors.append(i)
		correct_ans = choice(correct_pool)
		wrongs = sample(non_factors,k=4)
		answers = []
		answers.extend(wrongs)
		answers.append(correct_ans)
		answers = sorted(answers)
		answer_key[counter] = correct_ans
		# One factor will be the largest prime in base2
		# Another factor will be the largest prime in base1 - 1
		question_text = f"{counter}. The double factorial of a number n, denoted by n!!, is the product of all even integers up to n for any even number n or the product of all the odd integers up to n for any odd number n.  For example, 6!! = (6)(4)(2) and 7!! = (7)(5)(3).  If x={setup}, then which of the following must be a divisor of x?"
		print(question_text)
		print(f"A. {answers[0]}\nB. {answers[1]}\nC. {answers[2]}\nD. {answers[3]}\nE. {answers[4]}")
		print("\n\n")
		# print(f"{base1=} {base2=} {factors=} {total=} {base1_2fact= }{base1_2fact_factors=} {base2_2fact=}{base2_2fact_factors=} {correct_pool=} {wrongs=}")
		# print("\n\n\n")


print("ANSWER KEY")
for key in answer_key:
	print(f"{key}. {answer_key[key]}")