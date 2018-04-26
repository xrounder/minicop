import numpy
import scipy.special
import random
import matplotlib.pyplot as plt
import math

#https://stackoverflow.com/questions/32105954/how-can-i-write-a-binary-array-as-an-image-in-python

class neuralNetwork:

    def __init__(self, inputNodes, hiddenNodes, outputNodes, learningRate):
        self.inputNodes = inputNodes
        self.hiddenNodes = hiddenNodes
        self.outputNodes = outputNodes
        self.learningRate = learningRate

        self.weightsHidden = (numpy.random.rand(self.hiddenNodes, self.inputNodes) - 0.5)
        self.weightsOutput = (numpy.random.rand(self.hiddenNodes, self.outputNodes) - 0.5)
        #self.weightsHidden = (numpy.range(1,1))


        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    def train(self, input_list, target_list):

        inputs = numpy.array(input_list, ndmin=2).T
        targets =  numpy.array(target_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.weightsHidden,inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.weightsOutput.T,hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.weightsOutput, output_errors)

        self.weightsOutput += self.learningRate * numpy.dot((output_errors*final_outputs*(1.0 - final_outputs)), hidden_outputs.T).T
        self.weightsHidden += self.learningRate * numpy.dot(hidden_errors*hidden_outputs*(1.0 - hidden_outputs),numpy.transpose(inputs))

    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.weightsHidden, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.weightsOutput.T,hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs

if __name__ == "__main__":
    n = neuralNetwork(2,4,1,0.5)

    max = 9
    #training
    print("training Net ... \n")
    for i in range(10000):

        for x in range(max):
            #for y in range(max):
                valX = x/10
                valY = valX

                #Pythagoras
                valZ = (valX*valX)+(valY*valY)
                result = math.sqrt(valZ)

                if result <= 1:
                    #print("BIGGER 1 ",result)
                    #n.train([valX,valY],[0])
                    #print("SMALLER 1 ",result)
                    n.train([valX,valY],[0.8])
                    #n.train([valX*-1,valY*-1],[0.8])
                    #n.train([valX*-1,valY],[0.8])
                    #n.train([valX,valY*-1],[0.8])
                else:
                    n.train([valX,valY],[0.1])
                    #n.train([valX * -1, valY * -1], [0.1])
                    #n.train([valX*-1,valY],[0.1])
                    #n.train([valX, valY*-1], [0.1])




    for x in range(-max,max):
        for y in range(-max,max):

            result = n.query([x/10, y/10])
            print("X ",x/10," Y ",y/10,result)
            if (result >= 0.7 and result <= 0.89):
                plt.plot([x/10], [y/10], marker='o', markersize=2, color="red")
            else:
                plt.plot([x/10], [y/10], marker='o', markersize=2, color="black")

    plt.ylabel('y')
    plt.show()

