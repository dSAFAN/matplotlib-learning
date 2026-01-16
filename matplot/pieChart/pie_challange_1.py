import matplotlib.pyplot as plt

items = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [15, 30, 45, 10]
custom_color = ['red','yellow','#99ff99','#ffb3e6']


plt.figure(figsize=(6,6))
plt.pie(sizes,autopct='%1.1f%%',labels=items,colors=custom_color,startangle=90,shadow=True)
plt.title("Challange 1")
plt.show()