import matplotlib.pyplot as plt
fig, ax = plt.subplots() #create graph
# create constant
R = 8.314
b = 3.19*0.00001
a = 0.1382
V = [] #create V - massive with information about volume
i  = b+0.00001
while i <=0.001:
    V = V+[i]
    i+=0.000001
P=[] #create P - massive with information about press
T = -140+273.15
while T <=-100+273.15:
    P = []
    for i in range(0,len(V)):
        P = P+[(R*T)/(V[i]-b)-a/(V[i]**2)]
    ax.plot(V, P, label="Graph") # create graphs
    T+=10
ax.set_title("Van-der-Waals equation graph")
ax.set_ylabel("P, Pa", fontsize=10, color='black', labelpad=0)
ax.set_xlabel("V, m^3", fontsize=10, color='black', labelpad=0)
plt.show()