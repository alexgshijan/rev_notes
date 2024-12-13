non_prime_flag = False
query = input("Enter a number to query :")

for integer in range(2, int(query)):
    if int(query) % integer == 0:
        non_prime_flag = True

if non_prime_flag == True:
    print(f"{query} is not prime")
else:
    print(f"{query} is prime")