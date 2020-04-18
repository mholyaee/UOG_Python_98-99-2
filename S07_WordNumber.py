def wordnumber(str):
    n=0
    word=''
    for j in str:

        if j==' ' or j=='.' or j==',':
            if len(word)>0:
                n+=1
                print(word)
                word=''
        else:
            word+=j
    return n



str=input("Enter your string:")
temp=wordnumber(str)
print("The word number is:",temp)
