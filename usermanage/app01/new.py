
def outer(some_fun):     #some_fun=fun
    def inner(a):
        print(type(a))
        print("inner")
        ret=some_fun(a)     #ret=fun()  执行fun()
        print(ret)
        return ret         #return fun()    inner()=fun()
    return inner          #return fun  outer()=fun

# 引用装饰器的写法一
a=10
@outer
def fun(a):
    print(a)
    print("fun")
    return 2
fun(a)