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
T = -130+273.15
P = [] #create P - massive with information about press
for i in range(0,len(V)):
    P = P+[(R*T)/(V[i]-b)-a/(V[i]**2)]
ax.plot(V, P, label="Graph") # create graph
ax.set_title("Van-der-Waals equation graph")
ax.set_ylabel("P, Pa", fontsize=10, color='black', labelpad=0)
ax.set_xlabel("V, m^3", fontsize=10, color='black', labelpad=0)
eps = 0.00001 #set the exactness
v1 = 0.00006 # set the left border
v2 = 0.00008 # set the right border
while v2-v1>2*eps:#find min
    mid1 = v1 + (v2 - v1) / 3
    mid2 = v2 - (v2 - v1) / 3
    if (R*T)/(mid1-b)-a/(mid1**2)<(R*T)/(mid2-b)-a/(mid2**2):
        v2=mid2
    else: v1=mid1
min = (v1+v2)/2
print(min)
plt.scatter(min,[(R*T)/(min-b)-a/(min**2)], color = "red")
v1 = 0.00008# set the new left border
v2 = 0.0002# set the new right border
while v2-v1>2*eps:#find max
    mid1 = v1 + (v2 - v1) / 3
    mid2 = v2 - (v2 - v1) / 3
    if (R*T)/(mid1-b)-a/(mid1**2)>(R*T)/(mid2-b)-a/(mid2**2):
        v2=mid2
    else: v1=mid1
max = (v1+v2)/2
print(max)
plt.scatter(max,[(R*T)/(max-b)-a/(max**2)], color = "red")

plt.show()
