import glob
import re
import os
import jinja2
import pandas as pd
from IPython.display import Image,HTML
import numpy as np
from flask import Flask,request,render_template,session,redirect,send_from_directory
from itertools import cycle
import random



list_files=glob.glob("**", recursive=True)                      # create list of all files

new_list=[]

for file in list_files:
        #head,tail = os.path.split(file)
        #new_list.append(tail)
        new_list.append(file)
#print(new_list)
u301_total_list=[]
for file in list_files:
        if 'u301' in file:
                u301_total_list.append(file)


#--------------------- THE NEXT LARGE CHUNK OF CODE IS GATHERING THE DATA FOR EACH SEPARATE SIMULATION---------------------------------#



#-------------------------------------------------------------- density_time tables ----------------------------------------------#
#---U301---#
regex = re.compile('(.*)/u301_density_6_c(\d{4}).png')

u301_image_list=[]
u301_core_list = []

for file in new_list:
        match = regex.match(file)
        if match:
                u301_image_list.append(file)                    
                found = match
                #print(file)

for file in u301_image_list:                                    
        match = regex.match(file)
        if match:
                core_num_u301 = match.group(2)
                u301_core_list.append(core_num_u301)

#---U302---#

regex1 = re.compile('(.*)/u302_density_6_c(\d{4}).png')

u302_image_list = []
u302_core_list = []

for file in new_list:
        match = regex1.match(file)
        if match:
                u302_image_list.append(file)
                found = match


for file in u302_image_list:
        match = regex1.match(file)
        if match:
                core_num_u302 = match.group(2)
                u302_core_list.append(core_num_u302)

#---U303
regexu303_1 = re.compile('(.*)/u303_density_6_c(\d{4}).png')
u303_image_list = []
u303_core_list = []

for file in new_list:
        match = regexu303_1.match(file)
        if match:
                u303_image_list.append(file)
                found = match
for file in u303_image_list:
        match = regexu303_1.match(file)
        if match:
                core_num_u303 = match.group(2)
                u303_core_list.append(core_num_u303)


#---------------------------------------------------Proj_x_density tables-----------------------------#
#u301
regex3 = re.compile('(.*)/u301_peak_p(\d{4})_34_Projection_x_density.png')

u301_proj_x_image_list = []
u301__proj_x_peakid_list = []

for file in new_list:
        match = regex3.match(file)
        if match:
                u301_proj_x_image_list.append(file)
                found = match

for file in u301_proj_x_image_list:
        match = regex3.match(file)
        if match:
                u301_peakid_num = match.group(2)
                u301__proj_x_peakid_list.append(u301_peakid_num)

#u302
regex_u302_1 = re.compile('(.*)/u302_peak_p(\d{4})_34_Projection_x_density.png')

u302_proj_x_image_list = []
u302_proj_x_peakid_list = []

for file in new_list:
        match = regex_u302_1.match(file)
        if match:
                u302_proj_x_image_list.append(file)
                found = match
for file in u302_proj_x_image_list:
        match = regex_u302_1.match(file)
        if match:
                u302_proj_x_peakid = match.group(2)
                u302_proj_x_peakid_list.append(u302_proj_x_peakid)

#---U303

regexu303_2 = re.compile('(.*)/u303_peak_p(\d{4})_34_Projection_x_density.png')

u303_proj_x_image_list = []
u303_proj_x_peakid_list = []

for file in new_list:
        match = regexu303_2.match(file)
        if match:
                u303_proj_x_image_list.append(file)
                found = match
for file in u303_proj_x_image_list:
        match = regexu303_2.match(file)
        if match:
                u303_proj_x_peakid = match.group(2)
                u303_proj_x_peakid_list.append(u303_proj_x_peakid)



#---------------------------------------------------- Peak Split All Tables--------------------------------#

#----U301----
regex4 = re.compile('(.*)/u301_peak_split_all_excluded_c(\d{4})_c(\d{4})_Projection_x_density.png')
regex5 = re.compile('(.*)/u301_peak_split_all_excluded_c(\d{4})_c(\d{4})_Projection_y_density.png')
u301_peak_split_proj_x_list = []
u301_peak_split_proj_y_list = []
excluded_core_list_x =[]
excluded_core_list_y = []

for file in new_list:
        match=regex4.match(file)
        match1=regex5.match(file)
        if match:
                u301_peak_split_proj_x_list.append(file)
                found = match
        if match1:
                u301_peak_split_proj_y_list.append(file)
                found=match1
        
for file in u301_peak_split_proj_x_list:
        match = regex4.match(file)
        if match: 
                excluded_core_num1x = match.group(2,3)
                excluded_core_list_x.append(excluded_core_num1x)
for file in u301_peak_split_proj_y_list:
        match = regex5.match(file)
        if match:
                excluded_core_num1y = match.group(2,3)
                excluded_core_list_y.append(excluded_core_num1y)


#----U302----
regex_u302_2 = re.compile('(.*)/u302_peak_split_all_excluded_c(\d{4})_c(\d{4})_Projection_x_density.png')
regex_u302_3 = re.compile('(.*)/u302_peak_split_all_excluded_c(\d{4})_c(\d{4})_Projection_y_density.png')

u302_peak_split_proj_x_list = []
u302_peak_split_proj_y_list =[]
excluded_core_list1_x = []
excluded_core_list1_y = []
for file in new_list:
        match = regex_u302_2.match(file)
        match1= regex_u302_3.match(file)
        if match:
                u302_peak_split_proj_x_list.append(file)
                found = match
        if match1:
                u302_peak_split_proj_y_list.append(file)
                found=match1

for file in u302_peak_split_proj_x_list:
        match=regex_u302_2.match(file)
        if match:
                excluded_core_num2x = match.group(2,3)
                excluded_core_list1_x.append(excluded_core_num2x)
for file in u302_peak_split_proj_y_list:
        match = regex_u302_3.match(file)
        if match:
                excluded_core_num_2y = match.group(2,3)
                excluded_core_list1_y.append(excluded_core_num_2y)



#----U303
regexu303_3 = re.compile('(.*)/u303_peak_split_all_excluded_c(\d{4})_c(\d{4})_Projection_x_density.png')
regexu303_4 = re.compile('(.*)/u303_peak_split_all_excluded_c(\d{4})_c(\d{4})_Projection_y_density.png')

u303_peak_split_proj_x_list = []
u303_peak_split_proj_y_list = []
excluded_core_list2_x = []
excluded_core_list2_y = []

for file in new_list:
        match = regexu303_3.match(file)
        match1 = regexu303_4.match(file)
        if match: 
                u303_peak_split_proj_x_list.append(file)
                found = match
        if match1:
                u303_peak_split_proj_y_list.append(file)
                found=match1

for file in u303_peak_split_proj_x_list:
        match = regexu303_3.match(file)
        if match:
                excluded_core_num2x = match.group(2,3)
                excluded_core_list2_x.append(excluded_core_num2x)
for file in u303_peak_split_proj_y_list:
        match = regexu303_4.match(file)
        if match:
                excldued_core_num2y = match.group(2,3)
                excluded_core_list2_y.append(excldued_core_num2y)


#------------------------------------------------- Peak_split_corestack table --------------------------------#
#---U301
regex6 = re.compile('(.*)/u301_peak_split_corestack_c(\d{4})_c(\d{4})_Projection_x_density.png')
regex7 = re.compile('(.*)/u301_peak_split_corestack_c(\d{4})_c(\d{4})_Projection_y_density.png')
u301_peak_split_corestack_x_list = []
u301_peak_split_corestack_y_list = []
corestack_list_x = []
corestack_list_y = []
for file in new_list:
        match = regex6.match(file)
        match1 = regex7.match(file)
        if match:
                u301_peak_split_corestack_x_list.append(file)
                found=match
        if match1:
                u301_peak_split_corestack_y_list.append(file)
                found=match1

for file in u301_peak_split_corestack_x_list:
        match=regex6.match(file)
        if match:
                corestack_numx = match.group(2,3)
                corestack_list_x.append(corestack_numx)
for file in u301_peak_split_corestack_y_list:
        match = regex7.match(file)
        if match:
                corestack_numy = match.group(2,3)
                corestack_list_y.append(corestack_numy)
        
#---U302
regexu302_4 = re.compile('(.*)/u302_peak_split_corestack_c(\d{4})_c(\d{4})_Projection_x_density.png')
regexu302_5 = re.compile('(.*)/u302_peak_split_corestack_c(\d{4})_c(\d{4})_Projection_y_density.png')
u302_peak_split_corestack_x_list = []
u302_peak_split_corestack_y_list = []
core_stack_list1_x = [ ]
core_stack_list1_y = []
for file in new_list:
        match = regexu302_4.match(file)
        match1 = regexu302_5.match(file)
        if match:
                u302_peak_split_corestack_x_list.append(file)
                found=match
        if match1:
                u302_peak_split_corestack_y_list.append(file)
                found=match1

for file in u302_peak_split_corestack_x_list:
        match = regexu302_4.match(file)
        if match:
                corestack_num1x = match.group(2,3)
                core_stack_list1_x.append(corestack_num1x)
for file in u302_peak_split_corestack_y_list:
        match = regexu302_5.match(file)
        if match:
                corestack_num1y = match.group(2,3)
                core_stack_list1_y.append(corestack_num1y)

#----U303
regexu303_5 = re.compile('(.*)/u303_peak_split_corestack_c(\d{4})_c(\d{4})_Projection_x_density.png')
regexu303_6 = re.compile('(.*)/u303_peak_split_corestack_c(\d{4})_c(\d{4})_Projection_y_density.png')
u303_peak_split_corestack_x_list = []
u303_peak_split_corestack_y_list = []
core_stack_list2_x = []
core_stack_list2_y = []

for file in new_list:
        match = regexu303_5.match(file)
        match1 = regexu303_6.match(file)
        if match:
                u303_peak_split_corestack_x_list.append(file)
                found = match
        if match1:
                u303_peak_split_corestack_y_list.append(file)
                found = match1

for file in u303_peak_split_corestack_x_list:
        match = regexu303_5.match(file)
        if match:
                corestack_num2x = match.group(2,3)
                core_stack_list2_x.append(corestack_num2x)
for file in u303_peak_split_corestack_y_list:
        match = regexu303_6.match(file)
        if match:
                corestack_num2y = match.group(2,3)
                core_stack_list2_y.append(corestack_num2y)       



#----------------------------------------- peak_split_new clump tables-------------------------#
#---U301
regex8 = re.compile('(.*)/u301_peak_split_newclump_c(\d{4})_c(\d{4})_Projection_x_density.png')
regex9 = re.compile('(.*)/u301_peak_split_newclump_c(\d{4})_c(\d{4})_Projection_y_density.png')

u301_peak_split_newclump_x_list = []
u301_peak_split_newclump_y_list = []
newclump_list_x = []
newclump_list_y = []

for file in new_list:
        match = regex8.match(file)
        match1 = regex9.match(file)
        if match:
                u301_peak_split_newclump_x_list.append(file)
                found=match
        if match1:
                u301_peak_split_newclump_y_list.append(file)
                found=match1
        
for file in u301_peak_split_newclump_x_list:
        match=regex8.match(file)
        if match:
                newclump_num_x = match.group(2,3)
                newclump_list_x.append(newclump_num_x)
for file in u301_peak_split_newclump_y_list:
        match=regex9.match(file)
        if match:
                newclump_num_y = match.group(2,3)
                newclump_list_y.append(newclump_num_y)
        

#---U302

regexu302_6 = re.compile('(.*)/u302_peak_split_newclump_c(\d{4})_c(\d{4})_Projection_x_density.png')
regexu302_7 = re.compile('(.*)/u302_peak_split_newclump_c(\d{4})_c(\d{4})_Projection_y_density.png')

u302_peak_split_newclump_x_list = []
u302_peak_split_newclump_y_list = []
newclump_list1_x = []
newclump_list1_y = []

for file in new_list:
        match=regexu302_6.match(file)
        match1=regexu302_7.match(file)
        if match:
                u302_peak_split_newclump_x_list.append(file)
                found=match
        if match1:
                u302_peak_split_newclump_y_list.append(file)
                found=match1
for file in u302_peak_split_newclump_x_list:
        match = regexu302_6.match(file)
        if match:
                newclump_num1x = match.group(2,3)
                newclump_list1_x.append(newclump_num1x)
for file in u302_peak_split_newclump_y_list:
        match = regexu302_7.match(file)
        if match:
                newclump_num1y=match.group(2,3)
                newclump_list1_y.append(newclump_num1y)

#---U303

regexu303_7 = re.compile('(.*)/u303_peak_split_newclump_c(\d{4})_c(\d{4})_Projection_x_density.png')
regexu303_8 = re.compile('(.*)/u302_peak_split_newclump_c(\d{4})_c(\d{4})_Projection_y_density.png')

u303_peak_split_newclump_x_list = []
u303_peak_split_newclump_y_list = []
newclump_list2x = []
newclump_list2y = []
for file in new_list:
        match = regexu303_7.match(file)
        match1 = regexu303_8.match(file)
        if match:
                u303_peak_split_newclump_x_list.append(file)
                found = match
        if match1:
                u303_peak_split_newclump_y_list.append(file)
                found = match1
for file in u303_peak_split_newclump_x_list:
        match = regexu303_7.match(file)
        if match:
                newclump_num2x = match.group(2,3)
                newclump_list2x.append(newclump_num2x)
for file in u303_peak_split_newclump_y_list:
        match = regexu303_8.match(file)
        if match:
                newclump_num2y = match.group(2,3)
                newclump_list2y.append(newclump_num2y)               


#-------------------------------------------peak_split_orig tables-------------------------------------#
#---U301
regex10 = re.compile('(.*)/u301_peak_split_orig_c(\d{4})_c(\d{4})_Projection_x_density.png')
regex11 = re.compile('(.*)/u301_peak_split_orig_c(\d{4})_c(\d{4})_Projection_y_density.png')

u301_peak_split_orig_x_list =[]
u301_peak_split_orig_y_list = []
orignum_list_x = []
orignum_list_y = []
for file in new_list:
        match = regex10.match(file)
        match1 = regex11.match(file)
        if match:
                u301_peak_split_orig_x_list.append(file)
                found=match
        if match1:
                u301_peak_split_orig_y_list.append(file)
                found=match1

for file in u301_peak_split_orig_x_list:
        match = regex10.match(file)
        if match:
                orignum_x = match.group(2,3)
                orignum_list_x.append(orignum_x)
for file in u301_peak_split_orig_y_list:
        match = regex11.match(file)
        if match:
                orignum_y = match.group(2,3)
                orignum_list_y.append(orignum_y)
                

#---U302
regexu302_8 = re.compile('(.*)/u302_peak_split_orig_c(\d{4})_c(\d{4})_Projection_x_density.png')
regexu302_9 = re.compile('(.*)/u302_peak_split_orig_c(\d{4})_c(\d{4})_Projection_y_density.png')
u302_peak_split_orig_x_list = []
u302_peak_split_orig_y_list = []
orignum_list1_x = []
orignum_list1_y = []

for file in new_list:
        match = regexu302_8.match(file)
        match1 = regexu302_9.match(file)
        if match:
                u302_peak_split_orig_x_list.append(file)
                found=match
        if match1:
                u302_peak_split_orig_y_list.append(file)
                found=match1
for file in u302_peak_split_orig_x_list:
        match = regexu302_8.match(file)
        if match:
                orignum1x = match.group(2,3)
                orignum_list1_x.append(orignum1x)
for file in u302_peak_split_orig_y_list:
        match = regexu302_9.match(file)
        if match:
                orignum1y=match.group(2,3)
                orignum_list1_y.append(orignum1y)

#---U303
regexu303_9 = re.compile('(.*)/u303_peak_split_orig_c(\d{4})_c(\d{4})_Projection_x_density.png')
regexu303_10 = re.compile('(.*)/u303_peak_split_orig_c(\d{4})_c(\d{4})_Projection_y_density.png')
u303_peak_split_orig_x_list = []
u303_peak_split_orig_y_list = []
orignum_list2_x = []
orignmum_list2_y = []

for file in new_list:
        match = regexu303_9.match(file)
        match1 = regexu303_10.match(file)
        if match:
                u303_peak_split_orig_x_list.append(file)
                found=match
        if match1:
                u303_peak_split_orig_y_list.append(file)
                found=match1
for file in u303_peak_split_orig_x_list:
        match = regexu303_9.match(file)
        if match:
                orignum2x = match.group(2,3)
                orignum_list2_x.append(orignum2x)
for file in u303_peak_split_orig_y_list:
        match = regexu303_10.match(file)
        if match:
                orignum2y=match.group(2,3)
                orignmum_list2_y.append(orignum2y)


#----------------------------------------------core_zoom_annotate..._projection_x tables
#----U301
regex12 = re.compile('(.*)/u301_core_zoom_annotate_c(\d{4})_n(\d{4})_Projection_x_density.png')
u301_core_zoom_image_list=[]
u301_core_zoom_corenum_list=[]

for file in new_list:
        match = regex12.match(file)
        if match:
                u301_core_zoom_image_list.append(file)
                found = match
for file in u301_core_zoom_image_list:
        match = regex12.match(file)
        if match:
                u301_core_zoom_num = match.group(2)
                u301_core_zoom_corenum_list.append(u301_core_zoom_num)

#---U302
regexu302_10 = re.compile('(.*)/u302_core_zoom_annotate_c(\d{4})_n(\d{4})_Projection_x_density.png')
u302_core_zoom_image_list = []
u302_core_zoom_corenum_list = []

for file in new_list:
        match = regexu302_10.match(file)
        if match:
                u302_core_zoom_image_list.append(file)
                found=match
for file in u302_core_zoom_image_list:
        match = regexu302_10.match(file)
        if match:
                u302_core_zoom_corenum1 = match.group(2)
                u302_core_zoom_corenum_list.append(u302_core_zoom_corenum1)

#---U303
regexu303_11 = re.compile('(.*)/u303_core_zoom_annotate_c(\d{4})_n(\d{4})_Projection_x_density.png')
u303_core_zoom_image_list = []
u303_core_zoom_corenum_list = []

for file in new_list:
        match = regexu303_11.match(file)
        if match:
                u303_core_zoom_image_list.append(file)
                found=match
for file in u303_core_zoom_image_list:
        match = regexu303_11.match(file)
        if match:
                u303_core_zoom_corenum1 = match.group(2)
                u303_core_zoom_corenum_list.append(u303_core_zoom_corenum1)


dummy1_masslist=[random.randrange(1000,10000,1) for i in range(300)]
dummy1_density_list=[random.randrange(1000,10000,1) for i in range(300)]
dummy_core_list=[random.randrange(1,300,1) for i in range (300)]

dummy_data=tuple(zip(u301_core_list,dummy1_masslist,dummy1_density_list))
total_data=tuple(zip(u301_core_zoom_corenum_list,dummy1_masslist,dummy1_density_list,u301_image_list, u301_proj_x_image_list, u301_peak_split_proj_x_list,u301_peak_split_proj_y_list,u301_peak_split_corestack_x_list, u301_peak_split_corestack_y_list,u301_peak_split_newclump_x_list,u301_peak_split_newclump_y_list,u301_peak_split_orig_x_list,u301_peak_split_orig_y_list,u301_core_zoom_image_list,u301_core_zoom_corenum_list))
#-----------------------------------------------Flask app/data-----------------------------------#

headings = ('Core ID','Mass','Density_time')
headings1 = ('Peak ID','Mass','Projection_x')
headings2_x = ('Excluded Core Number', 'Mass','Peak_Split_All_Projection_X')
headings2_y = ('Excluded Core Number', 'Mass','Peak_Split_All_Projection_Y')
headings3_x = ('Corestack Core Number','Mass','Peak_Split_Corestack_Projection_X')
headings3_y = ('Corestack Core Number', 'Mass','Peak_Split_Corestack_Projection_Y')
headings4_x = ('NewClump Core Number', 'Mass', 'Peak_Split_NewClump_Projection_X')
headings4_y = ('NewClump Core Number', 'Mass', 'Peak_Split_NewClump_Projection_Y')
headings5_x = ('Orig Core Number','Mass','Peak_Split_Orig_Projection_X')
headings5_y = ('Orig Core Number', 'Mass','Peak_Split_Orig_Projection_Y')
headings6 = ('Core ID', 'Mass','Core_Zoom_Annotate_Projection_X')
headings_tot = ('Core ID','Mass','Density', 'Density_time','Projection_x','Peak_Split_All_Projection_X','Peak_Split_All_Projection_Y', 'Peak_Split_Corestack_Projection_X','Peak_Split_Corestack_Projection_Y','Peak_Split_NewClump_Projection_X','Peak_Split_NewClump_Projection_Y','Peak_Split_Orig_Projection_X','Peak_Split_Orig_Projection_Y','Core_Zoom_Annotate_Projection_X')

#-------U301 Data ------------#
data = tuple(zip(u301_core_list,dummy1_masslist,u301_image_list))    #u301 density_time
data2 = tuple(zip(u303_core_list,dummy1_masslist, u303_image_list))  # u303 density_time
data3 = tuple(zip(u301_proj_x_image_list,dummy1_masslist,u301__proj_x_peakid_list))  #u301 projection_x
data4= tuple(zip(u301_peak_split_proj_x_list,u301_peak_split_proj_y_list,excluded_core_list_x,excluded_core_list_y,dummy1_masslist))
data5 = tuple(zip(u301_peak_split_corestack_x_list, u301_peak_split_corestack_y_list, corestack_list_x, corestack_list_y,dummy1_masslist))
data6 =tuple(zip(u301_peak_split_newclump_x_list,u301_peak_split_newclump_y_list,newclump_list_x, newclump_list_y,dummy1_masslist))
data7 = tuple(zip(u301_peak_split_orig_x_list,u301_peak_split_orig_y_list,orignum_list_x,orignum_list_y,dummy1_masslist))
data8 = tuple(zip(u301_core_zoom_image_list,u301_core_zoom_corenum_list,dummy1_masslist))  #u301 core_zoom_annotate list
def getKey(item):
        return item[0]
data8_sort = sorted(data8,key=getKey)
data8_every14 = data8_sort[0::14]

#-----Query Table Data
dataQuery_u301= tuple(zip(u301_core_list,dummy1_masslist))

#------U302 Data---------------#
data1 = tuple(zip(u302_core_list, u302_image_list))  #u302 density_time

data9 = tuple(zip(u302_proj_x_peakid_list, u302_proj_x_image_list))
data9_sort = sorted(data9,key=getKey)
data9_every3 = data9_sort[0::3]
data10 = tuple(zip(u302_peak_split_proj_x_list,u302_peak_split_proj_y_list,excluded_core_list1_x,excluded_core_list1_y)) #U302 Peak_split_Exclude_all
data11 = tuple(zip(u302_peak_split_corestack_x_list,u302_peak_split_corestack_y_list,core_stack_list1_x,core_stack_list1_y))
data12  = tuple(zip(u302_peak_split_newclump_x_list,u302_peak_split_newclump_y_list,newclump_list1_x,newclump_list1_y))
data13 = tuple(zip(u302_peak_split_orig_x_list,u302_peak_split_orig_y_list,orignum_list1_x,orignum_list1_y))
data14 = tuple(zip(u302_core_zoom_image_list,u302_core_zoom_corenum_list))
data14_sort = sorted(data14,key=getKey)
data14_every14 = data14_sort[0::14]


#--------U303 Data-------------------#

data15 = tuple(zip(u303_image_list,u303_core_list))
data16 = tuple(zip(u303_proj_x_image_list,u303_proj_x_peakid_list))
data16_sort = sorted(data16,key=getKey)
data16_every2 = data16_sort[0::2]
data17 = tuple(zip(u303_peak_split_proj_x_list,u303_peak_split_proj_y_list,excluded_core_list2_x,excluded_core_list2_y))
data18 = tuple(zip(u303_peak_split_corestack_x_list,u303_peak_split_corestack_y_list,core_stack_list2_x,core_stack_list2_y))
data19 = tuple(zip(u303_peak_split_newclump_x_list,u303_peak_split_newclump_y_list,newclump_list2x,newclump_list2y))
data20 = tuple(zip(u303_peak_split_orig_x_list,u303_peak_split_orig_y_list,orignum_list2_x,orignmum_list2_y))
data21 = tuple(zip(u303_core_zoom_image_list,u303_core_zoom_corenum_list))
data21_sort = sorted(data21,key=getKey)
data21_every14 = data21_sort[0::14]


app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
	return render_template("home.html")	

@app.route('/u301')
def u301_tables():
	return render_template("table_u301.html", headings=headings,total_data=total_data, headings1=headings1, data=data, data3=data3, headings2_x=headings2_x, headings2_y=headings2_y, data4=data4, headings3_x=headings3_x,headings3_y=headings3_y, data5=data5, headings4_x=headings4_x, headnigs4_y=headings4_y, data6=data6, data7=data7, headings5_x=headings5_x, headings5_y=headings5_y, data8_every14=data8_every14, headings6=headings6)

@app.route('/u301/customizer')
def u301_table_customizer():
        return render_template("query_table.html", headings_tot=headings_tot, total_data=total_data)

        

@app.route('/u302')
def u302_table():
	return render_template("table_u302.html", headings=headings, headings1=headings1,headings2_x=headings2_x,headings2_y=headings2_y, data1=data1, data9_every3=data9_every3, data10=data10, data11=data11, headings3_x=headings3_x, headings3_y=headings3_y, headings4_x=headings4_x, headings4_y=headings4_y,data12=data12,headings5_x=headings5_x, headings5_y=headings5_y, data13=data13, data14_every14=data14_every14)

@app.route('/u303')
def u303_table():
	return render_template("table_u303.html", headings=headings, data2=data2,data15=data15,data16_every2=data16_every2,headings1=headings1, headings2_x=headings2_x, headings2_y=headings2_y, data17=data17, headings3_x=headings3_x, headings3_y=headings3_y,data18=data18, data19=data19,headings4_x=headings4_x,headings4_y=headings4_y, headings5_x=headings5_x,headings5_y=headings5_y,data20=data20,data21_every14=data21_every14)


if __name__ == "__main__":
	app.run(debug=True)
