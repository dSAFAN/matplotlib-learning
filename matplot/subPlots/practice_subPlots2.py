import matplotlib.pyplot as plt

# --- DATA PREP ---
# Data 1: Ages (for Histogram)
ages = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31]

# Data 2: Fruits (for Pie)
labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [15, 30, 45, 10]
colors = ['silver', 'silver', 'red', 'silver'] # Highlighting Cherry
exp =(0,0,0.1,0) 

fig , (ax1 , ax2) = plt.subplots(2,1 , figsize = (6,10))

ax1.hist(ages , bins=[0,10,20,30,40,50,60,70,80,90],
         color = 'skyblue' , edgecolor = 'black')
ax1.set_title("User Age Distribution")
ax1.set_xlabel("Age")
ax1.set_ylabel("Count")

ax2.pie(sizes , labels = labels , autopct = '%1.1f%%' ,
        colors = colors , explode = exp , startangle = 90 ,
        shadow = True , 
        wedgeprops = {'edgecolor' : 'white' , 'linewidth' : 2})
ax2.set_title("Fruit Sales Composition")

plt.suptitle("Executive Dashboard: Q2 Report", fontsize=16, fontweight='bold')
plt.tight_layout(h_pad=3.0, rect=[0, 0, 1, 0.95])
plt.show()