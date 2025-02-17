import matplotlib.pyplot as plt
fig, ax = plt.subplots()
R = 8.314
b = 3.19*0.00001
a = 0.1382
V = []
i  = b+0.00001
while i <=0.001:
    V = V+[i]
    i+=0.000001
T = -130+273.15
P = []
for i in range(0,len(V)):
    P = P+[(R*T)/(V[i]-b)-a/(V[i]**2)]
ax.plot(V, P, label="Graph")
ax.set_title("График уравнения Ван-дер-Ваальса")
ax.set_ylabel("P, Па", fontsize=10, color='black', labelpad=0)
ax.set_xlabel("V, м^3", fontsize=10, color='black', labelpad=0)
eps = 0.00001
v1 = 0.00006
v2 = 0.00008
while v2-v1>2*eps:
    mid1 = v1 + (v2 - v1) / 3
    mid2 = v2 - (v2 - v1) / 3
    if (R*T)/(mid1-b)-a/(mid1**2)<(R*T)/(mid2-b)-a/(mid2**2):
        v2=mid2
    else: v1=mid1
min = (v1+v2)/2
print(min)
plt.scatter(min,[(R*T)/(min-b)-a/(min**2)], color = "red")
v1 = 0.00008
v2 = 0.0002
while v2-v1>2*eps:
    mid1 = v1 + (v2 - v1) / 3
    mid2 = v2 - (v2 - v1) / 3
    if (R*T)/(mid1-b)-a/(mid1**2)>(R*T)/(mid2-b)-a/(mid2**2):
        v2=mid2
    else: v1=mid1
max = (v1+v2)/2
print(max)
plt.scatter(max,[(R*T)/(max-b)-a/(max**2)], color = "red")

# еще напишем щас счетчик длины
plt.show()
