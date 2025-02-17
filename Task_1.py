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
P=[]
T = -140+273.15
while T <=-100+273.15:
    P = []
    for i in range(0,len(V)):
        P = P+[(R*T)/(V[i]-b)-a/(V[i]**2)]
    ax.plot(V, P, label="Graph")
    T+=10
ax.set_title("График уравнения Ван-дер-Ваальса")
ax.set_ylabel("P, Па", fontsize=10, color='black', labelpad=0)
ax.set_xlabel("V, м^3", fontsize=10, color='black', labelpad=0)
plt.show()