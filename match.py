import glob
import re
import os
import jinja2
import pandas as pd
from IPython.display import HTML


list_files=glob.glob("**", recursive=True) 

new_list=[]

for file in list_files:
	head,tail = os.path.split(file)
	new_list.append(tail)
	
#print(new_list)

regex = re.compile('u301_density_6_c(\d{4}).png')

print("The files matching this format are: ")

final_list=[]
code_list = []

for file in new_list:
	match = regex.match(file)
	if match:
		final_list.append(file)	
		found = match
		print(file)
		code_list = match.groups()
		print(code_list)

final_list.reverse()



zip_list = list(zip(code_list, final_list))

print(zip_list)

for index, tuple in enumerate(zip_list):
	element_one = tuple[0]
	element_two = tuple[1]
	print(element_one,element_two)

#df =pd.DataFrame(list(zip(code_list, final_list)), columns = ['Code ID', 'Image'])

	

#result = df.to_html()
#print(result)


#------------------------------------------------------------------






#title = 'Density Table'
#outputfile = 'Density_Core.html'

#subs = jinja2.Environment(
#                loader=jinja2.FileSystemLoader('./')

#).get_template('template.html').render(title=title,mydata=table_data)
#
#with open(outputfile,'w') as f: f.write(subs)


#index_break = len(code_list)
#if len(final_list) % index_break !=0:
#	raise Exception('Not enough data.')
#staged_list = []
#current_list = []
#
#for idx in range(0,len(final_list)):
#	current_list.append(final_list[idx])
#	
#	if len(current_list) == index_break:
#		staged_list.append(current_list.copy())
#		current_list = []
#
#df = pd.DataFrame(data=staged_list, columns= code_list)
#print(df.to_html())
#---------------------------------------
