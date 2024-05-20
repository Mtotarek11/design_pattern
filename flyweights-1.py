class Flyweight : 
   

    def __init__(self,family) -> None:
        self.family = family 
     
    def opperation(self,unique_state) : 
   
        print(f"Flyweight{self._name}doing opperation with state ")



class FlyweightFactory : 
    _flyweight= {}
    def get_Flyweight(self , shared_Data ) : 
        if shared_Data not in self._flyweight : 
            print(f"creating flyweigh for state {shared_Data}")
            self._flyweight[shared_Data] = Flyweight(shared_Data)
        return self._flyweight[shared_Data]   




factor = FlyweightFactory()
fly1 = factor.get_Flyweight("A")
fly2 = factor.get_Flyweight("A")
fly3 = factor.get_Flyweight("C")
fly4 = factor.get_Flyweight("C")
fly5 = factor.get_Flyweight("B")
print(fly1 is fly2)
print(fly2 is fly3)
print(fly2 is fly4)
##fly2.opperation("good")
