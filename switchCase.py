def Test(currency):

    match currency:
        case '1':
            return "Mathematics 2"

        case '2':
            return "Operating Systems"

        case '3':
            return "Data Structures and Algorithm"
        
        case '4':
            return "Object Oriented Programming"

        case '5': 
            return "Computer Networks"

    


if __name__ == "__main__":
    print("1.CSC1006\n2.CSC1007\n3.CSC1008\n4.CSC1009\n5.CSC1010")
    currency = input("Select your course: ")
    print(Test(currency))