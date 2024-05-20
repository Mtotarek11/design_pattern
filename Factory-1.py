class A : 
    def __init__(self) -> None:
        print(" That Is Class A ")
class B  :
     def __init__(self) : 
          print(" That Is Class B ")
class C : 
     def __init__(self) -> None:
           print(" That is class C ") 
class Factory :
        def creat_class (self,data) : 
            if  data == "A"  : 
                return A()
            elif data == "B" : 
                return B()
            elif data == "C" :
                return C()
obj  = Factory().creat_class("A")
obj2 = Factory().creat_class("C")
obj3 = Factory().creat_class("B")
            