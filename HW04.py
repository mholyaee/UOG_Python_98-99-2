while True:
    st_number,code=input("Enter student number and code:").split()
    if code=='m' or code=='M':
        Last=st_number
    elif code=='f' or code=='F':
        pass
    else:
        break
print("The student number of last man is:", Last)
