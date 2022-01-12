import glob
import re
import os
import jinja2
import pandas as pd
#from IPython.core.display import HTML


list_files=glob.glob("**", recursive=True) 

new_list=[]

for file in list_files:
	head,tail = os.path.split(file)
	new_list.append(tail)
	
#print(new_list)

regex = re.compile('u301_density_6_c(\d{4}).png')

print("The files matching this format are: ")

final_list=[]
for file in new_list:
	match = regex.match(file)
	if match:
		final_list.append(file)	
		found = match
		print(file)
		code_list = match.groups()
		print(code_list)


#with open("table.html", "a") as file:
#	for h,i in zip(final_list, code_list):
#		file.write("<tr><td>" + h + "</td><td>" + i "</td></tr>")

#---------------------------------------
