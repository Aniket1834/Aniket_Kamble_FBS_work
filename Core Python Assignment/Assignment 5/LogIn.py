# prompt user to enter userid and password
attempt = 0

while (attempt<3):
    User = input("Enter UserName : ") 
    Pass1 = input("Enter Password : ")
    
    if( User == "Aniket_k" and Pass1 == "ak@123"):
        print("Login Succesfully!!!")
        break
    
    else:
        print("Please Enter Correct Usename ")
        
        attempt+=1
        
if(attempt==3):
    print("Log in Failed,")