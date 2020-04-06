a=int(input('input first measure:'))
b=int(input('input second measure:'))
if a>0 and b>0:
    if a==b:
        print('Is square')
    else:
        print('Is rectangle')
else:
    print('The inputs are not suitable')
