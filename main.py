from cryptography.fernet import Fernet

master_pwd=input("Enter Master password : ")

def view():
    with open('password.txt',"r") as f:
        for i in f.readlines():
            li=i.strip()
            new_li=li.split("|")
            for j in new_li:
                print(j,end=" ")
            print()
            

def add():
    while(True):
        new_choice=None
        name=input("Acount Name : ")
        pwd=input("Enter your password : ")
        while(True):
            cofm_pwd=input("Confirm your password : ")
            if(pwd==cofm_pwd):
                with open("password.txt","a") as f:
                    f.write(f'Account Name : {name} | Password : {pwd}\n ')
                return 1
            else:
                while(True):
                    new_comd=input("please confirm your password again or renter you new password (confirm pass/new pass)or to quit enter 'q' ").lower()
                    if(new_comd=='new pass'):
                        new_choice ='new pass'
                        break
                    elif(new_comd=='confirm pass'):
                        new_choice='confirm pass'
                        break
                    elif(new_comd=="q"):
                        return 0
                    else:
                        print("invalid option : ")
            if(new_choice=='new pass'):
                break

        if(new_choice=='new pass'):
            continue




while(True):
    mode=input("Would you like to view or add a password(view/add) or enter 'q' to quit : ").lower()
    if(mode=='q'):
        print("you choose to quit")
        break
    if(mode=='view'):
        view()
    elif(mode=='add'):
        result=add()
        if(result==1):
            print("password added succesfully ")
        else:
            print("You choose to quit")
            break

    else:
        print("invalid option")