"""
Author: Krishnendu Mukherjee, Chemical Engineering, University of Notre Dame
Advisor: Dr. Yamil Colon
"""

#importing libraries
import numpy as np
import pandas as pd
import math
import os
import re

#defining key parameters
k = 9E19
filename = "IC_25_full_XXX.csv"
atomsperring_i = 1
cell_length = 30.80
z_length = cell_length
probe_length = 9.0
delta = 0.25
#rings = int(round(probe_length/ring_delta))
counter = 0
#z_position = 0
bond_length = 1.54
Z = int(round(z_length/bond_length))
#X = int(probe_length/delta)
#Y = int(probe_length/delta)
N = int(probe_length/delta)

#Creating a .csv file for storing data
os.system("touch "+str(filename))

#checking if the .csv is present or not; if there old one would be removed and a new instance would be created
os.system("rm -f "+str(filename))
os.system("echo X,Y,Z,Potential >> "+str(filename))

# Running the bash code potential-sh to create the file .csv for reading
os.system("bash potential-sh")

# Extracting the coordinate of our CIF file -- the structure file
dataset = pd.read_csv('IC_25_XXX.csv',delimiter=',')
x = dataset.iloc[:,0].values
y = dataset.iloc[:,1].values
z = dataset.iloc[:,2].values

# Extracting the number of lines/elements in the .csv file
total = len(dataset)

# deconverting from crystallographic format to XYZ style
x = x*cell_length
y = y*cell_length
z = z*z_length

# Extracting charges
c = dataset.iloc[:,3].values

#Making grid for storing electric potential data
grid_space = (N+1)*(N+1)*(Z+1)
grid_space = int(grid_space)
print(grid_space)

#defining empty arrays with no size
'''r_x = []
r_y = []
r_z = []
p = []
'''
r_x = [0 for x in range(grid_space)] 
r_y = [0 for x in range(grid_space)] 
r_z = [0 for x in range(grid_space)] 
p = [0 for x in range(grid_space)] 


#print(Z_stacks,rings,grid_space)
#defining grid_space
for x_counter in range(N+1):
	#print (z_position)
	for y_counter in range(N+1):
		for z_position in range(Z+1):
			# Generating coordinates in cartesian coordinates
			r_x[counter] = cell_length/2 - probe_length/2 + x_counter*delta
			r_y[counter] = cell_length/2 - probe_length/2 + y_counter*delta
			r_z[counter] = (z_position*cell_length/Z)
			#print(r_x[counter])
			counter += 1
#print(counter,grid_space)

#looping through all the points in the grid-space
for i in range(counter):
	#going through all the elements in the box
	if ( i%(Z) == 0 and i != 0 ):
		os.system("echo "+"  >> "+str(filename))
	for num in range(total):
		X_D = (x[num]-r_x[i])**2 
		Y_D = (y[num]-r_y[i])**2
		Z_1 = (z[num]-r_z[i])**2
		Z_2 = (z[num]-r_z[i]-cell_length)**2
		Z_3 = (z[num]-r_z[i]+cell_length)**2 	   
		distance1 = np.sqrt(X_D + Y_D + Z_1)
		distance2 = np.sqrt(X_D + Y_D + Z_2)
		distance3 = np.sqrt(X_D + Y_D + Z_3)
		if (distance2 < 30 and distance3 < 30):
			p[i] = p[i] + (k*c[num]*((1/distance1)+(1/distance2)+(1/distance3)))
		elif (distance2 > 30 and distance3 < 30):
			p[i] = p[i] + (k*c[num]*((1/distance1)+(1/distance3)))
		elif (distance2 < 30 and distance3 > 30):
			p[i] = p[i] + (k*c[num]*((1/distance1)+(1/distance2)))
		elif (distance2 > 30 and distance3 > 30):
			p[i] = p[i] + (k*c[num]*((1/distance1)))
			
		
		#print("At position number: ",i,"in grid space, the electric field is: ",p[i])
		#if ( (r_x[i]-(cell_length/2))**2 + ((r_y[i]-(cell_length/2))**2) <= (probe_length/2)**2 ):	
	os.system("echo "+str(r_x[i])+","+str(r_y[i])+","+str(r_z[i])+","+str(p[i])+" >> "+str(filename))

#looping through all the points in the grid-space
for z_counter in range(Z+1):
	#making z file for value of Z
	z_filename = "XXXZ"+str(z_counter)+".csv"
	d_z = (z_counter*cell_length/Z)
	#Creating a .csv file for storing data
	#os.system("touch "+str(z_filename))
	#checking if the .csv is present or not; if there old one would be removed and a new instance would be created
	os.system("rm -f "+str(z_filename))
	os.system("touch "+str(z_filename))
	#going through all the elements in the box
	for x_counter in range(N+1):
		d_x = cell_length/2 - probe_length/2 + x_counter*delta
		for y_counter in range(N+1):
			d_y = cell_length/2 - probe_length/2 + y_counter*delta	
			P = 0
			for num in range(total):
				X_D = (x[num]-d_x)**2 
				Y_D = (y[num]-d_y)**2
				Z_1 = (z[num]-d_z)**2
				Z_2 = (z[num]-d_z-cell_length)**2
				Z_3 = (z[num]-d_z+cell_length)**2 	   
				distance1 = np.sqrt(X_D + Y_D + Z_1)
				distance2 = np.sqrt(X_D + Y_D + Z_2)
				distance3 = np.sqrt(X_D + Y_D + Z_3)
				if (distance2 < 30 and distance3 < 30):
					P = P + (k*c[num]*((1/distance1)+(1/distance2)+(1/distance3)))
				elif (distance2 > 30 and distance3 < 30):
					P = P + (k*c[num]*((1/distance1)+(1/distance3)))
				elif (distance2 < 30 and distance3 > 30):
					P = P + (k*c[num]*((1/distance1)+(1/distance2)))
				elif (distance2 > 30 and distance3 > 30):
					P = P + (k*c[num]*((1/distance1)))
				#P = P + (k*c[num]*((1/distance1)+(1/distance2)+(1/distance3)))
				#print("At position number: ",i,"in grid space, the electric field is: ",p[i])
			#if ( (d_x - (cell_length/2))**2 + ((d_y - (cell_length/2))**2) <= (probe_length/2)**2 ):	

			os.system("echo "+str(d_x)+","+str(d_y)+","+str(P)+" >> "+str(z_filename))
		os.system("echo "+"  >> "+str(z_filename))

