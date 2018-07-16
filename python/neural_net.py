import numpy as np
import os
import random

INPUT_LENGTH = 196608
LAYER_TWO_LENGTH = 50
LAYER_THREE_LENGTH = 25
OUTPUT_LENGTH = 5
MAX_WEIGHT = 2
MAX_BIAS = 2



class snap_nn:

    #Creates all of the arrays for storing weights and biases, all initialized to 0
    def __init__(self):
        self.inputs_to_layer2_w = np.zeros((LAYER_TWO_LENGTH, INPUT_LENGTH))
        self.inputs_to_layer2_b = np.zeros((LAYER_TWO_LENGTH))
        
        self.layer2_to_layer3_w = np.zeros((LAYER_THREE_LENGTH, LAYER_TWO_LENGTH))
        self.layer2_to_layer3_b = np.zeros((LAYER_THREE_LENGTH))
        
        self.layer3_to_output_w = np.zeros((OUTPUT_LENGTH, LAYER_THREE_LENGTH))
        self.layer3_to_output_b = np.zeros((OUTPUT_LENGTH))

    #Gives every weight and bias in the nn a random value within the range of MAX values
    def random_values(self):
        random.seed()
        for i in range(LAYER_TWO_LENGTH):
            for j in range(INPUT_LENGTH):
                self.inputs_to_layer2_w[i,j] = self.random_weight()
            self.inputs_to_layer2_b[i] = self.random_bias()
        for i in range(LAYER_THREE_LENGTH):
            for j in range(LAYER_TWO_LENGTH):
                self.layer2_to_layer3_w[i,j] = self.random_weight()
            self.layer2_to_layer3_b[i] = self.random_bias()
        for i in range(OUTPUT_LENGTH):
            for j in range(LAYER_THREE_LENGTH):
                self.layer3_to_output_w[i,j] = self.random_weight()
            self.layer3_to_output_b[i] = self.random_bias()

    #Saves every weight/bias value in the neural network to a text file named based on the current generation and child
    def save_nn(self, gen, child):
        filename = "g"+str(gen)+"c"+str(child)+".txt"
        foldername = "saves/"+"two"+str(LAYER_TWO_LENGTH)+"three"+str(LAYER_THREE_LENGTH)+"out"+str(OUTPUT_LENGTH)+"weight"+str(MAX_WEIGHT)+"bias"+str(MAX_BIAS)
        if not os.path.exists(foldername):
            os.makedirs(foldername)
        with open(foldername+"/"+filename, 'w') as f:
            for i in range(LAYER_TWO_LENGTH):
                for j in range(INPUT_LENGTH):
                    f.write(str(self.inputs_to_layer2_w[i,j])+"\n")
            for i in range(LAYER_TWO_LENGTH):     
                f.write(str(self.inputs_to_layer2_b[i])+"\n")
            for i in range(LAYER_THREE_LENGTH):
                for j in range(LAYER_TWO_LENGTH):
                    f.write(str(self.layer2_to_layer3_w[i,j])+"\n")
            for i in range(LAYER_THREE_LENGTH):
                f.write(str(self.layer2_to_layer3_b[i])+"\n")
            for i in range(OUTPUT_LENGTH):
                for j in range(LAYER_THREE_LENGTH):
                    f.write(str(self.layer3_to_output_w[i,j])+"\n")
            for i in range(OUTPUT_LENGTH):
                f.write(str(self.layer3_to_output_b[i])+"\n")

    #Loads a neural network from a file name based on the save_nn() structure. Every value in current neural network
    #is changed to the respective one in the loaded nn
    def load_nn_from_file(self, gen, child):
        filename = "g"+str(gen)+"c"+str(child)+".txt"
        foldername = "saves/"+"two"+str(LAYER_TWO_LENGTH)+"three"+str(LAYER_THREE_LENGTH)+"out"+str(OUTPUT_LENGTH)+"weight"+str(MAX_WEIGHT)+"bias"+str(MAX_BIAS)
        with open(foldername+"/"+filename, 'r') as f:
            lines = f.readlines()
            pro = 0
            for i in range(LAYER_TWO_LENGTH):
                for j in range(INPUT_LENGTH):
                    self.inputs_to_layer2_w[i,j] = lines[pro]
                    pro = pro + 1
            for i in range(LAYER_TWO_LENGTH):     
                self.inputs_to_layer2_b[i] = lines[pro]
                pro = pro + 1   
            for i in range(LAYER_THREE_LENGTH):
                for j in range(LAYER_TWO_LENGTH):
                    self.layer2_to_layer3_w[i,j] = lines[pro]
                    pro = pro + 1
            for i in range(LAYER_THREE_LENGTH):
                self.layer2_to_layer3_b[i] = lines[pro]
                pro = pro + 1
            for i in range(OUTPUT_LENGTH):
                for j in range(LAYER_THREE_LENGTH):
                    self.layer3_to_output_w[i,j] = lines[pro]
                    pro = pro + 1
            for i in range(OUTPUT_LENGTH):
                self.layer3_to_output_b[i] = lines[pro]
                pro = pro + 1
                
    #Returns Random Weight Value in range -MAX_WEIGHT to MAX_WEIGHT              
    def random_weight(self):
        return (random.random()-0.5)*(MAX_WEIGHT*2)

    #Returns Random Bias Value in range -MAX_BIAS to MAX_BIAS   
    def random_bias(self):
        return (random.random()-0.5)*(MAX_BIAS*2)

    #Squishes the input down to a value between 0 and 1
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    #Getters and setters for weights and biases
    def assign_layer2_weights(self, new_w):
        self.inputs_to_layer2_w = new_w

    def l2w(self):
        return self.inputs_to_layer2_w

    def assign_layer2_biases(self, new_b):
        self.inputs_to_layer2_b = new_b

    def l2b(self):
        return self.inputs_to_layer2_b

    def assign_layer3_weights(self, new_w):
        self.layer2_to_layer3_w = new_w

    def l3w(self):
        return self.layer2_to_layer3_w

    def assign_layer3_biases(self, new_b):
        self.layer2_to_layer3_b = new_b

    def l3b(self):
        return self.layer2_to_layer3_b

    def assign_output_weights(self, new_w):
        self.layer3_to_output_w = new_w

    def ow(self):
        return self.layer3_to_output_w

    def assign_output_biases(self, new_b):
        self.layer3_to_output_b = new_b

    def ob(self):
        return self.layer3_to_output_b

    #Calculates the activation value for every node
    def activations(self):
        self.layer2_a = np.dot(self.inputs_to_layer2_w, self.img_array_a) + self.inputs_to_layer2_b
        for i in range(LAYER_TWO_LENGTH):
            self.layer2_a[i] = self.sigmoid(self.layer2_a[i])
        self.layer3_a = np.dot(self.layer2_to_layer3_w, self.layer2_a) + self.layer2_to_layer3_b
        for i in range(LAYER_THREE_LENGTH):
            self.layer3_a[i] = self.sigmoid(self.layer3_a[i])
        self.output_a = np.dot(self.layer3_to_output_w, self.layer3_a) + self.layer3_to_output_b
        for i in range(OUTPUT_LENGTH):
            self.output_a[i] = self.sigmoid(self.output_a[i])
            
    #Returns Chosen Output Index, Chosen Output Value, All Output Values
    def get_output(self, img):
        self.img_array_a = img.flatten()
        self.activations()
        return (np.argmax(self.output_a),np.amax(self.output_a), self.output_a)

    #Returns child neural network   
    def breed(self, mate):
        random.seed()
        new_inputs_to_layer2_w = np.zeros((LAYER_TWO_LENGTH, INPUT_LENGTH))
        new_inputs_to_layer2_b = np.zeros((LAYER_TWO_LENGTH))
        
        new_layer2_to_layer3_w = np.zeros((LAYER_THREE_LENGTH, LAYER_TWO_LENGTH))
        new_layer2_to_layer3_b = np.zeros((LAYER_THREE_LENGTH))
        
        new_layer3_to_output_w = np.zeros((OUTPUT_LENGTH, LAYER_THREE_LENGTH))
        new_layer3_to_output_b = np.zeros((OUTPUT_LENGTH))
        #Random:
        #1 = New Random Value
        #5 = Mutated Self Value
        #8 = Mutated Mate Value
        # 2,4,9 = Mate Value
        # 3,6,7,10 = Self Value

        #Layer 2
        for i in range(LAYER_TWO_LENGTH):
            for j in range(INPUT_LENGTH):
                #Input Layer to Layer 2 Weights
                rand = random.randint(1,10)
                if rand == 1:
                    new_inputs_to_layer2_w[i,j] = self.random_weight()
                elif rand == 5:
                    new_inputs_to_layer2_w[i,j] = mate.l2w()[i,j] + self.random_weight()
                elif rand == 8:
                    new_inputs_to_layer2_w[i,j] = self.inputs_to_layer2_w[i,j] + self.random_weight()
                elif rand == 2 or rand == 4 or rand == 9:
                    new_inputs_to_layer2_w[i,j] = mate.l2w()[i,j]
                elif rand == 3 or rand == 6 or rand == 7 or rand == 10:
                    new_inputs_to_layer2_w[i,j] = self.inputs_to_layer2_w[i,j]
            #Layer 2 Biases
            rand = random.randint(1,10)
            if rand == 1:
                new_inputs_to_layer2_b[i] = self.random_bias()
            elif rand == 5:
                new_inputs_to_layer2_b[i] = mate.l2b()[i] + self.random_bias()
            elif rand == 8:
                new_inputs_to_layer2_b[i] = self.inputs_to_layer2_b[i] + self.random_bias()
            elif rand == 2 or rand == 4 or rand == 9:
                new_inputs_to_layer2_b[i] = mate.l2b()[i]
            elif rand == 3 or rand == 6 or rand == 7 or rand == 10:
                new_inputs_to_layer2_b[i] = self.inputs_to_layer2_b[i]
        #Layer 3
        for i in range(LAYER_THREE_LENGTH):
            for j in range(LAYER_TWO_LENGTH):
                #Layer 2 to Layer 3 Weights
                rand = random.randint(1,10)
                if rand == 1:
                    new_layer2_to_layer3_w[i,j] = self.random_weight()
                elif rand == 5:
                    new_layer2_to_layer3_w[i,j] = mate.l3w()[i,j] + self.random_weight()
                elif rand == 8:
                    new_layer2_to_layer3_w[i,j] = self.layer2_to_layer3_w[i,j] + self.random_weight()
                elif rand == 2 or rand == 4 or rand == 9:
                    new_layer2_to_layer3_w[i,j] = mate.l3w()[i,j]
                elif rand == 3 or rand == 6 or rand == 7 or rand == 10:
                    new_layer2_to_layer3_w[i,j] = self.layer2_to_layer3_w[i,j]
            #Layer 3 Biases
            rand = random.randint(1,10)
            if rand == 1:
                new_layer2_to_layer3_b[i] = self.random_bias()
            elif rand == 5:
                new_layer2_to_layer3_b[i] = mate.l3b()[i] + self.random_bias()
            elif rand == 8:
                new_layer2_to_layer3_b[i] = self.layer2_to_layer3_b[i] + self.random_bias()
            elif rand == 2 or rand == 4 or rand == 9:
                new_layer2_to_layer3_b[i] = mate.l3b()[i]
            elif rand == 3 or rand == 6 or rand == 7 or rand == 10:
                new_layer2_to_layer3_b[i] = self.layer2_to_layer3_b[i]
        #Output Layer
        for i in range(OUTPUT_LENGTH):
            for j in range(LAYER_THREE_LENGTH):
                #Layer 3 to Output Layer Weights
                rand = random.randint(1,10)
                if rand == 1:
                    new_layer3_to_output_w[i,j] = self.random_weight()
                elif rand == 5:
                    new_layer3_to_output_w[i,j] = mate.ow()[i,j] + self.random_weight()
                elif rand == 8:
                    new_layer3_to_output_w[i,j] = self.layer3_to_output_w[i,j] + self.random_weight()
                elif rand == 2 or rand == 4 or rand == 9:
                    new_layer3_to_output_w[i,j] = mate.ow()[i,j]
                elif rand == 3 or rand == 6 or rand == 7 or rand == 10:
                    new_layer3_to_output_w[i,j] = self.layer3_to_output_w[i,j]
            #Output Layer Biases
            rand = random.randint(1,10)
            if rand == 1:
                new_layer3_to_output_b[i] = self.random_bias()
            elif rand == 5:
                new_layer3_to_output_b[i] = mate.ob()[i] + self.random_bias()
            elif rand == 8:
                new_layer3_to_output_b[i] = self.layer3_to_output_b[i] + self.random_bias()
            elif rand == 2 or rand == 4 or rand == 9:
                new_layer3_to_output_b[i] = mate.ob()[i]
            elif rand == 3 or rand == 6 or rand == 7 or rand == 10:
                new_layer3_to_output_b[i] = self.layer3_to_output_b[i]
        new_nn = snap_nn()
        new_nn.assign_layer2_weights(new_inputs_to_layer2_w)
        new_nn.assign_layer2_biases(new_inputs_to_layer2_b)
        new_nn.assign_layer3_weights(new_layer2_to_layer3_w)
        new_nn.assign_layer3_biases(new_layer2_to_layer3_b)
        new_nn.assign_output_weights(new_layer3_to_output_w)
        new_nn.assign_output_biases(new_layer3_to_output_b)
        return new_nn  
                
                    
                
                
        
    
