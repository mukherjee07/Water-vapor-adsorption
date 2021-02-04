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
filename = "AR_ZR.csv"
atomsperring_i = 1
cell_length = 30.8
z_length = cell_length
probe_radius = 9.0
ring_delta = 0.50
rings = int(round(probe_radius/ring_delta))
counter = 0
z_position = 0
bond_length = 1.54
Z_stacks=int(round(z_length/bond_length))

#Creating a .csv file for storing data
os.system("touch "+str(filename))

#checking if the .csv is present or not; if there old one would be removed and a new instance would be created
os.system("rm -f "+str(filename))
os.system("echo X,Y,Z,Potential >> "+str(filename))

# Extracting the coordinate of our CIF file -- the structure file
dataset = pd.read_csv('final.csv',delimiter=',')
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
#grid_space = (rings + ((3/2)*rings*(rings+1)))*rings*Z_stacks
#grid_space = int(grid_space)
#print(grid_space)

#defining empty arrays with no size
'''r_x = []
r_y = []
r_z = []
p = []
'''
#r_x = [0 for x in range(grid_space)] 
#r_y = [0 for x in range(grid_space)] 
#r_z = [0 for x in range(grid_space)] 
#p = [0 for x in range(grid_space)] 


#print(Z_stacks,rings,grid_space)
#defining grid_space
#for z_position in range(Z_stacks):
for ring_counter in range(rings):
	#print (z_position)
	r = ring_delta*ring_counter
	for z_position in range(Z_stacks):
	#for ring_counter in range(rings):
		d_z = (z_position*cell_length/Z_stacks)
		atomsperring = atomsperring_i + (3*ring_counter)
		P = [0 for x in range(atomsperring)]	
		for position_counter in range(atomsperring):
			theta = 360*(position_counter/atomsperring)
			# Generating coordinates in radial coordinates
			d_x = cell_length/2 + r*math.sin(math.radians(theta))
			d_y = cell_length/2 + r*math.cos(math.radians(theta))
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
					P[position_counter] = P[position_counter] + (k*c[num]*((1/distance1)+(1/distance2)+(1/distance3)))
				elif (distance2 > 30 and distance3 < 30):
					P[position_counter] = P[position_counter] + (k*c[num]*((1/distance1)+(1/distance3)))
				elif (distance2 < 30 and distance3 > 30):
					P[position_counter] = P[position_counter] + (k*c[num]*((1/distance1)+(1/distance2)))
				elif (distance2 > 30 and distance3 > 30):
					P[position_counter] = P[position_counter] + (k*c[num]*((1/distance1)))
		P_final = np.average(P)
		os.system("echo "+str(r)+","+str(d_z)+","+str(P_final)+" >> "+str(z_filename))
	os.system("echo "+"  >> "+str(filename))
			#print(r_x[counter])
			#counter += 1
#print(counter,grid_space)

'''
#looping through all the points in the grid-space
for i in range(counter):
	#going through all the elements in the box
	for num in range(total):
		distance = np.sqrt((x[num]-r_x[i])**2 + (y[num]-r_y[i])**2 + (z[num]-r_z[i])**2)
		p[i] = p[i] + ((k*c[num])/distance)
		#print("At position number: ",i,"in grid space, the electric field is: ",p[i])

	os.system("echo "+str(r_x[i])+","+str(r_y[i])+","+str(r_z[i])+","+str(p[i])+" >> "+str(filename))
'''
