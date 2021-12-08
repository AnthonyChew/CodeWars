def find_it(seq):
    
   seq.sort()
   
   preNum  = seq[0]
   count = 0
   maxCount = 0
   rnum = 0
    
   for num in seq:
   
      if(num == preNum):
         count += 1
      else:
         if(count % 2): 
            maxCount = count
            rnum = preNum
            
         preNum = num
         count = 1
   
   if(count % 2): 
      maxCount = count
      rnum = preNum
   print(rnum)
   
   return maxCount

find_it([1,1,1,1,1,1,10,1,1,1,1])