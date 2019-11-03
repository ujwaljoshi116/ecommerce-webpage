def loginpass():
    print("Sign in  to contine ")
    print("-"*80)
    login=input("Enter username:")
    password=input("Enter password:")

    if login=="123@gmail.com":
         if password == "1234":
             print("Access given!!!!!!!")
            
         else :
             print("WRONG PASSWORD!!!!!!!")
             print("-"*80)
             loginpass()
    else:
        print("Wrong username or PASSWORD!!!!!!")
        print("-"*80)

        loginpass()

        
loginpass()        
