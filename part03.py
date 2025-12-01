def staff_version_with_histogram():

    print("Staff_Version_with_Histogram")

    
    credit_at_pass=0
    credit_at_defer=0
    credit_at_fail=0
    total=0

    list1=[]
    listed_credits=[0,20,40,60,80,100,120]

    progress_count=0
    progress_mtrailer_count=0
    exclude_count=0
    module_retriever_count=0
    choice=""
    count=0
        

    

    while True:
        while True:
            try:
                credit_at_pass=int(input("\nEnter your total PASS credits:\t"))
                
                if credit_at_pass in listed_credits:
                    
                    credit_at_defer=int(input("\nEnter your total DEFER credits:\t"))
                    
                    if credit_at_defer in listed_credits:
                        
                        credit_at_fail=int(input("\nEnter your total FAIL credits:\t"))
                        
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



    
        for x in list1:
            if list1[0]==120:
                
                print("\nProgress")            
                progress_count=progress_count+1
                
                
                break
            elif list1[0]==100:
                
                print("\nProgress (module trailer)")
                progress_mtrailer_count=progress_mtrailer_count+1
                
                break
            elif list1[2]>=80:
                
                
                print("\nExclude")
                exclude_count=exclude_count+1
                
                break
            
            else:
                
                print("\nDo not progress – module retriever")
                module_retriever_count= module_retriever_count+1
                break
                


    
        choice=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:\t")
        choice=choice.lower()

        list1=[]


        if choice == "y":
                continue



        
        
        
        elif choice== "q":
            
            
            print("\nHorizontal Histogram")

            print("Progress\t - ",progress_count," : ",end="")
            while count<progress_count :
                    count=count+1
                    print("*",end="")
                    
                    
                
            count=0
            print("\nTrailer\t\t - ",progress_mtrailer_count," : ",end="")
            while count<progress_mtrailer_count :
                    count=count+1
                    print("*",end="")
                    
                    

            count=0
            print("\nRetriever\t - ",module_retriever_count," : ",end="")
            while count<module_retriever_count :
                    count=count+1
                    print("*",end="")
                    
                   

            count=0
            print("\nExcluded\t - ",exclude_count," : ",end="")
            while count<exclude_count :
                    count=count+1
                    print("*",end="")
                    
                    

            print("\n ")
            print(progress_count+progress_mtrailer_count+module_retriever_count+exclude_count," Outcomes in total..")
            break
        
               
        else:
            print("\nError.program automatically quit..Please Enter y to continue or Enter q to quit next time...")
            break


