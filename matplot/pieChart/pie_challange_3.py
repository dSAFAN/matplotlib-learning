import matplotlib.pyplot as plt

items = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [15, 30, 45, 10]
item_color = ['#d3d3d3','#d3d3d3','#ff0000' ,'#d3d3d3']
explode_list = [0,0,0.1,0]
plt.figure(figsize=(7,5))
plt.pie(
    sizes,autopct='%1.1f%%',
    startangle=90 ,explode=explode_list,
    shadow=True, colors=item_color,
    labeldistance = None, labels=items ,
    wedgeprops={'edgecolor': 'white' , 'linewidth': 1})
plt.legend(title = "Fruit Types" , loc ="upper left" , bbox_to_anchor=(1,1))
plt.tight_layout(rect=[0,0,1,0.95])
plt.title("Pie Challange 3")
plt.savefig("Pie_Challange_3.png")
plt.show()
