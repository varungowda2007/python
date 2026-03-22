def is_prime(n):
    if n< 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter the number :"))
print(is_prime(num))

nu = int(input("Enter the number :"))
if nu < 2:
    print("Not a prime number")
else:
    for i in range(2, int(nu**0.5) + 1):
        if nu % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")