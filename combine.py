'''Python program to combine CVS mailing lists into single master one'''

import os
import csv


def check_exists(name_in, dic):
	'''Checks if company name already in dic.'''
	if name_in in dic:
		print(name_in, ' Exists!!!')
		return True

	return False

	

mast_dict = {}
repeat_dict = {}

pathName = os.getcwd()
pathName += os.path.join(pathName, '/mailing-lists/CSV/')
print('pathName: ', pathName)

print('Start combining')
print('*******************')


for filename in os.listdir(pathName):
	print(filename)
	# Open file and read it in
	file = open(os.path.join(pathName, filename), "r")
	reader = csv.reader(file, delimiter=',')

	if filename == 'AC-MI-Mailing-List.csv':
		# print('u found it')
		firstline = True
		for row in reader:
			if firstline:
				firstline = False
				continue

			# Check if company name already exists
			c_name = row[3]
			if not check_exists(c_name, mast_dict):
				mast_dict[c_name] = {}

				# TODO: Makes names not uppercase
				# fullname = row[0] + '' + row[1]
				# mast_dict[c_name]['contact'] = fullname
				mast_dict[c_name]['firstname'] = row[0].title()
				mast_dict[c_name]['lastname'] = row[1].title()
				
				mast_dict[c_name]['title'] = row[2]
				mast_dict[c_name]['address'] = row[4]
				mast_dict[c_name]['city'] = row[5]
				mast_dict[c_name]['state'] = row[7]
				mast_dict[c_name]['zip'] = row[8]
				mast_dict[c_name]['phone'] = row[9]
				mast_dict[c_name]['url'] = row[10]
				mast_dict[c_name]['description'] = row[11]
				mast_dict[c_name]['employees'] = row[12]
			else:
				# key = phone, val = []
				if c_name not in repeat_dict:
					repeat_dict[c_name] = []
				repeat_dict[c_name].append(row)


	elif filename == 'Kaeser-Jan18toApril19.csv':
		firstline = True
		for row in reader:
			if firstline:
				firstline = False
				continue

			# Check if company name already exists
			# Note: Need to remove extra space after company name
			c_name = row[0]
			c_name = c_name[:-1]
			if not check_exists(c_name, mast_dict):
				mast_dict[c_name] = {}

				# Split into first/last names
				hold = row[7].split()
				# print('hold:', hold)
				mast_dict[c_name]['firstname'] = hold[0].title()
				mast_dict[c_name]['lastname'] = hold[1].title()

				mast_dict[c_name]['title'] = row[11]
				# mast_dict[c_name]['address'] = row[4]
				mast_dict[c_name]['city'] = row[3]
				mast_dict[c_name]['state'] = row[4]
				mast_dict[c_name]['zip'] = row[5]
				mast_dict[c_name]['phone'] = row[8]
				mast_dict[c_name]['email'] = row[9]
				# mast_dict[c_name]['url'] = row[10]
				mast_dict[c_name]['description'] = row[6]
				# mast_dict[c_name]['employees'] = row[12]
			else:
				if c_name not in repeat_dict:
					repeat_dict[c_name] = []
				repeat_dict[c_name].append(row)

	else:
		firstline = True
		for row in reader:
			if firstline:
				firstline = False
				continue

			# Check if company name already exists
			c_name = row[0]
			if not check_exists(c_name, mast_dict):
				mast_dict[c_name] = {}

				mast_dict[c_name]['address'] = row[1]
				mast_dict[c_name]['city'] = row[2]
				mast_dict[c_name]['state'] = row[3]
				mast_dict[c_name]['zip'] = row[4]
				mast_dict[c_name]['phone'] = row[5]
				# mast_dict[c_name]['email'] = row[9]
				mast_dict[c_name]['url'] = row[6]
				mast_dict[c_name]['description'] = row[11]
				mast_dict[c_name]['employees'] = row[8]
				mast_dict[c_name]['parent'] = row[10]
			else:
				if c_name not in repeat_dict:
					repeat_dict[c_name] = []
				repeat_dict[c_name].append(row)


# Write mast_dict to CSV file
with open('master.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

	top = ['Company Name', 'First Name', 'Last Name', 'Title', 
			'Address', 'City', 'Zip Code', 'State',
			'Phone', 'URL', 'Description', 'Employees', 'Parent Company']

	writer.writerow(top)

	for key,val in mast_dict.items():
		out_list = []
		# print('VAL:', val)
		out_list.append(key)
		out_list.append(val.get('firstname', None))
		out_list.append(val.get('lastname', None))
		out_list.append(val.get('title',None))
		out_list.append(val.get('address',None))
		out_list.append(val.get('city',None))
		out_list.append(val.get('zip',None))
		out_list.append(val.get('state', None))
		out_list.append(val.get('phone', None))
		out_list.append(val.get('url', None))
		out_list.append(val.get('description', None))
		out_list.append(val.get('employees', None))
		out_list.append(val.get('parent', None))

		writer.writerow(out_list)

# Write Repeats to CSV file
with open('repeats.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

	# top = ['Company Name', 'First Name', 'Last Name', 'Title', 
	# 		'Address', 'City', 'Zip Code', 'State',
	# 		'Phone', 'URL', 'Description', 'Employees', 'Parent Company']

	# writer.writerow(top)

	for key, val in repeat_dict.items():
		# print(key, val)
		writer.writerow([key])

		for entry in val:
			writer.writerow(entry)
		



# print(mast_dict['826 Michigan'])
# print(mast_dict['Aria Energy'])
# print(mast_dict['General Motors Company'])
# print(repeat_dict)



