import matplotlib.pyplot as plt


# Study Hours Effects Exam Scores (True)
study_hours = [1,2,3,4,5,6,7,8]
exam_score = [55,60,65,70,72,85,88,95]

plt.scatter(study_hours , exam_score , marker = "*" , s = 100)
plt.title("Study Hours vs. Grades")
plt.xlabel("Hours")
plt.ylabel("Score")
plt.grid(axis='y', linestyle = '--')
plt.show()


# High Speed Reduces Fuel Efficiency (True)

Speed = [40,50,60,70,80,90,100,110,120]
fuel = [18,17,16,15,14,12,10,8,6]

plt.scatter(Speed , fuel , color = 'red' , marker = 'x' , s = 150)
plt.title("Speed vs. Fuel Efficiency")
plt.xlabel("Speed (km/h)")
plt.ylabel("Fuel Efficiency (km/L)")
plt.grid(axis='both',linestyle = '--')
plt.show()


# Multiple Groups Plotting
Dog_weight = [20,25,30,35,40]
Dog_height = [50,55,60,65,70]

Cat_weight = [4,5,6,7,8]
Cat_height = [25,28,30,32,35]

plt.scatter(Dog_weight,Dog_height,color='blue',label='Dogs',marker='o')
plt.scatter(Cat_weight,Cat_height,color='orange',label='Cats',marker='o')

plt.title("Pet Sizes: Dogs vs. Cats")
plt.xlabel("Weight")
plt.ylabel("Height")
plt.grid(axis='both',linestyle='-.')
plt.legend()
plt.show()