class Menento : 
    def __init__(self,state) :
        self.state = state
    def get_state (self) :
        return self.state    
    
class originator : 
    def __init__(self) :
        self.state = None

    def set_state(self,state) : 
        print(f'setting new state to {state}')     
        self.state = state
        
    def create_memento(self): 
        return Menento(self.state)
    
    def restore_memento(self,memento) : 
        self.state = memento.get_state()
        print(f'Restored state to {self.state}')

class Caretaker : 
    def __init__(self) :
        self._mementos = []
    def add_memento(self, memento) : 
        self._mementos.append(memento)
    def get_memento(self , index) : 
        return self._mementos[index]




