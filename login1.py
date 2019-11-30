import pickle
f=open('dict.pkl','rb')
s=pickle.load(f)
f.close()
s3=s
#print(s3)
keys=s3.keys()
val=s3.values()
fp=open('dict.pkl','wb')
uname=input('Enter Username:')
if uname not in keys:
    ab=input('Are u an existing user(Y/N)')
    if ab=='n'or ab=='N':
        nu=input('Enter New Username').lower()
        np=input('Enter Password')
        s3[nu]=np
    else:
        print('Enter Valid Username')
else:
    i=0
    a='N'
    while(i<5 or a=='y' or a=='Y'):
        i+=1
        pas=input("Enter Password")
        if s3[uname]==pas:
            print('Login Succesfull')
            break
            a='Y'
        else:
            print('Enter correct Password')
    if i==6 or i==5:
        print("Reached Maximum Limit Try Later")
        c=input('Do You Want To Change Password(Y/N)')
        if c=='y' or c=='Y':
            s3[uname]=input("Enter New Password")
#print(s3)                 
pickle.dump(s3,fp)        
fp.close()
