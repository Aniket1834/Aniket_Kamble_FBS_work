#number of notes

amount = int(input("Enter Amount : "))
print("Minimum number ofnotes needed : ")

note = 500

while (amount>0):
    if amount>=note:
        count = amount // note
        amount = amount % note
        
        print(note,":" ,count)
        
        
    if (note==500):
        note =200
        
    elif (note == 200):
        note = 100
        
    elif(note == 100):
        note = 50
        
    elif (note == 50):
        note = 20
    
    elif (note == 20):
        note = 10
    elif (note == 10):
        break
print("Remaining Amount : ", amount)
        