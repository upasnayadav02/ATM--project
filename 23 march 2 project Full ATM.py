#Real world ATM
users={
    "upasna":{"pin":"1234","balance":10000},
    "chetan":{"pin":"0203","balance":20000}
    }
transactions=[]
pins={"1234","0203"}
username=input("Enter a username:").strip().lower()
if username in users:
    for  i in range (3):
        pin=input("enter a pin:")
        if pin==users[username]["pin"]:
            print("Login sucessfully")
            while True:
                print("======MENU======")
                print("""Select an Option
                1.Check Balance
                2.Deposit
                3.Withdraw
                4.Exit""")
                choice=int(input("Enter an option:"))
                if choice== 1:
                    print("Balance",users[username]["balance"])
                elif choice==2:
                    amunt=int(input("Enter a deposit amunt:"))
                    users[username]["balance"]+=amunt
                    transactions.append("Deposited"+str(amunt))
                elif choice==3:
                    amnt=int(input("Enter a amount:"))
                    if amnt<=users[username]["balance"]:
                        users[username]["balance"]-=amnt
                        transactions.append("WIthdraw"+str(amnt))
                    else:
                        print("Insufficent Balance")
                elif choice==4:
                    print("Transaction History:")
                    for t in transactions :
                        print(t)
                elif choice==5:
                    print("Thank you")
                    break
                else:
                    print("Invalid Choice")
                
        else:
            print("Account Blocked")
else:
    print("User Not Found")
                
                    
        
                
                        
                


    
            
        
    
        
        
        
    

        
    
          
          
          
          
        
        
        


 

            
    
    

    

    
    
    
    

    
     

    



             






    
