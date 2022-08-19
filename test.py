import demo
a=2000
def fun1():
    print("in fun1 of test")
if __name__=="__main__":
    print(a)
    fun1()
    print(demo.p)
    demo.myfunc()
    print("test module name is:",__name__)
count = 0
n = int(input("enter a number"))
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print(n, "is a prime num")
else:
    print(n, "is a not prime num")



