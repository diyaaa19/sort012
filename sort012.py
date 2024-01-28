arr = [2,0,1,1,0,2,1,0] 
n = len(arr) 

def printArr(arr, n): 
	for i in range(n): 
		print(arr[i],end=" ") 

def sortArr(arr, n): 
	ct0 = 0
	ct1 = 0
	ct2 = 0
	
	
	for i in range(n): 
		if arr[i] == 0: 
			ct0+=1
		
		elif arr[i] == 1: 
			ct1+=1
			
		elif arr[i] == 2: 
			ct2+=1
	
	i = 0
	
	
	while (ct0 > 0): 
		arr[i] = 0
		i+=1
		ct0-=1
	
	
	while (ct1 > 0): 
		arr[i] = 1
		i+=1
		ct1-=1
	
	
	while (ct2 > 0): 
		arr[i] = 2
		i+=1
		ct2-=1
	
	
	printArr(arr, n) 

sortArr(arr, n) 



