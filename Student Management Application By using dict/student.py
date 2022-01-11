n=int(input('ENTER NO OF STUDENT:'))
dict={} #EMPTY DICT FOR STORE DATA
for i in range(n):
    name=input('ENTER STUDENT NAME:')
    marks=int(input('ENTER STUDENT MARKS:'))
    dict[name]=marks
print('STUDENT DATA INSERTION COMPLETED')
print('*'*30)
print('NAME','\t\t', 'MARKS')
print("*"*30)
for k,v in dict.items():
    print(k,'\t\t',v)

print('SEARCH OERATION STARTED....')
while True:
    name=input('ENTER STUDENT NAME TO GET THE MARKS:')
    marks=dict.get(name,-1) # IF THE STUDENT NAME NOT IN DICT IT RETURNS DEAFULT VALUE -1
    if marks==-1:
        print('Student not found')
    else:
        print('MARKS OF',name,'ARE',marks)
    option=input('DO YOU WANT TO FIND ANOTHER STUDENT MARKS(YES/NO):')
    if option.lower()=='no':
        break
print('THNAKS FOR USING OUR APPLICATION')
