def binary_net(X,shuffle):
    import fredkin
    import random
    import numpy as np

    layer_num = len(shuffle) 
    X = np.array(X)

    Y = np.zeros((layer_num+1,len(X)))
    for i in range(int(len(X)/3)):
        Y[0][3*i], Y[0][3*i+1], Y[0][3*i+2] = fredkin.fredkin(X[3*i], X[3*i+1], X[3*i+2])
    for l in range(layer_num):
        Y_shuffle = Y[l][shuffle[l]]
        for i in range(int(len(X)/3)):
            Y[l+1][3*i], Y[l+1][3*i+1], Y[l+1][3*i+2] = fredkin.fredkin(Y_shuffle[3*i], Y_shuffle[3*i+1], Y_shuffle[3*i+2])
    
    return Y[layer_num]
    
