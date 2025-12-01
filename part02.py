def student_version_validation():
    
    print("Student_Version (Validation)")
    
    credit_at_pass=0
    credit_at_defer=0
    credit_at_fail=0
    total=0

    list1=[]
    listed_credits=[0,20,40,60,80,100,120]

    
    while True:
        try:
            credit_at_pass=int(input("\nPlease enter your credits at pass:\t"))
            
            if credit_at_pass in listed_credits:
                
                credit_at_defer=int(input("\nPlease enter your credits at defer:\t"))
                
                if credit_at_defer in listed_credits:
                    
                    credit_at_fail=int(input("\nPlease enter your credits at fail:\t"))
                    
                    if credit_at_fail in listed_credits:
                        
                        total = credit_at_pass+credit_at_defer + credit_at_fail
                        
                        if total==120:
                            break
                        
                        
                        else:
                            print("\nTotal incorrect")
                            
                    else:
                        print("\nOut of range")
                        
                else:
                    print("\nOut of range")
                    
            else:
                print("\nOut of range")
                
        except:
            print("\nInteger required")




    
    list1.append(credit_at_pass)
    list1.append(credit_at_defer)
    list1.append(credit_at_fail)
