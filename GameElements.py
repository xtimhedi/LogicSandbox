from ursina import *
from GateActorEngine import *
from ursina.prefabs.first_person_controller import FirstPersonController
class SwitchActor(Entity):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.on=False
        self.DefinedGate = GateActor([["out", "TestGate",0]],parent=self,color=color.orange,type="PlaceableObject")
        self.DefinedGate.on_click = self.ToggleButton
    def ToggleButton(self):
        self.on = not self.on
    
    
    
    def update(self):
        try:
            self.DefinedGate.Pegs[0].on = self.on
        except:
            pass
            
class ButtonActor(Entity):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.on=False
        self.DefinedGate = GateActor([["out", "TestGate",0]],parent=self,color=color.orange,type="PlaceableObject")
    
    def input(self,key):
        if key == 'left mouse down' and mouse.hovered_entity == self.DefinedGate:
            self.on = True
            self.DefinedGate.Pegs[0].on = True
        elif key == 'left mouse up' and mouse.hovered_entity == self.DefinedGate:
            self.on = False
            self.DefinedGate.Pegs[0].on = False

# credit to {https://github.com/tonka3000/miniminecraft/blob/main/mmc/firstperson.py} for their FPCAdvanced class that includes flying
class FPCAdvanced(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._fly = True
        self.fly = False

    @property
    def fly(self):
        return self._fly

    @fly.setter
    def fly(self, value:bool):
        self._fly = value
        self.gravity = 0 if self._fly else 1

    def update(self):
        super().update()

        if not self.fly:
            return

        # Fly control
        if held_keys['space']:
            self.position += self.up * time.dt * self.speed
        if held_keys['shift']:
            self.position -= self.up * time.dt * self.speed
    