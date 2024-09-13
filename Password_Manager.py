master_pwd=input("input the master paswrd")

def view():
    with open('file.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw=data.split("|")
            print("User Name is ",user,"Password is ", passw)
def write():
    username=input("Enter the user name: ")
    pwd=input("Enter the password: ")
    with open('file.txt','a') as f:
        f.write(username+"|"+pwd+"\n")
while True:
    mode=input("Do you want to read the file or write the file,Press Q to quit: ")
    if mode=="Q":
        quit()
        break
    if mode=="add":
        write()
    if mode=="read":
        view()
