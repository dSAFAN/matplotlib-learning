import matplotlib.pyplot as plt
import numpy as np

#Simple vertical bar graph
x = ["Action","Comedy","Drama","Sci-Fi","Horror"]
y = [150,110,85,130,60]
plt.xlabel("Genre")
plt.ylabel("Tickest Sold")
plt.title("Movie Genre Popularity")
#plt.bar(x,y,color = "teal")
#plt.show()

#Simple horizonatl bar graph
xy = ["Python","JavaScript","C++","Java","Go"]
yx = [85 , 70 , 45 , 60 , 30]
#plt.barh(xy,yx,color='salmon')
plt.grid(axis='x',linestyle='--',alpha=0.7)
plt.title("Favourite Programming Languages")
plt.xlabel("Number of Votes")
plt.ylabel("Language")
#plt.show()

#Grouped bar chart
# 1
Products = ["Laptop","Mouse","Monitor","Keyboard"]
sales_22 = [200,150,180,120]
sales_23 = [250,140,200,170]
x_indexes = np.arange(len(Products))
w = 0.35

#plt.bar(x_indexes - w/2, sales_22 , width= w , label = "2022 Sales")
#plt.bar(x_indexes + w/2, sales_23 , width= w , label = "2023 Sales")

plt.title("Electronics Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.xticks(ticks=x_indexes,labels=Products)

plt.legend()
#plt.show()

# 2
Subjects = ["Math","Science","English","History"]
Boys = [75,80,65,70]
Girls = [80,75,70,75]
xx = np.arange(len(Subjects))
ww = 0.4

plt.bar(xx + ww/2 ,Girls , label = "Girls Average" , color = "pink" , width = ww )
plt.bar(xx - ww/2 ,Boys , label = "Boys Average" , color = "blue" , width = ww )

plt.xticks(ticks=xx , labels=Subjects)
plt.grid(axis="y",linestyle="--")

plt.title("School Exam Grades : Boys vs. Girls")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.legend(loc = 'best')
plt.show() 

Teams = ["Team A" , "Team B" , "Team C"]
attackPoints = [40,55,30]
defensePoints = [20,15,35]

plt.bar(Teams, attackPoints , label = "Attack Points" , color = "red" , alpha = 0.5)
plt.bar(Teams, defensePoints ,label = "Defense Points" , bottom= attackPoints , color = "blue" , alpha = 0.4)

plt.legend(loc = 'best')
plt.title("Total Score Tracker")
plt.xlabel("Teams")
plt.ylabel("Score")
plt.grid(axis="y",linestyle = '--')

plt.show()