import time, numpy
# These dictionaries are supposed to contain the data of one month (omitted for length).
datetime = {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]}
data = {
	'IO' : {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]},
	'IP' : {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]},
	'IF' : {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]},
	'OO' : {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]},
	'OP' : {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]},
	'OF' : {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]}
}

# Stores the averages
averages = {
	'IO' : {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]},
	'IP' : {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]},
	'IF' : {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]},
	'OO' : {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]},
	'OP' : {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]},
	'OF' : {'00':[], '01':[], '02':[], '03':[], '04':[], '05':[], '06':[], '07':[], '08':[], '09':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[], '17':[], '18':[], '19':[], '20':[], '21':[], '22':[], '23':[]}

}

def get_averges(data_list, averages):
	"""Calculates average of 5 minute intervals."""
	for x in range(0,len(data_list),5):
		mean = (data_list[x]+data_list[x+1]+data_list[x+2]+data_list[x+3]+data_list[x+4])/5
		averages.append(mean)

def data_to_collection(data_list):
	"""Receives a list of data and returns a R list."""
	stringField = 'c('
	for x in range(len(data_list)):
		if x == len(data_list)-1:
			stringField += str(data_list[x]) + ');'
		else :
			stringField += str(data_list[x]) + ','
	return stringField

def print_blocks(key,value,time,name):
	"""Receives a list of data and returns a R list."""
	try:
		date = name.split(".")[0]
	except:
		date = "DATE-NOT-FOUND"

	label = key.title()

	to_print = """fecha <- 'Data from %s'
data_collection <- %s
time <- %s
title <- 'Time vs %s with Hypothesis Overlay'
type_of_data <- '%s'


""" % (date,value,time,label,label)
	return to_print

def main():
	# Tuples that will hold the lower and upperbounds
	tuples = {'IO' : [],'IP' : [],'IF' : [],'OO' : [],'OP' : [],'OF' : []}
	# Lists that will contain the simulated day
	simulated = {'IO' : [0]*288,'IP' : [0]*288,'IF' : [0]*288,'OO' : [0]*288,'OP' : [0]*288,'OF' : [0]*288}
	# Fill averages with corresponding values
	for keytype in data:
		for hour in averages[keytype]:
			get_averges(data[keytype][hour],averages[keytype][hour])

	# Fill tuples with data
	for keytype in tuples:
		for hour in averages[keytype]:
			tuples[keytype].append((numpy.mean(averages[keytype][key]),numpy.std(averages[keytype][key])))

	# Get upper and lowerbounds and create uniformly random values in their time slot
	for keytype in tuples:
		for x in range(len(tuples[keytype])):
			for i in range(12*x,12*(x+1)):
				# Lowerbound is Mean - Standard Dev
				lowerBound = tuples[keytype][x][0] - tuples[keytype][x][1] 
				# Upperbound is Mean
				upperBound = tuples[keytype][x][0]
				# Add value to simulation list
				simulated[keytype][i] = numpy.random.uniform(lowerBound,upperBound,1)[0]

	# Write to file the simulated data of all types.
	with open('simulationAll.r','w') as f:
		f.write("dates <-")
		# For the graph in R, the timestamps are used as indicators of the time.
		f.write(data_to_collection(datatime))
		f.write('\n')
		# Write the keytypes in the data
		for keytype in simulated:

			f.write('simul%s <-'%keytype)
			f.write(data_to_collection(simulated[keytype]))
			f.write('\n')


if __name__ == "__main__":
	main()
