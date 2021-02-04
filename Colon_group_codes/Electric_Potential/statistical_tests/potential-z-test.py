'''
Author: Krishnendu Mukherjee
Advisor: Dr. Yamil Colon
Affiliation: University of Notre Dame
The aim of this code is to study Idealized structures (carbon) and understand
how electric potential affects the phenomena of water vapor adsorption.
In that respect, this code is simply a statistical test whether the electric 
potential of these structures are affected by the adosprtion of water or not.
We have two hypothesis at play here:
H0 : Null hypothesis, i.e. The change in electric field is not affecting water adsoprtion phenomena and any changes or deviation from the mean of 0 is due to random error,
H1 : The Alternate hypothesis, i.e. the difference in the electric potential due to water vapor loading is indeed a result of electric potential and there is no random error involved.
We would finally present things like, statistical power and probability of null hyopthesis being true as a final result
Input: The code would need two csv files or even one, having the corresponding electric potentials across different grids
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as stats

#importing the two datasets, one loaded and the other empty
dataset1 = pd.read_csv("IC_26_full_Inner.csv",delimiter=",")
dataset2 = pd.read_csv("IC_26_full_Inner_L.csv",delimiter=",")

#B contains potential at 0% RH (i.e. before loading of water)
B = dataset1.iloc[:,3].values

#A contains potential at 100% RH
A = dataset2.iloc[:,3].values

#extracting the size of the dataset
size = len(dataset1)

#The first approach is dividing the initial grid-space into positive and negative potential scalers and then tracking if 
# their magnitudes changes as a function or randomly after loading

#Expected number of positive and negative grids
Pos = 0
Neg = 0

#Looping through grid-space to differentiate the two vectors
for i in range(size):
	if (B[i] > 0):
		Pos = Pos + 1
	elif (B[i] < 0):
		Neg = Neg + 1

#print(size,Pos,Neg,Pos+Neg)
#Creating grid scalers to store positive & negative potential
V_pos = np.zeros(Pos)
V_neg = np.zeros(Neg)

#re-initialising them to zero
Pos = 0
Neg = 0

#Cumulative vector which shows directions of change of electric potential
# PP = Pos--> Pos, NN = Neg --> Neg and so-on
PP = 0
PN = 0
NP = 0
NN = 0

#magnitude of potential changes; corresponding to the vectors above
mPP = 0
mPN = 0
mNP = 0
mNN = 0

#going through the difference between loaded and un-loaded potential at same locations
#and analysing how many of them changed from p-->n or n-->p or p-->p or n-->n
for i in range(size):
	if (B[i] > 0):
		V_pos[Pos] =  B[i] - A[i]
		if (B[i] > A[i]):
			PN = PN + 1
			mPN = mPN + V_pos[Pos]
		else:
			PP = PP + 1
			mPP = mPP + V_pos[Pos]
		Pos = Pos + 1
	elif (B[i] < 0):
		V_neg[Neg] = B[i] - A[i]
		if (A[i] > B[i]):
			NP = NP + 1
			mNP = mNP + V_neg[Neg]
		else:
			NN = NN + 1
			mNN = mNN + V_neg[Neg]
		Neg = Neg + 1

#Testing the null hypothesis for these vectors
# Testing for the positive potential grid-points first

#calculating the mean and standard deviation first
mean_pos = np.mean(V_pos)
std_pos = np.std(V_pos,ddof=1)

#calculating the z-value and the corresponding p-value of the null-hypothesis
z_pos = mean_pos/(std_pos/math.sqrt(Pos))
pval_pos = stats.norm.cdf(z_pos,Pos-1)

#printing the p-value and alpha for positive grid-points
print(mean_pos,std_pos,z_pos,pval_pos)

#printing the electric potential grid direction vector
print("Number of grid point changes (in fraction of total change)")
print("Pos-Pos,Pos-Neg",PP/size,PN/size)
print("Neg-Pos,Neg-Neg",NP/size,NN/size)

#printing the magnitude of the electric potential grid direction vector
mPP = -mPP
mNP = -mNP
TC = mPP + mNP + mPN + mNN

print("Magnitude of change matrix (in fraction of total change)")
print("Pos-Pos,Pos-Neg",mPP/TC,mPN/TC)
print("Neg-Pos,Neg-Neg",mNP/TC,mNN/TC)

# Testing for the negative potential grid-points
mean_neg = np.mean(V_neg)
std_neg = np.std(V_neg,ddof=1)
z_neg = mean_neg/(std_neg/math.sqrt(Neg))
pval_neg = stats.norm.cdf(z_neg,Neg-1)

#printing the p-value and alpha for negative grid-points
print(mean_neg,std_neg,z_neg,pval_neg)

# This is the second approach
'''
size = len(dataset1)
D = B - A
#print(D[:10])
#D = np.abs(D)
#print(D[:10])
mean = np.mean(D)
sigma = np.std(D,ddof=1)
print(mean,sigma)

#calculating the z-score
zscore = mean/(sigma/math.sqrt(size))
print("The z-score is ",zscore)

#calculating the p-value and then alpha
pval = stats.norm.cdf(zscore,size-1)

print("The p-value for this statistical test",pval)
#print(avg/sigma/np.sqrt(size))
'''
