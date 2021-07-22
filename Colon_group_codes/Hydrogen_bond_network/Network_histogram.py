'''
Author: Krishnendu Mukherjee
Affiliation: University of Notre Dame
Advisor: Dr. Yamil Colon
Objective: To plot a histogram for number of hydrogen bonds per molecules for different numbers for different configurations
'''

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#defining the bar widht variable
barw = 0.125

#reading the data into different bins
dataset = pd.read_csv('Network.csv',delimiter=',')
num = dataset.iloc[:,0].values
AR = dataset.iloc[:,1].values
AA = dataset.iloc[:,2].values
AAR = dataset.iloc[:,3].values
IP = dataset.iloc[:,4].values
OP = dataset.iloc[:,5].values
#legend = ['Alt_radial', 'Alt_along','Alt_along_radial','Inner_positive','Outer_positive']

#setting positions for bars on x-axis
br1 = np.arange(len(num))
br2 = [x + barw for x in br1 ]
br3 = [x + barw for x in br2 ]
br4 = [x + barw for x in br3 ]
br5 = [x + barw for x in br4 ]

fig = plt.subplots()
p1 = plt.bar(br1,AR, edgecolor='black', width = barw, color = 'blue')
p2 = plt.bar(br2,AA, edgecolor='black', width = barw, color = 'red')
p3 = plt.bar(br3,AAR, edgecolor='black', width = barw, color = 'black')
p4 = plt.bar(br4,IP, edgecolor='black', width = barw, color = 'orange')
p5 = plt.bar(br5,OP, edgecolor='black', width = barw, color = 'cyan')
plt.ylabel("Frequency of total hydrogen bonds\n per molecule of water",fontsize="25")
plt.xlabel("Number of Hydrogen bonds",fontsize="25")
plt.legend((p1[0],p2[0],p3[0],p4[0],p5[0]),('Alt_radial','Alt_along','Alt_along_radial','Inner_positive','Outer_positive'),fontsize='16')
#plt.xticks(range(0, 4))
#plt.yticks(range(0, 50))
plt.title('Hydrogen bonding network histogram for an ICC of 9.24$\AA$ pore size\n for different charge configurations',fontsize='25')
plt.show()
