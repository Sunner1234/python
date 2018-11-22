c=789
def foo():
	#c=456
    def bar():
    	#c=123
        print(c)
    bar()

if __name__ == '__main__':	
	foo()
	print(__name__)
	#print(globals())
	