import part01
import part02
import part03
import part04
import part05




while True: 
    print()
    print()
    print()
    print()

    print("01---> Student Version")
    print("02---> Student Version(Validation)")
    print("03---> Staff Version with Horizontal Histogram")
    print("04---> Staff Version with Vertical Histogram")
    print("05---> Alternative Staff Version (optional extension)!!!You can use only one time..if u want run this again..exit and restart program..")
    print("06---> Exit")
    
    choice = int(input("\nEnter Your Choice :  "))
    print()
    
    




    if choice == 1:
                part01.student_version()
    elif choice == 2:
                part02.student_version_validation()
    elif choice == 3:
                part03.staff_version_with_histogram()
    elif choice == 4:
                part04.vertical_histogram()
    elif choice == 5:
                part05.alternative_staff()

    elif choice == 6:
        break
                
    else:
        
        print("\nEnter valid number between 1-6 !")
        
        continue 
