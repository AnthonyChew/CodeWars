def exp_sum(n):
    #your code here
    
    cd = []
    
    for num in range(1 ,n):
        if( (n % num) == 0):
            cd.append(num)

    count = len(cd) - 1
    resultCount = 0
    numCount = 0
    
    #posibility
    while(count != 0):
        
        while( (cd[count] + cd[numCount]) < n ):
            
        
        count -= 1
    
    
    # 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
    
exp_sum(4)