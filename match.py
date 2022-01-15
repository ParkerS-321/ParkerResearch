import glob
import re
import os
import jinja2
import pandas as pd
from IPython.display import Image,HTML
import numpy as np

list_files=glob.glob("**", recursive=True) 

new_list=[]

for file in list_files:
	#head,tail = os.path.split(file)
	#new_list.append(tail)
	new_list.append(file)
#print(new_list)

regex = re.compile('(.*)/u301_density_6_c(\d{4}).png')

print("The files matching this format are: ")

image_list=[]
core_list = []

for file in new_list:
	match = regex.match(file)
	if match:
		image_list.append(file)	
		found = match
		print(file)

for file in image_list:
	match = regex.match(file)
	if match:
		core_num = match.group(2)
		core_list.append(core_num)		

print(core_list)



df = pd.DataFrame(list(zip(core_list,image_list)), columns = ['Core ID', 'Image'])

#df = pd.DataFrame(core_list,columns=['Core ID'])
#df['Image'] = image_list

def path_to_image_html(path):
	return '<img src="' + path + '" width= "120">'

pd.set_option('display.max_colwidth', None)

image_cols = ['Image']

format_dict = {}
for image_col in image_cols:
	format_dict[image_col] = path_to_image_html


df.to_html('u301_table.html',escape=False, formatters=format_dict)



#------------------------------------------------------------------






