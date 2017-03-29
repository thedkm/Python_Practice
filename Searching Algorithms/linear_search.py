#Time complexity O(n)

def sequential_search(data,target,low,high):
	for i in range(low,high):
		if data[i] == target:
			print("data is found at index {} and data is {}".format(i,data[i])) 
			break
		else:print("data is not found! !!")
			
def main():
    
    data=[2, 4 ,5, 7, 8 ,9,12, 14 ,17, 19 ,22 ,25, 27 ,28, 33,37]
    target =17
    low =0
    high= 15

   
    sequential_search(data,target,low,high)


if __name__ == '__main__': main()
