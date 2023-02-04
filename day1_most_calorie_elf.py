f = open('input1.txt','r')
lista = f.read().rsplit('\n')
total_cal_list = []
total_cal_sum = 0
for x in lista:
	if x.isdigit():
		total_cal_sum = total_cal_sum + int(x)
	else:
		total_cal_list.append(total_cal_sum)
		total_cal_sum = 0
f.close()
print(max(total_cal_list))
