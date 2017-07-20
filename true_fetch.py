#!/usr/bin/env python
from dataquery import DataQuery
from sys import argv, exit
import time, datetime, pickle, os

def get_data(dq,start,end):
	"""Connects to database and queries for given start and end dates."""
	data = {'input octet': [], 'output octet': [], 'input packet': [], 'output packet': [],'input flows':[], 'output flows':[], 'time': []}
	
	for item in dq.GetDataRange(3,start,end):
		data['input octet'].append(item[0])
		data['output octet'].append(item[1])
		data['input packet'].append(item[2])
		data['output packet'].append(item[3])
		data['input flows'].append(item[4])
		data['output flows'].append(item[5])
		data['time'].append(item[6])
	return data

# Verify arguments
def verify_arguments(argv):
	if len(argv) < 4:
		print "Usage: true_fetch.py <output> <start-date> <end-date>"
		exit()

	else:
		out = argv[1]
		if os.path.isfile(out):
			val = raw_input("Warning! File %s already exists, overwrite? [Y/N]: "%argv[2])
			if val.upper() == 'Y':
				return argv[1]
			else:
				while os.path.isfile(out):
					out = raw_input("File %s still exists, enter new name: "%out)			
		return out

def get_dates(start,end):
	try:
		newstart = time.mktime(datetime.datetime.strptime(start, "%d/%m/%Y").timetuple())
		newend = time.mktime(datetime.datetime.strptime(end, "%d/%m/%Y").timetuple())
		return (newstart,newend)
	except:
		print "The entered dates are not valid."
		exit()
# ----- Functions from previous script-----
# Invoke on every key
def data_to_collection(data_list):
	"""Receives a list of data and returns a R list."""
	stringField = 'c('
	for x in range(len(data_list)):
		if x == len(data_list)-1:
			stringField += str(data_list[x]) + ');'
		else :
			stringField += str(data_list[x]) + ','
	return stringField

# Print the data in blocks
def print_blocks(key,value,time,name):
	"""Returns string that contains values to be written in an R file."""
	try:
		date = name.split(".")[0]
	except:
		date = "DATE-NOT-FOUND"

	label = key.title()

	to_print = """fecha <- 'Data from %s'
%s_collection <- %s
time <- %s
title <- 'Time vs %s with Hypothesis Overlay'
type_of_data <- '%s'


""" % (date,key,value,time,label,label)
	return to_print

def main(argv):
	outfile = verify_arguments(argv)
	filename = argv[1]
	start,end = get_dates(str(argv[2]),str(argv[3]))
	dq = DataQuery()
	data = get_data(dq,start,end)
	# Write to file the contents
	with open(outfile,'wb') as fopen:
		time = data_to_collection(data['time'])
		keys = {'time': time}
		for key in data:
			if key not in keys:
				keys[key] = data_to_collection(data[key])
				to_print = print_blocks(key, keys[key],time,outfile)
				fopen.write(to_print)

if __name__ == '__main__':
	main(argv)