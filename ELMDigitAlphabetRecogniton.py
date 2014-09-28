print(__doc__)
import numpy as np
from scipy import linalg    #to calculate Moore Penrose inverse

def getDataset(data, target, _N, C):     #C-no.of classes
    #_N = (int(input()));    #hidden number of neurons the user wants
    data1 = np.transpose(data);   # the input is given as (No. of fatures * No. of elements in dataset)
    sz = data1[:, 0].size;  #No. of features
    weights = np.random.standard_normal((sz) * _N);  #using random normal distribution to generate sz*_N random weights into a row vector
    final = np.reshape(weights, (sz, -1));  #reshaping row vector into (No. of features * No. of hidden layer neurons)
    b = np.random.standard_normal(_N);  #Bias for X0 feature neuron
    #print _N, data.shape, final.shape;  
    def sigmoid(W, X, b):
	    s = np.dot(X, W);
	    G= []
	    x = s+b
	    for k in x:
		    for l in k:
			    sig = 1/(1+np.exp(-l));
			    G+= [sig]
	    G = np.reshape(G, (shape(x)[0], -1));
	    return G
    G=[]
    G = sigmoid(final, data, b);    #final=weight vector
    #print G
    #print G.shape;

    G_ = np.linalg.pinv(G);
   
    #print  shape(G_);
    A= np.ones((C, shape(data)[0]))*-1;
    def createRow(a, b, c):
	    A[b][a] = c;
    for x in range(shape(data)[0]):
	    createRow(x, target[x], 1);
    T= np.transpose(A)
    #print T
   
    beta= np.dot(G_, T)
    #print shape(beta);
    #print shape(G)
    #print shape(T)
    newT = np.dot(G,beta)
    return newT


