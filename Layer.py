import numpy as np
import random

path_w = 'result/param.txt'


class Layer(object):
    def __init__(self, lr=0.1):
        self.params = {}
        self.grads = {}
        self.lr = lr

    def update(self):
        for k in self.params.keys():
            self.params[k] = self.params[k] - self.lr * self.grads[k]
            for i in range(len(self.params[k])):
                if self.params[k][i] > 1.0 or self.params[k][i] < 0.0:
                    self.params[k][i] = self.params[k][i] + \
                        self.lr*self.grads[k][i]

    def zerograd(self):
        for k in self.params.keys():
            self.grads[k] = np.zeros(
                shape=self.params[k].shape, dtype=self.params[k].dtype)


class Sequential:
    def __init__(self, layers=[]):
        self.layers = layers

    def addlayer(self, layer):
        self.layers.append(layer)

    def forward(self, x):
        for l in self.layers:
            x = l.forward(x)
        return x

    def backward(self, y):
        for l in reversed(self.layers):
            y = l.backward(y)
        return y

    def update(self):
        for l in self.layers:
            l.update()

    def zerograd(self):
        for l in self.layers:
            l.zerograd()

    def print_param(self):
        for l in self.layers:
            l.print_param()

    def save_param(self):
        for l in self.layers:
            l.save_param()


class ANDLayer(Layer):
    def __init__(self, input_dim, output_dim):
        super(ANDLayer, self).__init__()

        self.params['p'] = np.random.rand(int(output_dim/2))
        self.shuffle = random.sample(range(input_dim*3), k=output_dim)
        self.x_mid = np.zeros(input_dim*3)
        self.x_out = np.zeros(output_dim)
        self.grads['p'] = np.zeros(int(output_dim/2))
        self.grads['X'] = np.zeros(input_dim)
        # print(self.params['p'])
        # print(self.shuffle)

    def forward(self, x):
        self.x = x
        for i in range(len(x)):
            self.x_mid[i*3] = x[i]
            self.x_mid[i*3+1] = x[i]
            self.x_mid[i*3+2] = 1 - x[i]

        for i in range(int(len(self.x_out)/2)):
            self.x_out[i*2] = self.params['p'][i]*self.x_mid[self.shuffle[i*2]] + self.x_mid[self.shuffle[i*2]] * \
                self.x_mid[self.shuffle[i*2+1]] - self.params['p'][i] * \
                self.x_mid[self.shuffle[i*2]]*self.x_mid[self.shuffle[i*2+1]]
            self.x_out[i*2+1] = (1-self.params['p'][i])*self.x_mid[self.shuffle[i*2]
                                                                   ] + self.params['p'][i]*self.x_mid[self.shuffle[i*2+1]]

        # print(self.x_out)
        return self.x_out

    def backward(self, y):
        for i in range(int(len(self.x_out)/2)):
            self.grads['p'][i] = y[i*2]*(self.x_mid[self.shuffle[i*2]]*(1-self.x_mid[self.shuffle[i*2+1]])) + \
                y[i*2+1]*(self.x_mid[self.shuffle[i*2+1]] -
                          self.x_mid[self.shuffle[i*2]])

        # print(self.grads['p'])
        grad_Xmid = np.zeros(len(self.x_mid))

        for i in range(int(len(self.x_out)/2)):
            grad_Xmid[self.shuffle[i*2]] = y[i*2]*(self.params['p'][i]+self.x_mid[self.shuffle[i*2+1]] -
                                                   self.params['p'][i]*self.x_mid[self.shuffle[i*2+1]]) + y[i*2+1]*(1-self.params['p'][i])
            grad_Xmid[self.shuffle[i*2+1]] = y[i*2]*(self.x_mid[self.shuffle[i*2]]-self.params['p']
                                                     [i]*self.x_mid[self.shuffle[i*2]]) + y[i*2+1]*self.params['p'][i]

        for i in range(len(self.x)):
            self.grads['X'][i] = grad_Xmid[i*3] + \
                grad_Xmid[i*3+1] - grad_Xmid[i*3+2]

        # print(self.grads['X'])
        return self.grads['X']

    def print_param(self):

        print(self.shuffle)
        print(self.params['p'])
        print('---------------------------------------------------')

    def save_param(self):
        shuffle_str = [str(n) for n in self.shuffle]
        param_str = [str(n) for n in self.params['p']]
        with open(path_w, mode='a') as f:
            f.write('[' + ','.join(shuffle_str) + ']\n')
            f.write('[' + ','.join(param_str) + ']\n')
            f.write(
                '----------------------------------------------------------------\n')


class Classifier:
    def __init__(self, model):
        self.model = model

    def update(self, x, t):
        self.model.zerograd()
        y = self.model.forward(x)
        loss = (y[0] - t)**2 / 2
        # print(loss)
        dout = np.zeros(len(y))
        dout[0] = y[0] - t
        dout = self.model.backward(dout)
        self.model.update()

    def test(self, x):
        y = self.model.forward(x)
        return y[0]

    def print_param(self):
        self.model.print_param()

    def save_param(self):
        self.model.save_param()
        with open(path_w, mode='a') as f:
            f.write('\n')
