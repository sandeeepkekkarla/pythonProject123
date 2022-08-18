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

