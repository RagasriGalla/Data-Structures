def count_digits(n):
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count

num = int(input("Enter a number: "))

# Handle 0 case
if num == 0:
    print("Number of digits: 1")
else:
    print("Number of digits:", count_digits(abs(num)))
