def testELMDigitRecognition(newT):
    Z = []
    for x in newT:
        for i, j in enumerate(x):
            if(j==max(x)):
                Z=Z+[i]
                
    z = (Z==digits.target);
    count=0;
    for k in z:
        if(k==False):
            count = count+1;
    #print count
    print (1797-count)/1797.
