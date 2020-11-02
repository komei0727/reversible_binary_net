import fredkin
import random
import numpy as np
import matplotlib.pyplot as plt

X = [[0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1,], [1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 1]]
p1 = p3 = p6 = p7 = 0.4
p2 = p4 = p5 = 0.6
P = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
lambda1 = lambda2 = lambda3 = lambda4 = lambda5 = lambda6 = lambda7 = 0
delta_E = np.zeros(5600)
p_1 = np.zeros(5600)
p_2 = np.zeros(5600)
p_3 = np.zeros(5600)
p_4 = np.zeros(5600)
p_5 = np.zeros(5600)
p_6 = np.zeros(5600)
p_7 = np.zeros(5600)

for epoch in range(200):
    for R in range(4):
        for p in range(7):
            
            Y = Y_1 = Y_2 = Y_3 = t_1 = t_2 = t_3 = t_4 = t_5 = 0
            for i in range(100):
                x1 = X[R][0]
                x2 = X[R][1]
                r1 = random.random()
                r2 = random.random()
                r3 = random.random()
                r4 = random.random()
                r5 = random.random()
                r6 = random.random() 
                r7 = random.random()

                if P[0] >= r1:
                    lambda1 = 1
                else:
                    lambda1 = 0
                if P[1] >= r2:
                    lambda2 = 1
                else:
                    lambda2 = 0
                if P[2] >= r3:
                    lambda3 = 1
                else:
                    lambda3 = 0
                if P[3] >= r4:
                    lambda4 = 1
                else:
                    lambda4 = 0
                if P[4] >= r5:
                    lambda5 = 1
                else:
                    lambda5 = 0
                if P[5] >= r6:
                    lambda6 = 1
                else:
                    lambda6 = 0
                if P[6] >= r7:
                    lambda7 = 1
                else:
                    lambda7 = 0
                c_1_1, b1_1_1, b2_1_1 = fredkin.fredkin(x1, lambda1, lambda2)
                c_1_2, b1_1_2, b2_1_2 = fredkin.fredkin(x2, lambda3, lambda4)
                c_1_3, b1_1_3, b2_1_3 = fredkin.fredkin(lambda5, lambda6, lambda7)

                c_2_1, b1_2_1, b2_2_1 = fredkin.fredkin(c_1_1, b1_1_2, b1_1_3)
                c_2_2, b1_2_2, b2_2_2 = fredkin.fredkin(c_1_2, b1_1_1, b2_1_3)
                c_2_3, b1_2_3, b2_2_3 = fredkin.fredkin(c_1_3, b2_1_1, b2_1_2)

                c_3_1, b1_3_1, b2_3_1 = fredkin.fredkin(b1_2_1, b1_2_2, c_2_3)
                c_3_2, b1_3_2, b2_3_2 = fredkin.fredkin(c_2_2, b2_2_1, b2_2_2)
                c_3_3, b1_3_3, b2_3_3 = fredkin.fredkin(b2_2_3, c_2_1, b1_2_3)

                c_4_1, b1_4_1, b2_4_1 = fredkin.fredkin(b2_3_1, b1_3_1, b1_3_2)
                c_4_2, b1_4_2, b2_4_2 = fredkin.fredkin(b1_3_3, c_3_2, b2_3_2)
                c_4_3, b1_4_3, b2_4_3 = fredkin.fredkin(b2_3_3, c_3_3, c_3_1)

                c_5_1, b1_5_1, b2_5_1 = fredkin.fredkin(c_4_1, b1_4_3, b2_4_2)
                c_5_2, b1_5_2, b2_5_2 = fredkin.fredkin(b2_4_1, b2_4_3, b1_4_2)
                c_5_3, b1_5_3, b2_5_3 = fredkin.fredkin(c_4_2, b1_4_1, c_4_3)

                Y += c_5_1
                Y_3 += b2_5_1
                Y_2 += c_5_3
                Y_1 += c_5_2
                t_1 += b1_5_1
                t_2 += b1_5_2
                t_3 += b2_5_2
                t_4 += b1_5_3
                t_5 += b2_5_3

            Y = Y / 100
            Y_1 = Y_1 / 100
            Y_2 = Y_2 / 100
            Y_3 = Y_3 / 100
            t_1 = t_1 / 100
            t_2 = t_2 / 100
            t_3 = t_3 / 100
            t_4 = t_4 / 100
            t_5 = t_5 / 100
            E = (Y-X[R][2])**2 
            #print(X[R][0], X[R][1], Y, Y_1, Y_2, Y_3, t_1, t_2, t_3, t_4, t_5, E)


            #print(lambda1, lambda2, lambda3, lambda4, lambda5, lambda6, lambda7)
            
            P[p] += 0.05
            
            Y = Y_1 = Y_2 = Y_3 = t_1 = t_2 = t_3 = t_4 = t_5 = 0
            for i in range(100):
                x1 = X[R][0]
                x2 = X[R][1]
                r1 = random.random()
                r2 = random.random()
                r3 = random.random()
                r4 = random.random()
                r5 = random.random()
                r6 = random.random() 
                r7 = random.random()

                if P[0] >= r1:
                    lambda1 = 1
                else:
                    lambda1 = 0
                if P[1] >= r2:
                    lambda2 = 1
                else:
                    lambda2 = 0
                if P[2] >= r3:
                    lambda3 = 1
                else:
                    lambda3 = 0
                if P[3] >= r4:
                    lambda4 = 1
                else:
                    lambda4 = 0
                if P[4] >= r5:
                    lambda5 = 1
                else:
                    lambda5 = 0
                if P[5] >= r6:
                    lambda6 = 1
                else:
                    lambda6 = 0
                if P[6] >= r7:
                    lambda7 = 1
                else:
                    lambda7 = 0
                c_1_1, b1_1_1, b2_1_1 = fredkin.fredkin(x1, lambda1, lambda2)
                c_1_2, b1_1_2, b2_1_2 = fredkin.fredkin(x2, lambda3, lambda4)
                c_1_3, b1_1_3, b2_1_3 = fredkin.fredkin(lambda5, lambda6, lambda7)

                c_2_1, b1_2_1, b2_2_1 = fredkin.fredkin(c_1_1, b1_1_2, b1_1_3)
                c_2_2, b1_2_2, b2_2_2 = fredkin.fredkin(c_1_2, b1_1_1, b2_1_3)
                c_2_3, b1_2_3, b2_2_3 = fredkin.fredkin(c_1_3, b2_1_1, b2_1_2)

                c_3_1, b1_3_1, b2_3_1 = fredkin.fredkin(b1_2_1, b1_2_2, c_2_3)
                c_3_2, b1_3_2, b2_3_2 = fredkin.fredkin(c_2_2, b2_2_1, b2_2_2)
                c_3_3, b1_3_3, b2_3_3 = fredkin.fredkin(b2_2_3, c_2_1, b1_2_3)

                c_4_1, b1_4_1, b2_4_1 = fredkin.fredkin(b2_3_1, b1_3_1, b1_3_2)
                c_4_2, b1_4_2, b2_4_2 = fredkin.fredkin(b1_3_3, c_3_2, b2_3_2)
                c_4_3, b1_4_3, b2_4_3 = fredkin.fredkin(b2_3_3, c_3_3, c_3_1)

                c_5_1, b1_5_1, b2_5_1 = fredkin.fredkin(c_4_1, b1_4_3, b2_4_2)
                c_5_2, b1_5_2, b2_5_2 = fredkin.fredkin(b2_4_1, b2_4_3, b1_4_2)
                c_5_3, b1_5_3, b2_5_3 = fredkin.fredkin(c_4_2, b1_4_1, c_4_3)

                Y += c_5_1
                Y_3 += b2_5_1
                Y_2 += c_5_3
                Y_1 += c_5_2
                t_1 += b1_5_1
                t_2 += b1_5_2
                t_3 += b2_5_2
                t_4 += b1_5_3
                t_5 += b2_5_3

            Y = Y / 100
            Y_1 = Y_1 / 100
            Y_2 = Y_2 / 100
            Y_3 = Y_3 / 100
            t_1 = t_1 / 100
            t_2 = t_2 / 100
            t_3 = t_3 / 100
            t_4 = t_4 / 100
            t_5 = t_5 / 100
            E_1 = (Y-X[R][2])**2 
            #print(X[R][0], X[R][1], Y, Y_1, Y_2, Y_3, t_1, t_2, t_3, t_4, t_5, E)


            #print(lambda1, lambda2, lambda3, lambda4, lambda5, lambda6, lambda7)
            
            P[p] -= 0.1
            
            Y = Y_1 = Y_2 = Y_3 = t_1 = t_2 = t_3 = t_4 = t_5 = 0
            for i in range(100):
                x1 = X[R][0]
                x2 = X[R][1]
                r1 = random.random()
                r2 = random.random()
                r3 = random.random()
                r4 = random.random()
                r5 = random.random()
                r6 = random.random() 
                r7 = random.random()

                if P[0] >= r1:
                    lambda1 = 1
                else:
                    lambda1 = 0
                if P[1] >= r2:
                    lambda2 = 1
                else:
                    lambda2 = 0
                if P[2] >= r3:
                    lambda3 = 1
                else:
                    lambda3 = 0
                if P[3] >= r4:
                    lambda4 = 1
                else:
                    lambda4 = 0
                if P[4] >= r5:
                    lambda5 = 1
                else:
                    lambda5 = 0
                if P[5] >= r6:
                    lambda6 = 1
                else:
                    lambda6 = 0
                if P[6] >= r7:
                    lambda7 = 1
                else:
                    lambda7 = 0
                c_1_1, b1_1_1, b2_1_1 = fredkin.fredkin(x1, lambda1, lambda2)
                c_1_2, b1_1_2, b2_1_2 = fredkin.fredkin(x2, lambda3, lambda4)
                c_1_3, b1_1_3, b2_1_3 = fredkin.fredkin(lambda5, lambda6, lambda7)

                c_2_1, b1_2_1, b2_2_1 = fredkin.fredkin(c_1_1, b1_1_2, b1_1_3)
                c_2_2, b1_2_2, b2_2_2 = fredkin.fredkin(c_1_2, b1_1_1, b2_1_3)
                c_2_3, b1_2_3, b2_2_3 = fredkin.fredkin(c_1_3, b2_1_1, b2_1_2)

                c_3_1, b1_3_1, b2_3_1 = fredkin.fredkin(b1_2_1, b1_2_2, c_2_3)
                c_3_2, b1_3_2, b2_3_2 = fredkin.fredkin(c_2_2, b2_2_1, b2_2_2)
                c_3_3, b1_3_3, b2_3_3 = fredkin.fredkin(b2_2_3, c_2_1, b1_2_3)

                c_4_1, b1_4_1, b2_4_1 = fredkin.fredkin(b2_3_1, b1_3_1, b1_3_2)
                c_4_2, b1_4_2, b2_4_2 = fredkin.fredkin(b1_3_3, c_3_2, b2_3_2)
                c_4_3, b1_4_3, b2_4_3 = fredkin.fredkin(b2_3_3, c_3_3, c_3_1)

                c_5_1, b1_5_1, b2_5_1 = fredkin.fredkin(c_4_1, b1_4_3, b2_4_2)
                c_5_2, b1_5_2, b2_5_2 = fredkin.fredkin(b2_4_1, b2_4_3, b1_4_2)
                c_5_3, b1_5_3, b2_5_3 = fredkin.fredkin(c_4_2, b1_4_1, c_4_3)

                Y += c_5_1
                Y_3 += b2_5_1
                Y_2 += c_5_3
                Y_1 += c_5_2
                t_1 += b1_5_1
                t_2 += b1_5_2
                t_3 += b2_5_2
                t_4 += b1_5_3
                t_5 += b2_5_3

            Y = Y / 100
            Y_1 = Y_1 / 100
            Y_2 = Y_2 / 100
            Y_3 = Y_3 / 100
            t_1 = t_1 / 100
            t_2 = t_2 / 100
            t_3 = t_3 / 100
            t_4 = t_4 / 100
            t_5 = t_5 / 100
            E_2 = (Y-X[R][2])**2 
            #print(X[R][0], X[R][1], Y, Y_1, Y_2, Y_3, t_1, t_2, t_3, t_4, t_5, E)


            #print(lambda1, lambda2, lambda3, lambda4, lambda5, lambda6, lambda7)
            
            if abs(E_2-E_1)<0.01:
                P[p] += 0.05
            elif E_2 > E_1:
                P[p] += 0.1
            if P[p] > 1:
                P[p] = 1
            if P[p] < 0:
                P[p] = 0
            print(P)
            delta_E[28*epoch+7*R+p] = abs(E_2-E_1)
            p_1[28*epoch+7*R+p] = P[0]
            p_2[28*epoch+7*R+p] = P[1]
            p_3[28*epoch+7*R+p] = P[2]
            p_4[28*epoch+7*R+p] = P[3]
            p_5[28*epoch+7*R+p] = P[4]
            p_6[28*epoch+7*R+p] = P[5]
            p_7[28*epoch+7*R+p] = P[6]

fig, ax = plt.subplots()

x = np.linspace(1,5600,5600)
c1,c2,c3,c4,c5,c6,c7 = "blue","green","red","black","yellow","grey","pink"
l1,l2,l3,l4,l5,l6,l7 = "p1","p2","p3","p4","p5","p6","p7"

ax.set_title("Transition of learning parameters", fontsize=18)
ax.set_xlabel("epoch", fontsize=18)
ax.set_ylabel("probability", fontsize=18)
ax.grid()
ax.plot(x, p_1, color=c1, label=l1)
ax.plot(x, p_2, color=c2, label=l2)
ax.plot(x, p_3, color=c3, label=l3)
ax.plot(x, p_4, color=c4, label=l4)
ax.plot(x, p_5, color=c5, label=l5)
ax.plot(x, p_6, color=c6, label=l6)
ax.plot(x, p_7, color=c7, label=l7)

ax.legend(loc=0, fontsize=16)
plt.show()