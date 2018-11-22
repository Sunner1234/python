def foo():
    b=123
    #闭包
    def bar():
        nonlocal b
        b=456
        print(b)
    bar()
    print(b)
#调用主函数
foo()
        