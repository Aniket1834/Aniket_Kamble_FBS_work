'''prompt user to enter userid and password. After verifying 
userid and password display a 4 digit random number and ask user to enter the 
same. If user enters the same number then show him success message otherwise 
failed. (Something like captcha)'''


import random

UserId = input("Enter User Id:")
Pass1 = input("Enter Password:")

if(UserId == 'Aniketk1655' and Pass1 == 'ak123'):
    
    Captcha = random.randint(1000,9999)
    print("Captcha",Captcha)
    input = int(input("Enter Captch:"))
    
    if(input==Captcha):
        print("Log in Succesfully!!")
    
    else:
        print("Enter valis Captcha")
        
else:
    print("Enter Valid User Id or Password")
    