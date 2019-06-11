''' Python program to create email list from master. '''

import os
import csv


pathName = os.getcwd()
print(os.path.join(pathName, '/master.csv'))

file = open(os.path.join(pathName, 'master.csv'), "r")
reader = csv.reader(file, delimiter=',')

comp_dic = {}
tool_dic = {}
unsure_dic = {}

firstline = True
for row in reader:
	if firstline:
		firstline = False
		continue

	# print(row)

	# Check if email is present
	if row[10] != '':
		# Check that company name or first/last name is there
		email = row[10]
		# print(email)
		if row[0] != '' or row[2] != '' or row[3] != '':
			# Check if tool, compressor, or misc list
			if row[1] == 'True':
				if email in comp_dic:
					print('EMAIL COMP MATCH: ', email)
				comp_dic[email] = {}
				comp_dic[email]['first'] = row[2]
				comp_dic[email]['last'] = row[3]
				comp_dic[email]['company'] = row[0]
				comp_dic[email]['phone'] = row[9]
				

			elif row[1] == 'False':
				# print('Tool List')
				if email in tool_dic:
					print('EMAIL TOOL MATCH: ', email)
				tool_dic[email] = {}
				tool_dic[email]['first'] = row[2]
				tool_dic[email]['last'] = row[3]
				tool_dic[email]['company'] = row[0]
				tool_dic[email]['phone'] = row[9]
			else:
				# print('Unsure List')
				if email in unsure_dic:
					print('EMAIL UNSURE MATCH: ', row[10])
				unsure_dic[email] = {}
				unsure_dic[email]['first'] = row[2]
				unsure_dic[email]['last'] = row[3]
				unsure_dic[email]['company'] = row[0]
				unsure_dic[email]['phone'] = row[9]

# Add mailing-only CSV sheets
pathName = os.getcwd()
pathName += os.path.join(pathName, '/mailing-lists/CSV/mailing_only/')


file = open(os.path.join(pathName, 'WebsiteLeadData-COMPRESSORS.csv'), "r")
reader = csv.reader(file, delimiter=',')

firstline = True
for row in reader:
	if firstline:
		firstline = False
		continue

	email = row[4]
	if email in comp_dic:
		print('EMAIL Lead Data COMP MATCH: ', email)
		print(email, comp_dic[email])
		continue
	comp_dic[email] = {}
	hold = row[3].split()
	if len(hold) > 1:
		comp_dic[email]['last'] = hold[1].title()
	comp_dic[email]['first'] = hold[0].title()



file = open(os.path.join(pathName, 'WebsiteLeadData-TOOLS.csv'), "r")
reader = csv.reader(file, delimiter=',')

firstline = True
for row in reader:
	if firstline:
		firstline = False
		continue

	email = row[4]
	if email == '':
		break
	if email in tool_dic:
		print('EMAIL Lead Data TOOL MATCH: ', email)
		print(email, tool_dic[email])
		continue
	tool_dic[email] = {}
	hold = row[3].split()

	if len(hold) > 1:
		tool_dic[email]['last'] = hold[1].title()
	tool_dic[email]['first'] = hold[0].title()

# Get unsure from repeats
pathName = os.getcwd()

file = open(os.path.join(pathName, 'repeats.csv'), "r")
reader = csv.reader(file, delimiter=',')

counter = 0
firstline = True
for row in reader:
	if firstline:
		firstline = False
		counter += 1
		continue

	if row[0] == 'ABREO':
		break

	email = row[0]
	if email == 'pgc@teamaircenter.com':
		continue

	if email in unsure_dic:
		print('EMAIL Repeat UNSURE MATCH: ', email)
		print(email, unsure_dic[email])
		continue

	unsure_dic[email] = {}
	unsure_dic[email]['first'] = row[1]
	unsure_dic[email]['last'] = row[2]



# Write data to files
with open('mailing-comp.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

	top = ['Company Name', 'First Name', 'Last Name', 'Email', 'Phone']

	writer.writerow(top)

	for key,val in comp_dic.items():
		out_list = []
		# print('VAL:', val)
		out_list.append(val.get('company', None))
		out_list.append(val.get('first', None))
		out_list.append(val.get('last', None))
		out_list.append(key)
		out_list.append(val.get('phone', None))

		writer.writerow(out_list)

	print('Finished mailing-comp.csv')

with open('mailing-tool.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

	top = ['Company Name', 'First Name', 'Last Name', 'Email', 'Phone']

	writer.writerow(top)

	for key,val in tool_dic.items():
		out_list = []
		# print('VAL:', val)
		out_list.append(val.get('company', None))
		out_list.append(val.get('first', None))
		out_list.append(val.get('last', None))
		out_list.append(key)
		out_list.append(val.get('phone', None))

		writer.writerow(out_list)

	print('Finished mailing-tool.csv')


with open('mailing-unsure.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

	top = ['Company Name', 'First Name', 'Last Name', 'Email', 'Phone']

	writer.writerow(top)

	for key,val in unsure_dic.items():
		out_list = []
		# print('VAL:', val)
		out_list.append(val.get('company', None))
		out_list.append(val.get('first', None))
		out_list.append(val.get('last', None))
		out_list.append(key)
		out_list.append(val.get('phone', None))

		writer.writerow(out_list)

	print('Finished mailing-unsure.csv')