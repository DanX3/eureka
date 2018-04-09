# setting the range of the plot, auto by default
# set xrange [0:16]
# set yrange [0:16]
set autoscale

# axis settings
set title 'Title'
set xlabel 'X axis'
set ylabel 'Y axis'
set log y
# set log x
# set xtics rotate by 45 offset -4,-2

# set the legend on the top left corner
set key left top

# style settings
set style line 1 linecolor rgb '# 0060ad' linetype 1 linewidth 2
set style line 2 linecolor rgb '# 2196F3' pointtype 7 pointsize 2
set terminal pngcairo size 800,600 enhanced font 'Helvetica,12'
# set terminal svg size 800,600 fname 'Verdana' fsize 10
set grid

#set output "plot.png"
#plot 'data.dat' using 1:2 title '1e4' with lines ls 2
