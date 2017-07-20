import time, numpy

# The data of the month of september (omitted for length)
month_io = []
month_if = []
month_ip = []
month_oo = []
month_op = []
month_of = []

# The unix timestamps
month_time = []

# Dates to store sizes
dates = {'00' : [],'01' : [],'02' : [],'03' : [],'04' : [],'05' : [],'06' : [],'07' : [],'08' : [],'09' : [],'10' : [],'11' : [],'12' : [],'13' : [],'14' : [],'15' : [],'16' : [],'17' : [],'18' : [],'19' : [],'20' : [],'21' : [],'22' : [],'23' : []}
dataIO = {'00' : [],'01' : [],'02' : [],'03' : [],'04' : [],'05' : [],'06' : [],'07' : [],'08' : [],'09' : [],'10' : [],'11' : [],'12' : [],'13' : [],'14' : [],'15' : [],'16' : [],'17' : [],'18' : [],'19' : [],'20' : [],'21' : [],'22' : [],'23' : []}
dataIF = {'00' : [],'01' : [],'02' : [],'03' : [],'04' : [],'05' : [],'06' : [],'07' : [],'08' : [],'09' : [],'10' : [],'11' : [],'12' : [],'13' : [],'14' : [],'15' : [],'16' : [],'17' : [],'18' : [],'19' : [],'20' : [],'21' : [],'22' : [],'23' : []}
dataIP = {'00' : [],'01' : [],'02' : [],'03' : [],'04' : [],'05' : [],'06' : [],'07' : [],'08' : [],'09' : [],'10' : [],'11' : [],'12' : [],'13' : [],'14' : [],'15' : [],'16' : [],'17' : [],'18' : [],'19' : [],'20' : [],'21' : [],'22' : [],'23' : []}
dataOO = {'00' : [],'01' : [],'02' : [],'03' : [],'04' : [],'05' : [],'06' : [],'07' : [],'08' : [],'09' : [],'10' : [],'11' : [],'12' : [],'13' : [],'14' : [],'15' : [],'16' : [],'17' : [],'18' : [],'19' : [],'20' : [],'21' : [],'22' : [],'23' : []}
dataOP = {'00' : [],'01' : [],'02' : [],'03' : [],'04' : [],'05' : [],'06' : [],'07' : [],'08' : [],'09' : [],'10' : [],'11' : [],'12' : [],'13' : [],'14' : [],'15' : [],'16' : [],'17' : [],'18' : [],'19' : [],'20' : [],'21' : [],'22' : [],'23' : []}
dataOF = {'00' : [],'01' : [],'02' : [],'03' : [],'04' : [],'05' : [],'06' : [],'07' : [],'08' : [],'09' : [],'10' : [],'11' : [],'12' : [],'13' : [],'14' : [],'15' : [],'16' : [],'17' : [],'18' : [],'19' : [],'20' : [],'21' : [],'22' : [],'23' : []}


##############################BY DIFF DAYS IN A MONTH
days_averages = {"Sunday": ([0]*288, 0, [0]*288), "Monday": ([0]*288, 0, [0]*288), "Tuesday": ([0]*288, 0, [0]*288), "Wednesday": ([0]*288, 0, [0]*288), "Thursday": ([0]*288, 0, [0]*288), "Friday": ([0]*288, 0, [0]*288), "Saturday": ([0]*288, 0, [0]*288)}

# Invoke on every key
def data_to_collection(data_list):
	stringField = 'c('
	for x in range(len(data_list)):
		if x == len(data_list)-1:
			stringField += str(data_list[x]) + ');'
		else :
			stringField += str(data_list[x]) + ','
	return stringField

def giveMeAKey(weekdayNum):
	return {
		'0': "Sunday",
		'1': "Monday",
		'2': "Tuesday",
		'3': "Wednesday",
		'4': "Thursday",
		'5': "Friday",
		'6': "Saturday",
	}[weekdayNum]

def data_original(data_list):
	stringField = 'c('
	for x in range(len(data_list)):
		if x == len(data_list)-1:
			stringField += str(data_list[x]) + ');'
		else :
			stringField += str(data_list[x]) + ','
	return stringField

def retrieve_data():
	DAYS = len(month_io)/288
	the_weekday = ''
	the_weekday_num = 0
	the_weekday_stamp = 0
	for weekday in range(0, 7):
		for specific_hour in range(288):
			tmp_total = 0
			weekday_cntr = 0
			for specific_day in range(weekday, DAYS, 7):
				temp_data = month_io[specific_hour  +  288 * specific_day]
				tmp_total += temp_data
				the_weekday_stamp = month_time[specific_hour + 288 * specific_day]
				the_weekday_num = time.strftime("%w", time.localtime(the_weekday_stamp))
				weekday_cntr += 1
				########### Acumulation of data here ########
				dataIO[time.strftime("%H", time.localtime(the_weekday_stamp))].append(month_io[specific_hour  +  288 * specific_day])
				dataIP[time.strftime("%H", time.localtime(the_weekday_stamp))].append(month_ip[specific_hour  +  288 * specific_day])
				dataIF[time.strftime("%H", time.localtime(the_weekday_stamp))].append(month_if[specific_hour  +  288 * specific_day])
				dataOO[time.strftime("%H", time.localtime(the_weekday_stamp))].append(month_oo[specific_hour  +  288 * specific_day])
				dataOP[time.strftime("%H", time.localtime(the_weekday_stamp))].append(month_op[specific_hour  +  288 * specific_day])
				dataOF[time.strftime("%H", time.localtime(the_weekday_stamp))].append(month_of[specific_hour  +  288 * specific_day])

				dates[time.strftime("%H", time.localtime(the_weekday_stamp))].append(the_weekday_stamp)
				########### Acumulation of data ends here #####
			the_weekday = giveMeAKey(the_weekday_num)
			days_averages[the_weekday][0][specific_hour] = tmp_total
			days_averages[the_weekday] = (days_averages[the_weekday][0], weekday_cntr, days_averages[the_weekday][2])

for key in days_averages:
	for i in range(288):
		days_averages[key][2][i] = days_averages[key][0][i] / days_averages[key][1]

# Write to values to outputfile
with open('simulation2.py','w') as s:
	s.write('datatime = {')
	for key in dates:
		s.write("'%s': ["%key)
		for x in range(len(dates[key])):
			if x == len(dates[key]) -1:
				s.write("%d" % dates[key][x])
			else:
				s.write("%d," % dates[key][x])
		s.write("],\n")
	s.write("}")

	s.write('dataIO = {')
	for key in dataIO:
		s.write("'%s': ["%key)
		for x in range(len(dataIO[key])):
			if x == len(dataIO[key]) -1:
				s.write("%d" % dataIO[key][x])
			else:
				s.write("%d," % dataIO[key][x])
		s.write("],\n")
	s.write("}")

	s.write('dataIP = {')
	for key in dataIP:
		s.write("'%s': ["%key)
		for x in range(len(dataIP[key])):
			if x == len(dataIP[key]) -1:
				s.write("%d" % dataIP[key][x])
			else:
				s.write("%d," % dataIP[key][x])
		s.write("],\n")
	s.write("}")

	s.write('dataIF = {')
	for key in dataIF:
		s.write("'%s': ["%key)
		for x in range(len(dataIF[key])):
			if x == len(dataIF[key]) -1:
				s.write("%d" % dataIF[key][x])
			else:
				s.write("%d," % dataIF[key][x])
		s.write("],\n")
	s.write("}")

	s.write('dataOO = {')
	for key in dataOO:
		s.write("'%s': ["%key)
		for x in range(len(dataOO[key])):
			if x == len(dataOO[key]) -1:
				s.write("%d" % dataOO[key][x])
			else:
				s.write("%d," % dataOO[key][x])
		s.write("],\n")
	s.write("}")

	s.write('dataOP = {')
	for key in dataOP:
		s.write("'%s': ["%key)
		for x in range(len(dataOP[key])):
			if x == len(dataOP[key]) -1:
				s.write("%d" % dataOP[key][x])
			else:
				s.write("%d," % dataOP[key][x])
		s.write("],\n")
	s.write("}")
	s.write('dataOF = {')
	for key in dataOF:
		s.write("'%s': ["%key)
		for x in range(len(dataOF[key])):
			if x == len(dataOF[key]) -1:
				s.write("%d" % dataOF[key][x])
			else:
				s.write("%d," % dataOF[key][x])
		s.write("],\n")
	s.write("}")
