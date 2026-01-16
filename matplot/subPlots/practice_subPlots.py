import matplotlib.pyplot as plt

# --- DATA PREP ---
# Data 1: Ages (for Histogram)
ages = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31]

# Data 2: Fruits (for Pie)
labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [15, 30, 45, 10]
colors = ['silver', 'silver', 'red', 'silver'] # Highlighting Cherry
exp =(0,0,0.1,0) 

# --- THE DASHBOARD SETUP ---
# "1, 2" means: 1 Row, 2 Columns (Side-by-Side)
# figsize=(12, 5): Widescreen to fit two charts

fig , (ax1 , ax2) = plt.subplots(1,2 , figsize=(12,5))

# --- PANEL 1: The Histogram ---
# we use 'ax1.hist', NOT 'plt.hist'

ax1.hist(ages ,bins=5 , color ='skyblue' , edgecolor = 'black' )
ax1.set_title("User Age Distribution") # Note: .set_title(), not .title()
ax1.set_xlabel("Age")
ax1.set_ylabel("Count")

# --- PANEL 2: The Pie Chart ---
# Notice we use 'ax2.pie'
ax2.pie(sizes , labels = labels , autopct = '%1.1f%%' , explode = exp ,
        startangle = 90 , shadow = True , colors = colors ,
        wedgeprops = {'edgecolor' : 'white' , 'linewidth' : 2})
ax2.set_title("Fruit Sales Composition")

# --- FINAL POLISH ---
plt.suptitle("Executive Dashboard: Q1 Report", fontsize=16, fontweight='bold')
plt.tight_layout() # Adjusts spacing so panels don't overlap
plt.show()