number = int(input('Enter the number here:'))
isPrime = False

if number > 1:
    for i in range(2,number):
        if number % i == 0:
            isPrime = True
            break

if isPrime:
    print(number,'It is not a prime number')
else:
    print(number,'It is a prime number')


