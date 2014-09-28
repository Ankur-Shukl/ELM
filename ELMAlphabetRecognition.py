import csv
dataset = []
with open('Alphabets.txt') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		dataset += [row]
dataset = dataset[0:20000];
arr=[]
target=[]
for x in dataset:
	arr  +=[x[1:]]
	target +=x[0]
count=-1;
for x in arr:
    count = count+1
    for i,j in enumerate(x):
        arr[count][i]=int(j)
    
for i,j in enumerate(target):
	target[i] = ord(j)-65
data=arr


	
