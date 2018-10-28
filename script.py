#These two lines below provide a diplay name and $DISPLAY environment variable.
#Those were errors I had been getting without adding them at the very 
#beggining of the scrit.
#Another option is to comment these two lines out and use ssh -Y when 
#logging to the server.

import matplotlib               
matplotlib.use('PDF')

#Problem 1
#Opening the file
fhand = open('CO-OPS__8729108__wl.csv')
#Setting initial values of the variables
water_level = 0
largest = None
#Initiating the for loop that reads line per line and finds the largest value
#for the string section that delimits the water level.
#I used a try and except because the first line was just the title of the dataset
#and I wanted to avoid that.
for line in fhand:
#Setting the portions of the data set to be analyzed.
     date_time_curr = line[:16]
     water_level = line[17:22]
     try:
#Setting how the loop will operate when running line by line.
        water_level_float = float(water_level)
        if largest is None or water_level_float > largest :
            largest = water_level_float
#Keeping track of the day and time the highest value was obtained.
            date_time_max = date_time_curr
              
     except:
        continue
#Printing the largest value and also the day and time when this value was obtained.
print(largest, date_time_max)

#Problem 2
#Necessary to import Pandas in order to use it.
import pandas as pd

#Opening the file with Pandas. Notice how different it is than how it is done
#in problem 1.
df=pd.read_csv("/ufrc/zoo6927/share/mariacortez/CO-OPS__8729108__wl.csv")
#Verify if the data set was correctly opened.
df.head()
#Verify how the columns are labeled to select them in the next step.
df.columns
#Print the line in the data set that cointains the highest water level.
print(df[df[' Water Level']==df[' Water Level'].max()])

#Problem 3
#Setting initial values of the variable.
largest = None
#Creating an empty list to receive what will be selected through the for loop.
difference_list = []
#Setting i equals 0 so the loop can start at the first row.
i = 0
#Initiating the for loop that reads line per line and finds the largest value
#across all the rows in the data set.
#I used a try and except because the first row was just the title of the dataset
#and I wanted to avoid that.
for i, row in df.iterrows():
    try:
#Setting the date and time(0) column and the water level column(1) to be analyzed in the loop.
#For the water level column we compute the difference between two consecutive measurements.
        difference_date_time = df.iloc[i + 1, 0]
        difference = (df.iloc[(i + 1), 1] - df.iloc[(i), 1])
#Appending the difference computed to the list.
        difference_list.append(difference)
#Using the for loop to select the largest value in the difference list computed.
        for line in difference_list:
            if largest is None or line > largest:
                largest = line
#Keeping track of the date and time when the biggest difference was obtained.
                difference_date_time_max = difference_date_time
    except:
        continue
#Printing the largest difference and also the correspondent day and time that this was obtained. 
print(largest, difference_date_time_max)

#Problem 4
#Import all the necessary packages to run the script.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker 
#Open the data set using Pandas.
df=pd.read_csv("/ufrc/zoo6927/share/mariacortez/CO-OPS__8729108__wl.csv")
#Verify if the data set was correctly opened.
df.head()
#Verify how the columns are labeled to select them in the next step.
df.columns
#Naming the columns in the data set that will be used to produce the graph.
water_level = df[' Water Level']
time = df['Date Time']

#Creating an empty figure to receive the plot information.
fig = plt.figure()
#Creating the axis that will later be modified.
ax = plt.axes()
#Ploting the graph based on the info recovered by the variables selected in the data set.
plot = plt.plot(time, water_level,'-')
#Creating the title of the plot and defining the size of the font.
fig.suptitle('Water level variation over time during Hurricane Michael', fontsize=10)
#Setting the ticks to be recovered within a bigger interval, diminishng the number of
#ticks shown in the graph.
ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
#Setting the 'x' label.
ax.set_xlabel('Time', fontsize=10)
#Setting the 'y' label.
ax.set_ylabel('Water level', fontsize=10)
#Setting the size of the ticks labels in 'x' axis.
ax.tick_params(axis='x', labelsize=6)
#Setting the size of the ticks labels in the 'y' axis.
ax.tick_params(axis='y', labelsize=8)
#Fitting the graph in the area available for the figure.
plt.gcf().autofmt_xdate()
#Saving the figure under 'my_figure.pdf'
fig.savefig('my_figure.pdf')






