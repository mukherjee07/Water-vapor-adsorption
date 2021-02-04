"""
Author: Krishnendu Mukherjee, Chemical Engineering, University of Notre Dame
Advisor: Dr. Yamil Colon
Objectives: Given a .csv input with water molecules position listed as H1,H2,O in cartesian coordinates in a row, find the number of hydrogen bonds
corresponding to each of them and also the total h-bonds in the system
"""

#importing libraries
import numpy as np
import pandas as pd
import math
import os
import re

#defining key parameters
cell_length = 30.80
z_length = cell_length

# Extracting the coordinates of the loaded water molecules
waterdataset = pd.read_csv('water.csv',delimiter=',')
X_h1 = waterdataset.iloc[:,0].values
Y_h1 = waterdataset.iloc[:,1].values
Z_h1 = waterdataset.iloc[:,2].values
X_h2 = waterdataset.iloc[:,3].values
Y_h2 = waterdataset.iloc[:,4].values
Z_h2 = waterdataset.iloc[:,5].values
X_o = waterdataset.iloc[:,6].values
Y_o = waterdataset.iloc[:,7].values
Z_o = waterdataset.iloc[:,8].values

# Extracting the length 
water_size = len(waterdataset)

#Initialisng hydrogen bond scaler for all the water molecules
H = np.zeros(water_size)

#Initialising the hydrogen bond histogram variables for 0-4 numbers of H-bonds (for a given molecule i) associated with the whole system
H0 = 0
H1 = 0
H2 = 0
H3 = 0
H4 = 0

#Looping through all the water molecule position to correct the boundary crossing and fit all the molecules in a single cylinder (pore)
for i in range(water_size):
	# if the water molecules cross the boundary in either of the end, subtract the fractional coordinates with it
	if (Z_h1[i] > z_length):
		Z_h1[i] = Z_h1[i] - z_length
	elif (Z_h1[i] < 0):
		Z_h1[i] = Z_h1[i] + z_length
	if (Z_h2[i] > z_length):
		Z_h2[i] = Z_h2[i] - z_length
	elif (Z_h2[i] < 0):
		Z_h2[i] = Z_h2[i] + z_length
	if (Z_o[i] > z_length):
		Z_o[i] = Z_o[i] - z_length
	elif (Z_o[i] < 0):
		Z_o[i] = Z_o[i] + z_length

#traversing from one by one through all the oxygen atoms and then finding the network pattern for each of them
for i in range(water_size):
	for j in range(water_size-1):
		#first constraint O-O distance should be less than 3.5 Angstorm
		OO = math.sqrt((X_o[i]-X_o[j])**2 + (Y_o[i] - Y_o[j])**2 + (Z_o[i] - Z_o[j])**2)
		if (OO < 3.5):

			#first constraint passed! go for the second one H-O...O angle should be less than 30 degrees
			# to find the angle we need to first find the vector arms
			a = np.array([X_h1[i],Y_h1[i],Z_h1[i]]) #position of hydrogen 1 for i  	
			b = np.array([X_o[i],Y_o[i],Z_o[i]]) #position of oxygen for i 	
			c = np.array([X_o[j],Y_o[j],Z_o[j]]) #position of oxygen for j
			d = np.array([X_h2[i],Y_h2[i],Z_h2[i]]) #position of hydrogen 2 for i
		
			# finding the two vectors for H1-O and O-O
			ba = a - b
			bc = c - b	
			
			# finding the vector for H2-O
			bd = d - b
			
			#now finding the angle 1 cosine between the arm
			#print(ba,bc)
			cosine_angle1 = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
			angle1 = np.arccos(cosine_angle1)
			angle1 = np.degrees(angle1)
			
			#now finding the angle 1 cosine between the arm
			#print(ba,bc)
			cosine_angle2 = np.dot(bd, bc) / (np.linalg.norm(bd) * np.linalg.norm(bc))
			angle2 = np.arccos(cosine_angle2)
			angle2 = np.degrees(angle2)
			
			#a test to by-pass the second constraint, uncomment the next line and comment out the 2nd constraint below
			#H[i] = H[i] + 1
			#'''
			#using the second constraint of arm angles for h-bonding 
			if (angle1 < 30 or angle2 < 30):
				#add one more to the number of hydrogen bonds corresponding to atom i
				H[i] = H[i] + 1

			#'''
	#conditions loops to bin he hydrogen bond for a given molecules into different variables
	if (H[i] == 0):
		H0 += 1
	elif (H[i] == 1):
		H1 += 1
	elif (H[i] == 2):
		H2 += 1
	elif (H[i] == 3):
		H3 += 1
	elif (H[i] == 4):
		H4 += 1

	print(H[i])
print("total number of hydrogen bonds in the system is: ",np.sum(H))
print(H0,H1,H2,H3,H4)
