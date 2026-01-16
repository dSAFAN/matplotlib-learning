import matplotlib.pyplot as plt

labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [15, 30, 45, 10]
explode_val = [0,0,0,0.1]

plt.figure(figsize=(6,6))

plt.pie(sizes ,shadow=True,explode=explode_val ,labels= labels , autopct='%1.1f%%',startangle=90)
plt.title("Fruit Composition")
plt.show()