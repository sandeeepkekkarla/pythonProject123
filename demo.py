p = 1000
def myfunc():
    print("welcome")
print("demo module name is:", __name__)
print(dir(p))
count = 0
n = int(input("enter a number"))
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print(n, "is a prime num")
else:
    print(n, "is a not prime num")



