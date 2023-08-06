if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) #Convert to list
    
#Or make a new list and copy all the elements in new list 
    # arry = []
    # [arry.append(x) for x in arr if x not in arry]
    
    def high(a):
        test = -101
        for i in range(0, len(a)):
            temp = a[i]
            if a[i] > test:
                test = a[i]
        return test
                    
    def new():
        var = high(arr)
        second = [i for i in arr if i != var]
        final = high(second)
        print(final)
        
    new()