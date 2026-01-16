import matplotlib.pyplot as plt

items = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [15, 30, 45, 10]

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=items , autopct='%1.1f%%', 
        wedgeprops={'width':0.3,'edgecolor':'white'} ,
        labeldistance = None)
plt.title("Pie Challange 2" , fontsize = 16 , fontweight = 'bold')
plt.legend(title = "Fruit Types" , loc ="upper left" , bbox_to_anchor=(1,1))
plt.savefig("Pie_Challange_2.png")
plt.show()