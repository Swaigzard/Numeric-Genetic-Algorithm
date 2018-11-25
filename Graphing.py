from GA import *
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


# Creates the legend for the graph
RED = mpatches.Patch(color='red',label='Average Fitness per Generation')
BLUE = mpatches.Patch(color='blue',label='Best Fitness per Generation')
plt.legend(handles=[RED,BLUE])

# Title for graph and window
plt.title('Fitness Measurements Per Generation')
fig = plt.gcf()
fig.canvas.set_window_title('Genetic Algorithm Graphing')

# Average fitness per generation imported from GA file
x1 = GA.GenCounterList
y1 = GA.AvgFitness
# Best fitness per generation imported from GA file
x2 = GA.GenCounterList
y2 = GA.BestFit

plt.plot(x1,y1,'r',x2,y2,'b')
plt.ylabel('Fitness')
plt.xlabel('Generation')

plt.show()

