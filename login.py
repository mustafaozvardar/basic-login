print("*** Welcome to Login Page ***")


name="root"
password=1234
totry=3

print("Tries left: ",totry)

while True:
    username=input("-> Enter your name: ") 
    userpassword=int(input("-> Enter your password: "))
    
    if name==username and password!=userpassword:
        print("!..Invalid Password..!")
        totry-=1
        print("Tries left: ",totry)
    elif name!=username and password==userpassword:
        print("!..Invalid Username..!")
        totry-=1
        print("Tries left: ",totry)
    elif name!=username and password!=userpassword:
        print("!..Invalid Username and Password..!")
        totry-=1
        print("Tries left: ",totry)
    else:
        print("-> Login Successful...")
        break
    if(totry==0):
        print("-> Login Failed...")
        break
