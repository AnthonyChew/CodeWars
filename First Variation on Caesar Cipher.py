def moving_shift(s, shift):
    result = ""

    for i, v in enumerate(s):

        i = i + shift - 1

        if v.isalpha():
            if ord('a') <= ord(v) and ord(v) <= ord('z'):
                # small case
                shifted_char = ord(v) + ((i + 1) % 26)
                if(ord('z') < shifted_char):
                    encoded_char = ord('a') - 1 + (shifted_char - ord('z'))
                else:
                    encoded_char = shifted_char

            elif ord('A') <= ord(v) and ord(v) <= ord('Z'):
                # Upper
                shifted_char = ord(v) + ((i + 1) % 26)
                if(ord('Z') < shifted_char):
                    encoded_char = ord('A') - 1 + (shifted_char - ord('Z'))
                else:
                    encoded_char = shifted_char
            else:
                encoded_char = ord(v) + i

        else:
            encoded_char = ord(v)

        result = result + chr(encoded_char)

    sliceCount = len(s) / 5

    if(round(sliceCount) < sliceCount):
        sliceCount = round(sliceCount) + 1
    else:
        sliceCount = round(sliceCount)


    tempList = []

    for count in range( 0 ,len(result) , sliceCount):
        if( count + sliceCount < len(result)):
            tempList.append(result[count : count + sliceCount])
        else:
            tempList.append(result[count : len(result)])
    
    emptyArray = 5 - len(tempList) 
    
    if(emptyArray != 0):
        for array in range(emptyArray):
            tempList.append("")
    return tempList


def demoving_shift(s, shift):
    
    tempString = ""
    result = ""

    for words in s:
        tempString += words
    
    for i, v in enumerate(tempString):

        i = i + shift - 1

        if v.isalpha():
            if ord('a') <= ord(v) and ord(v) <= ord('z'):
                # small case
                shifted_char = ord(v) - ((i + 1) % 26)
                if(shifted_char < ord('a')):
                    encoded_char = ord('z') + 1 - (ord('a') - shifted_char)
                else:
                    encoded_char = shifted_char

            elif ord('A') <= ord(v) and ord(v) <= ord('Z'):
                # Upper
                shifted_char = ord(v) - ((i + 1) % 26)
                if(shifted_char < ord('A')):
                    encoded_char = ord('Z') + 1 - (ord('A')- shifted_char)
                else:
                    encoded_char = shifted_char
            else:
                encoded_char = ord(v) - i

        else:
            encoded_char = ord(v)

        result = result + chr(encoded_char)
    return(result)
