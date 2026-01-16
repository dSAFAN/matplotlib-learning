import matplotlib.pyplot as plt

items = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [15, 30, 45, 10]

plt.figure(figsize=(6,6))
plt.pie(sizes,labels=items,autopct='%1.1f%%',wedgeprops={'width':0.3,'edgecolor':'white'})
plt.title("Pie Challange 2")
plt.show()