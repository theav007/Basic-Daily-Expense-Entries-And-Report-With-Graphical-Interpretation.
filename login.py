b={1:'Entry',2:'Details',3:'Exit'}

for i in b:
    print(b[i])
b1=int(input('Enter Command:'))
if b1==1:
    import entry
elif b1==2:
    import details
elif b1==3:
    print('Exit')
else:
    print('Please Enter Right One:')
            