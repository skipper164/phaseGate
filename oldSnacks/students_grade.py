numb_of_stu =int (input('how many student do you have? '))

numb_of_subj = int(input('how many subject do they offer? '))
print('saving >>>>>')
print('savd successfully')
print()
loop = 1
loop2 = 1
nest_score_list = []
total_list = []
average_list = []


while True:
	print(f'entering score for stundent {loop}: ')
	score_list = []
	total = 0
	average = 0
	

	while True:
		score = int(input(f'enter score for subject {loop2}: '))
		if(score <= 100 and score >= 0):
			score_list.append(score)
			loop2 +=1
			total += score
	
			if(loop2 > numb_of_subj): break
			
		else: print('invalid score, pls enter a score between 0 - 100')

	average = f"{total / numb_of_subj:.2f}"
	average_list.append(average)
	total_list.append(total)
	nest_score_list.append(score_list)
	print()

	
	total =0
	loop2 =1
	loop +=1
	if(loop > numb_of_stu): break 



highest_score_list = []
lowest_score_list = []
high_score = 0
lowest_score = 100
total_score = 0
total_score_list = []
average_score_list = []
pass_list = []
fail_list = []
high_stu_list = []
low_stu_list = []
high_stu = 0
low_stu = 0
pass_score =0
fail = 0

print('======================================================================')
print('STUDENT', end='	     ')
l=1
for i in range(numb_of_subj):
	print('SUB',l,end='  ')
	l+=1
print('        ''TOT', 'AVE', 'POS', sep='	  ')
print('======================================================================')

x=1
x2=1
for loop3 in range(numb_of_stu):
	print('student', x, end='	')
	for y in range(numb_of_subj):
		print(nest_score_list[loop3][y], end='    ')

		if(nest_score_list[y][loop3] > high_score): 
			high_score = nest_score_list[y][loop3]
			high_stu = x2
		if(nest_score_list[y][loop3] < lowest_score): 
			lowest_score = nest_score_list[y][loop3]
			low_stu = x2
		total_score += nest_score_list[y][loop3]
		if(nest_score_list[y][loop3] >= 50): pass_score +=1
		if(nest_score_list[y][loop3] < 50): fail +=1
		x2+=1
	
	high_stu_list.append(high_stu)
	low_stu_list.append(low_stu)
	fail_list.append(fail)
	pass_list.append(pass_score)
	average_score = f"{total_score / numb_of_stu:.2f}"
	average_score_list.append(average_score)
	total_score_list.append(total_score)
	lowest_score_list.append(lowest_score)
	highest_score_list.append(high_score)	

	print('  ',total_list[loop3], average_list[loop3], sep='	    ')

	high_stu = 0
	low_stu = 0
	pass_score =0
	fail =0
	total_score =0
	lowest_score =100
	high_score =0
	x+=1
	x2=1

print(f"""
=======================================================================
=======================================================================
""")

print(lowest_score_list)
print(total_score_list)
print(fail_list)
print(average_score_list)


z2=1
for z in range(numb_of_subj):
	print(f"""
SUBJECT SUMMARY
subject{z2}

Highest scorring student is: Student{high_stu_list[z]} scorring {highest_score_list[z]}
Lowest scoring student is: Student{low_stu_list[z]} scoring {lowest_score_list[z]}
Total score: {total_score_list[z]} 
Number of passes: {pass_list[z]}
Number of fails: {fail_list[z]}

""")
	z2+=1









