if __name__ == "__main__":
    start = int(input("Enter the start of range: "))
    end = int(input("Enter the end of range: "))
  
    for odd in range(start, end + 1, -1):
        
        if odd % 2 != 0:
            print(odd, end = " ")