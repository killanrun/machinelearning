import numpy as np
import pygame
from collections import deque
import random

#pygame.init()
#world = pygame.display.set_mode((100,100))



def sigmoid(x, differentiate=False):
    if differentiate:
        return x * (1-x)
    else:
        return 1/(1 + np.exp(-x))


def relu(x, differentiate=False):
    if differentiate:
        return np.greater(x, 0).astype(int)
    else:
        return np.maximum(0, x)

class Layer:
    def __init__(self, shape, act):
        self.shape = shape
        self.data = np.zeros(self.shape)
        self.act = act

    def activate(self):
        if self.act == 'sigmoid':
            self.data = sigmoid(self.data)
        elif self.act == 'relu':
            self.data = relu(self.data)

class Network:
    def __init__(self, layers):
        self.layers = layers
        self.weights = []
        self.error = 0
        self.generate_weights()

    def generate_weights(self):
        for layer in range(len(self.layers)):
            if self.layers[layer] != self.layers[-1]:
                w = np.full((self.layers[layer].shape[0], self.layers[layer+1].shape[0]), 0.5)
                self.weights.append(w)

    def transfer(self, inputs):

        self.layers[0].data = inputs
        for layer in range(len(self.layers)-1):
            z = np.dot(self.weights[layer].T, self.layers[layer].data)
            self.layers[layer+1].data = z
            self.layers[layer+1].activate()

    def mean_square_error(self, targets):
        outputs = self.layers[-1].data
        diff = targets - outputs
        square = diff*diff
        self.error = square
        return square

    def train(self, targets):
        output_network = self.layers[-1].data
        output_error = self.mean_square_error(targets)
        tmp = output_error * sigmoid(output_network, differentiate=True)
        val = 0.05 * np.dot(tmp.reshape(1,-1).T, self.layers[-2].data.reshape(-1,1).T)
        self.weights[-1] += val.T
        hidden_errors = np.dot(self.weights[-1], output_error)
        tmp = hidden_errors * relu(self.layers[-2].data, differentiate=True)
        self.weights[-2] += 0.05 * np.dot(tmp.reshape(1,-1), self.layers[-3].data.reshape(-1,1))


class Memory:
    def __init__(self, length):
        self.length = length
        self.memory = deque(maxlen=self.length)

    def sample(self, size):
        return random.sample(self.memory, size)

    def add(self, itemslist):
        self.memory.append(itemslist)

class Agent(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.memory = Memory(4096)
        self.network = Network([Layer((100,100), None),Layer((100,100), 'relu'),Layer((5,1), 'sigmoid')])
        self.actions = [[0,0],[1,0],[0,1],[1,1]]
        self.environment = pygame.surfarray.array2d(world)
        self.reward = 0
        self.image = pygame.Surface((10,10))
        self.image.fill(pygame.color.Color('Black'))
        self.rect = self.image.get_rect()
    def move(self, action):
        if self.rect.centerx > 100:
            self.rect.centerx -= 10
        elif self.rect.centerx <0:
            self.rect.centerx += 10
        if self.rect.centery > 100:
            self.rect.centery -= 10
        elif self.rect.centery <0:
            self.rect.centery += 10
        else:
            self.rect.move_ip(action[0],action[1])
'''
a1 = Agent((0,0))

agents = pygame.sprite.Group()
agents.add(a1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False


    world.fill(pygame.color.Color("White"))
    agents.draw(world)


    a1.network.transfer(np.random.random(10000).reshape(100,100))
    print(a1.network.layers[-1].data)
    a1.move(a1.actions[np.argmax(a1.network.layers[-1].data)])


    pygame.display.update()


'''







