def testELMAlphabetRecognition(newT):
    Z = []
    for x in newT:
        for i, j in enumerate(x):
            if(j==max(x)):
                Z=Z+[i]
              
    A=[]
    count=0;
    for i in range(shape(Z)[0]):
        A+=[Z[i]==target[i]]
    for k in A:
        if(k==False):
            count = count+1;
    #print count
    print (20000-count)/20000.
