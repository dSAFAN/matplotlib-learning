import matplotlib.pyplot as plt

# Driver A: Mostly consistent (around 40-50 mins)
driver_a = [45, 48, 42, 47, 46, 44, 49, 41, 45, 43, 48, 52, 40, 46, 47]

# Driver B: Wildly variable (some fast, some slow, some outliers)
driver_b = [25, 30, 28, 32, 65, 70, 22, 29, 31, 26, 68, 72, 27, 33, 110]

plt.figure(figsize=(10,10))
plt.hist(driver_a ,label= "Driver A" ,range=(0,80), bins=8 , color='green' , alpha = 0.5 , edgecolor = 'black')
plt.hist(driver_b ,label= "Driver B" , range=(0,80), bins=8 , color='purple' , alpha = 0.5 , edgecolor = 'black')
plt.title("Driver A vs. Driver B" , fontsize = 16 , fontweight = 'bold')
plt.xlabel("Minutes")
plt.ylabel("Deliveries")
plt.grid(True,linestyle='--',alpha=0.4)
plt.legend()
plt.savefig('hist_capstone.png')
plt.show()