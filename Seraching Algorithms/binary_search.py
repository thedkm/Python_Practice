#Time Complexity O(logn)

def binary_search(data,target,low ,high):
    if low > high :
       print("Data is not found!!")
    else:
        mid = (low+high)//2
        if target == data[mid]:
            print( "Data found at index {} and data is {}".format(mid,data[mid]))
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)


def main():
    
    data=[2, 4 ,5, 7, 8 ,9,12, 14 ,17, 19 ,22 ,25, 27 ,28, 33,37]
    target =22
    low =0
    high= 15

    binary_search(data, target, low, high)




if __name__ == '__main__': main()
