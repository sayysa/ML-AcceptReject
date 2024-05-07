def evaluate_string(s):
    # if string ends with 0
    if s[-1] != '0':
        return False
    
    # count 0s
    count = 0
    for char in s:
        if char == '0':
            count += 1
    
    # if even 0s
    if count % 2 != 0:
        return False
    
    return True

def main():
    while True:
        value = input("\nEnter a string: ")
        
        if not value.isdigit():
            print("Bye.\n")
            break
        
        if evaluate_string(value):
            print("Accepted")
        else:
            print("Rejected")

if __name__ == "__main__":
    main()
