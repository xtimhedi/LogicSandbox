from GateActorEngine import GateActor
from ursina import *

class PassthroughActor(Entity):
    def __init__(self,**kwargs):
        # as this is just serving as a parent for all subentites (the BaseGate/pegs), we dopt need to assign anythgon in this
        super().__init__(**kwargs)
        
        # assign this a GateActor
        self.DefinedGate = GateActor([["in", "TestGate",-0.2],["out", "TestGate",0.2]],parent=self,color=color.red,type="PlaceableObject")
        
    def update(self):
        try:
            self.DefinedGate.Pegs[1].on = self.DefinedGate.Pegs[0].on
        except:
            pass
            
            
            
class NandActor(Entity):
    def __init__(self,**kwargs):
        # as this is just serving as a parent for all subentites (the BaseGate/pegs), we dopt need to assign anythgon in this
        super().__init__(**kwargs)
        
        # assign this a GateActor
        self.DefinedGate = GateActor([["in", "a",-0.2],["in", "b",0],["out", "out",0.2]],parent=self,color=color.red,type="PlaceableObject")
        
    def GateFunction(self,a,b):
        return not (a and b)
        
    def update(self):
        try:
            self.DefinedGate.Pegs[2].on = not (self.DefinedGate.Pegs[0].on and self.DefinedGate.Pegs[1].on)
        except:
            pass