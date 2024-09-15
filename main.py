from cryptography.fernet import Fernet

'''def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    with open("key.key","rb") as key_file:
        key=key_file.read()
    return key

key=load_key()
fer=Fernet(key)
def view():
    print("\n" + "-"*40)
    print("Viewing saved passwords:")
    print("-"*40)
    with open('password.txt',"r") as f:
        for line in f:
            line=line.strip()
            parts=line.split('|')
            if(len(parts)==2):
                username,paswd=parts
                try:
                    decrypt_paswd=fer.decrypt(paswd.encode()).decode()
                    print(f"Name : {username}, password : {decrypt_paswd}")
                except Exception as e:
                    print(f"Error decrypting password for user {username}: {e}")
    print("-"*40)
def add():
    print("\n" + "-"*40)
    print("Adding a new password:")
    print("-"*40)
    while(True):
        new_choice=None
        name=input("Acount Name : ")
        pwd=input("Enter your password : ")
        while(True):
            cofm_pwd=input("Confirm your password : ")
            if(pwd==cofm_pwd):
                with open("password.txt","a") as f:
                    f.write(f'{name} | {fer.encrypt(pwd.encode()).decode()}\n ')
                return 1
            else:
                while(True):
                    print("-"*40)
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
print("\n" + "-"*40)
print("Password Manager")
print("-"*40)
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