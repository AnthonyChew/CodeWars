def pig_it(text):
    #your code here
    
    count = 0

    words = text.split()
    newWord = []
    
    for word in words:
        reConWord = ""
        
        if(word.isalpha()):
            for count in range(1 , len(word) + 1):
                
                if(count != len(word)):
                    reConWord += word[count]
                else:
                    reConWord += word[0] + "ay"
            
            newWord.append(reConWord)
        else:
            newWord.append(word)
            
        
    print(' '.join(newWord)) 
    return(' '.join(newWord)) 
    
pig_it()