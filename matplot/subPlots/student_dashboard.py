import matplotlib.pyplot as plt
scores = [55, 60, 45, 80, 95, 100, 30, 40, 75, 78, 82, 85, 90, 92, 98]
score_cd = [0,20,40,60,80,100]
sizes = [12,3]
labels = ['Pass' ,'Fail']
colors = ['green' , 'red']

fig , axs = plt.subplots(1,2 , figsize =(12,12))

axs[0].hist(scores , bins = score_cd , color = 'pink' , edgecolor = 'black' )
axs[0].set_title("Marks distribution")
axs[0].set_ylabel("Count")
axs[0].set_xlabel("Marks")
axs[0].grid(True , linestyle = '--' , alpha = 0.5)

axs[1].pie(sizes, labels = labels , colors = colors , shadow = True ,
           wedgeprops = {'edgecolor': 'white','linewidth': 1} ,
           autopct = '%1.1f%%' , startangle = 90 , labeldistance = None)
axs[1].set_title("Pass vs. Fail Percentage")

plt.suptitle("Student Performance Dashbaord" , fontsize = 16 , fontweight = 'bold')
plt.tight_layout
plt.legend(title = "Qualification\nPattern" , loc ="upper left" , bbox_to_anchor=(1,1))
plt.savefig("Student_dashboard.png" , dpi = 300 , bbox_inches = 'tight')
plt.show()