def exp_sum(n):
    #your code here
    
    cd = []
    
    for num in range(1 ,n):
        if( (n % num) == 0):
            cd.append(num)

    count = len(cd) - 1
    resultCount = 0
    
    #posibility
    while(count != 0):
        
        for numCount in range(count):
            tempSum = cd[count] + cd[numCount]    
            if(tempSum > n):
                break
            else:
                resultCount += 1
            print(tempSum)
        
        count -= 1
    
    
    # 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
    
exp_sum(4)