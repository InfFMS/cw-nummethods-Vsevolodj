import matplotlib.pyplot as plt
fig, ax = plt.subplots() #create graph
ax.plot([0,0.0005],[0,0], label="0", color = "black")# create graph
# create constant
R = 8.314
b = 3.19*0.00001
a = 0.1382
Pnas = 3664186.998
V = [] #create V - massive with information about volume
i  = b+0.00001
while i <=0.001:
    V = V+[i]
    i+=0.0000001
T = -130+273.15
P = []  #create P - massive with information about press
for i in range(0,len(V)):
    P = P+[(R*T)/(V[i]-b)-a/(V[i]**2)-Pnas]
ax.plot(V, P, label="Graph")# create graph
ax.set_title("Van-der-Waals equation graph")
ax.set_ylabel("P, Pa", fontsize=10, color='black', labelpad=0)
ax.set_xlabel("V, m^3", fontsize=10, color='black', labelpad=0)
#creste function for solutions and squares
def P(V):
    return (R*T)/(V-b)-a/(V**2)-Pnas
def soluion(f, b1, b2):
    eps = 10**(-7)
    while b2-b1>2*eps:
        c = (b1+b2) / 2
        if f(b1)*f(c)<=0:
            b2=c
        else: b1=c
    return round(c,8)
def square(f,b1,b2):
    step = (b2-b1)/1000
    a = b1
    square = 0
    b = step
    while b<b1:
        square += (f(a) + f(b)) * (b - a) / 2
        a += step
        b += step
    return (square - (b1-b2)*f(b1))
first= 6.140625e-05
second= 9.984375e-05
third= 0.00019484375
print("Solutions")
print("First:",soluion(P,6*10**(-5),65*10**(-6)))
x = soluion(P,6*10**(-5),65*10**(-6))
plt.scatter(x,P(x), color = "red")
print("Third:",soluion(P,18*10**(-5),20*10**(-5)))
x = soluion(P,18*10**(-5),20*10**(-5))
plt.scatter(x,P(x), color = "red")
print("Square:")
print("First:", square(P,first,third), Pnas*(third-first))

print("As can be seen with good accuracy, the areas are equal")
plt.show()