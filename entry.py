date=input('Enter The Date:')
name=input('Enter The Name:')
remarks=input('Enter the Reason For Expences:')
amt=float(input('Enter The Amount:'))
mode=input('Enter The Mode:')

file=open('entry.csv','a')
c=date+','+name+','+remarks+','+str(amt)+','+mode+'\n'

file.write(c)
file.close()
print('Successfully Done!!!!!')