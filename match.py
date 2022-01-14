import glob
import re
import os
import jinja2
import pandas as pd
from IPython.display import HTML
import numpy as np

list_files=glob.glob("**", recursive=True) 

new_list=[]

for file in list_files:
	head,tail = os.path.split(file)
	new_list.append(tail)
	
#print(new_list)

regex = re.compile('u301_density_6_c(\d{4}).png')

print("The files matching this format are: ")

final_list=[]
core_list = []

for file in new_list:
	match = regex.match(file)
	if match:
		final_list.append(file)	
		found = match
		print(file)
		#core_num = match.groups()
	 	#core_list.append(core_num)
		#print(core_list)

for file in final_list:
	match = regex.match(file)
	if match:
		core_num = match.groups()
		core_list.append(core_num)




df = pd.DataFrame(core_list,columns=['Core ID'])
df['Image'] = final_list

def path_to_image_html(path):
	return '<img src "'+ path + '"width= "60">'

pd.set_option('display.max_colwidth', None)

image_cols = ['Image']

format_dict = {}
for image_col in image_cols:
	format_dict[image_col] = path_to_image_html


df.to_html('u301_table.html',escape=False, formatters=format_dict)


#df = pd.DataFrame(list(zip(core_list,final_list)),
#	columns=['Core ID', 'Image'])

#result = df.to_html('u301_table.html')
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
