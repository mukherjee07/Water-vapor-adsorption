set term pngcairo size 3500,2900 font "Arial,20" fontscale 3.0 enhanced
#size 9000, 5000 
set size 0.85,1.0
set output '2DAR25_ZR.png'

set datafile separator comma
set view map
set encoding iso_8859_1
#unset surface
filename="AR_ZR.csv"
#unset xtics
set xlabel font "Times Roman, 20"
set ylabel font "Times Roman, 20"
#set zlabel font "Times Roman, 20"
set title font "Times Roman, 25"
set title 'Electric potential for an idealised cylinder with 9{\305} Diameter (Alt radial)'
set title offset 4,0
set xlabel 'radial distance from center (in Angstorm)'
set ylabel 'Z-axis (in Angstorm)'
#set xlabel offset 0,0
#set ylabel offset -1,0
set xrange [0:9]
set yrange [0:30.8]
set xtics border
set ytics border
set origin 0,0
#set xyplane at 0
#set zlabel 'Electric Potential '
#set colorbox
set cblabel 'Electric Potential (in Nm/C)'
set cblabel font 'Times Roman, 20'
set cblabel offset 2,0
set cbrange [-1E19:1E19]
set palette model RGB
#set palette defined (8E19 "dark-yellow", 3E19 "orange", 1E19 "orange-red", 0 "red", 0 "purple", -1E19 "mediumpurple3", -3E19 "blue", -8E19 "dark-blue" )
#load potential_new.csv
set pm3d interpolate 100,100 
splot filename using 1:2:3 with pm3d #and image
show colorbox label
set hidden3d
