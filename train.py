import numpy as np
import random
import Layer

X_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
X_label = np.array([0, 1, 1, 0])
# X_input = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
# X_label = np.array([0, 1, 1, 0, 1, 0, 0, 1])


for k in range(20):
    model = Layer.Sequential(layers=[])
    model.addlayer(Layer.ANDLayer(3, 8))
    model.addlayer(Layer.ANDLayer(8, 16))
    model.addlayer(Layer.ANDLayer(16, 16))
    model.addlayer(Layer.ANDLayer(16, 16))
    model.addlayer(Layer.ANDLayer(16, 16))
    model.addlayer(Layer.ANDLayer(16, 16))
    model.addlayer(Layer.ANDLayer(16, 16))
    model.addlayer(Layer.ANDLayer(16, 16))
    model.addlayer(Layer.ANDLayer(16, 16))
    model.addlayer(Layer.ANDLayer(16, 16))
    classifier = Layer.Classifier(model)

    for epoch in range(1000):
        number = random.randint(0, len(X_label)-1)
        x = X_input[number]
        t = X_label[number]
        classifier.update(x, t)

    loss = 0
    for i in range(len(X_label)):
        number = i
        x = X_input[i]
        t = X_label[i]
        y = classifier.test(x)
        loss = loss + ((y - t)**2 / 2)
    loss = loss / 4
    if loss < 0.0001:
        print('{}回目成功'.format(k+1))
        classifier.save_param()
