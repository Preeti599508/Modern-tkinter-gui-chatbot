import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sales_data={
    "Product A":100,
    "Product B":200,
    "Product C":500,
    "Product D":600,
    "Product E":400
}

inventory_data={
    "Product A":150,
    "Product B":75,
    "Product C":150,
    "Product D":150,
    "Product E":150
}

product_data={
    "A":10,
    "B":40,
    "C":20,
    "D":30,
    "E":20
}

sales_month_data={
    "jan":200,
    "feb":300,
    "mar":800,
    "apr":1300,
    "may":900,
    "jun":900,
    "jul":700,
    "aug":1000,
    "sep":300,
    "oct":450,
    "nov":450,
    "dec":1300
}

plt.rcParams["axes.prop_cycle"]=plt.cycler(color=["purple","purple","purple","purple","purple"])
fig1,axl=plt.subplots()
axl.bar(sales_data.keys(),sales_data.values())
axl.set_title("Sales by product")
axl.set_xlabel("Product")
axl.set_ylabel("Sales")
plt.show()

fig2, ax2=plt.subplots()
ax2.barh(list(inventory_data.keys()),inventory_data.values())
ax2.set_title("Inventory of product")
ax2.set_xlabel("Inventory")
ax2.set_ylabel("Product")
plt.show()

fig3, ax3=plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys())
ax3.set_title("Product Breakdown")
plt.show()

fig4,ax4=plt.subplots()
ax4.plot(list(sales_month_data.keys()),sales_month_data.values())
ax4.set_title("Sales by month")
ax4.set_xlabel("Month")
ax4.set_ylabel("Sales")
plt.show()

fig5,ax5=plt.subplots()
ax5.fill_between(sales_month_data.keys(),sales_month_data.values())
ax5.set_title("Month Sales")
ax5.set_xlabel("Month")
ax5.set_ylabel("Sales")
plt.show()

root=tk.Tk()
root.title("Dashboard")
root.state("zoomed")

side_frame=tk.Frame(root,bg="#B4C2A85")
side_frame.pack(side="left",fill="y")

charts_frame=tk.Frame(root)
charts_frame.pack()
upper_frame=tk.Frame(charts_frame)
upper_frame.pack(fill="both",expand=True)

canvas1=FigureCanvasTkAgg(fig1,upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left",fill="both",expand=True)

canvas2=FigureCanvasTkAgg(fig2,upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left",fill="both",expand=True)

canvas3=FigureCanvasTkAgg(fig3,upper_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left",fill="both",expand=True)

lower_frame=tk.Frame(charts_frame)
lower_frame.pack(fill="both",expand=True)

canvas4=FigureCanvasTkAgg(fig4,lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side="left",fill="both",expand=True)

canvas5=FigureCanvasTkAgg(fig5,lower_frame)
canvas5.draw()
canvas5.get_tk_widget().pack(side="left",fill="both",expand=True)



 
root.mainloop()