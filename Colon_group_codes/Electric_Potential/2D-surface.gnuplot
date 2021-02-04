set term pngcairo size 3500,2900 font "Hevlectica,20" fontscale 3.0 enhanced
#size 9000, 5000 
set size 0.85,1.0
set output '2DBAA26_ZXYZ.png'

set datafile separator comma
set view map
set encoding iso_8859_1
#unset surface
filename="AAZXYZ.csv"
#unset xtics
set xlabel font "Hevlectica, 20"
set ylabel font "Hevlectica, 20"
#set zlabel font "Hevlectica, 20"
set title font "Hevlectica, 23"
set title 'Electric potential for an ICC with 9{\305} Diameter at Z = POS{\305} (Alt along)'
set title offset 5,0
set xlabel 'xaxis (in {\305})'
set ylabel 'yaxis (in {\305})'
set xlabel offset 0,0
set ylabel offset -1,0
set xrange [7.9:22.9]
set yrange [7.9:22.9]
set xtics border
set ytics border
set origin 0,0
#set xyplane at 0
#set zlabel 'Electric Potential '
#set colorbox
set cblabel 'Electric Potential (in Nm/C)'
set cblabel font 'Hevlectica, 20'
set cblabel offset 2,0
set cbrange [-8E19:8E19]
set palette model RGB
#set palette defined (-8E19 "dark-green", -3E19 "green", -1E19 "light-green", 0 "light-green", 0 "orange", 1E19 "dark-orange", 3E19 "red", 8E19 "dark-red")
#load potential_new.csv
set pm3d interpolate 100,100 
splot filename using 1:2:3 with pm3d #and image
show colorbox label
set hidden3d
#set lmargin at screen 0.1
#set rmargin at screen 10.7
#splot 'potential_new.csv' using 1:2:3:4 with image
#set term png truecolor notransparent nocrop enhanced font arial 20 size 
#1200,1200 linewidth 2 
