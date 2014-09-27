print(__doc__)

from sklearn import datasets;
digits = datasets.load_digits();
data = digits.data;
target = digits.target;


import numpy as np
from createRow import createRow
from scipy import linalg
_N = (int(input()));#hidden number of neurons the user wants
data1 = data.transpose();
sz = data1[:, 0].size;
weights = np.random.normal((sz) * _N);
final = np.reshape(weights, (sz, -1));
b = np.random.standard_normal(_N);
print _N, data.shape, final.shape;
def sigmoid(W, X, b):
	s = np.dot(X, W);
	G= []
	x = s+b
	for k in x:
		for l in k:
			sig = 1/(1+np.exp(-l));
			G+= [sig]
	G = np.reshape(G, (x.shape[0], -1));
	return G
G=[]
G = sigmoid(final, data, b);
print G
print G.shape;
'''U, s, Vh = linalg.svd(G, full_matrices=False);
inv = np.reciprocal(s)
S = np.diag(inv);
G_ = np.dot(np.dot(np.transpose(Vh), S), np.transpose(U));
print "Printing G.........\n"
print G_
print shape(G_)'''
G_ = np.linalg.pinv(G);
print "G_ has shape";
print  shape(G_);
A= np.ones((digits.target_names.size, digits.target.size))*-1;
def createRow(a, b, c):
	A[b][a] = c;
for x in range(digits.target.size):
	createRow(x, digits.target[x], 1);
T= np.transpose(A)
print T
print "Now finally "
beta= np.dot(G_, T)
print shape(beta);
#print shape(G)
print shape(T)
newT = np.dot(G,beta)

#ELM with mapreduce
