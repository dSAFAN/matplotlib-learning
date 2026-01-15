import matplotlib.pyplot as plt

r_hours = [1,2,3,5,6,7]
r_score =[50,55,65,75,80,85]

v_hours = [2,3,4,5,6,8]
v_score =[60,70,75,80,88,92]

plt.scatter(r_hours,r_score,color='red',marker='o',label='Reading')
plt.scatter(v_hours,v_score,color='blue',marker='^',label='Videos')
plt.title("Study Method Effectiveness")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(axis='both',linestyle='-.')
plt.legend(loc = 'best')
plt.savefig('Effective Study Method.png')
plt.show()