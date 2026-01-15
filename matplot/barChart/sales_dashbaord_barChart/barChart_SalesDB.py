import matplotlib.pyplot as plt
import numpy as np

items = ["Phone" , "Tablet", "Laptop"]
NY_Sales = [120,80,50]
CA_Sales = [135,70,65]
x_indexes = np.arange(len(items))
width = 0.4
plt.bar(x_indexes - width/2 , NY_Sales, label = "New York Sales" , color = "blue" , width = width)
plt.bar(x_indexes + width/2 , CA_Sales , label = "California Sales" , color = "green" , width = width)
plt.grid(axis='y' , linestyle = '--')
plt.xticks(ticks=x_indexes,labels=items)
plt.title("Sales Dashboard : New York vs. California")
plt.xlabel("Items")
plt.ylabel("Units Sold")
plt.legend(loc ='best')
plt.savefig('sales_dashboard.png')
plt.show()