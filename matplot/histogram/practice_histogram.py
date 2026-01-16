import matplotlib.pyplot as plt

# Histogram (Distribution)
# 1. Basic
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31]
data_set_2 = [15, 25, 35, 45, 55, 65, 10, 20, 30, 40, 50, 60, 5, 15]
exam_scores = [55, 60, 45, 80, 95, 100, 30, 40, 75, 78, 82, 85, 45, 33, 90, 92, 98, 50, 52, 60]
'''

plt.figure(figsize=(6,4))
plt.hist(data)
plt.title("Ex 1: Basic Histogram")
plt.show()
'''
# 2. Bin Tweak
'''
plt.figure(figsize=(6,4))
plt.hist(data, bins=5, color='skyblue' , edgecolor='black')
plt.title("Ex 2: Tweaking Bins & Edges")
plt.xlabel("Scores")
plt.ylabel("Count")
plt.show()
'''

# 3. Range focus
'''
plt.figure(figsize=(6,4))
plt.hist(data,bins=5,color='salmon',edgecolor = 'black' ,range=(0,50))
plt.title("Ex 3: Focused Range (0-50 only)")
plt.show()
'''

# 4. Overlay two histograms to compare distributions
'''
plt.figure(figsize=(6,4))
plt.hist(data , bins=5 , alpha = 0.5 , label='Book Data')
plt.hist(data_set_2 , bins=5 , alpha = 0.5 , label='New Data')

plt.title('Ex 4: Comparing Two Groups')
plt.legend()
plt.show()
'''

# 5
'''
plt.hist(exam_scores,bins=[0,20,40,60,80,100])
plt.show()
'''
'''
plt.figure(figsize=(8,5))
plt.hist(data,bins=5,range=(0,50),color='skyblue',edgecolor = 'black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
'''

plt.figure(figsize=(10,5))
plt.hist(data, bins=10,edgecolor = 'black', alpha=0.5, color='blue', label='Book Data (High)')
plt.hist(data_set_2, bins=10, alpha=0.5,edgecolor = 'black' , color='orange', label='New Data (Low)')

plt.legend()
plt.title("Comparison: Book Data vs. New Data")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()