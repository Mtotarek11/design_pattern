class Car : 
    def __init__(self) -> None:
        self.color = None
        self.type = None 
        self.engine = None
        self.air_conditioning = None

    def put_air_conditioning(self, air_conditioning): 
        self.air_conditioning = air_conditioning

    def put_color(self,color) : 
        self.color = color 
        
    def what_type(self,type) : 
        self.type = type

    def engine_type(self,engine) : 
        self.engine = engine

    def display(self):
        print(f'That car has Color {self.color}\n'
            f'That car has engine {self.engine}\n'
            f'That car has air conditioning {self.air_conditioning}\n'
            f'The type of car is {self.type}')

class CarBuilder : 
    def __init__(self) -> None:
        self.car = Car()
    def put_air_conditioning(self, air_conditioning):
        self.car.put_air_conditioning(air_conditioning)
        return self
    
    def put_color(self,color) : 
        self.car.put_color(color)  
        return self
    
    def what_type(self,type) : 
        self.car.what_type(type)  
        return self
    
    def engine_type(self,engine) : 
        self.car.engine_type(engine) 
        return self
    
    def build (self) : 
        return self.car
    
x = CarBuilder
car_v = x.put_air_coditioning("hot").put_color("red").what_type("BMW").what_engine("very fast").build
car_v.display()
        