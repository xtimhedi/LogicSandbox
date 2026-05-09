from ursina import *
import sys
Main = sys.modules['__main__']

class WireActor(Entity):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        PosA = a.world_position + Vec3(0, a.world_scale_y / 2.4, 0)
        PosB = b.world_position + Vec3(0, b.world_scale_y / 2.4, 0)
        Distance = distance(PosA, PosB)
        super().__init__(
            model='cube',
            color=color.gray,
            parent=scene,
            world_position=PosA,
            origin=(0, 0, -0.5),
            scale=(0.1, 0.1, Distance),
            collider='box',
            on=True
        )
        self.world_parent = scene
        self.look_at(PosB)
        
        self.outline = Entity(
            model='cube',
            color=color.blue,
            parent=scene,
            world_position=PosA,
            origin=(0, 0, -0.5),
            scale=(0.11, 0.11,Distance+0.01),
            wireframe=True
        )
        self.outline.world_parent = scene
        self.outline.look_at(PosB)
        
    def update(self):
        if mouse.hovered_entity == self:
            self.outline.enabled = True
        else:
            self.outline.enabled = False
            
        try:
            self.on = self.a.on
            self.b.on = self.on
        except:
            pass
            
        
        
    def input(self,key):
        if key == 'left mouse down':
            if Main.SelectedGate == 'Wire Cutters':
                if mouse.hovered_entity == self:
                    destroy(self)
                    destroy(self.outline)
                
                
class InputPin(Entity):
    def __init__(self,**kwargs):
        super().__init__(
            model='assets/InputPeg',
            collider='box',
            color=color.black,
            on=False,
            **kwargs
        )
        
    def update(self):
        if self.hovered:
            self.wireframe = True
        else:
            self.wireframe = False
            
        if self.on == True:
            self.color = color.red
        else:
            self.color = color.black
        
class OutputPin(Entity):
    def __init__(self,**kwargs):
        super().__init__(
            model='assets/OutputPeg',
            collider='box',
            color=color.black,
            on=False,
            **kwargs
        )
    def update(self):
        if self.hovered:
            self.wireframe = True
        else:
            self.wireframe = False
            
        if self.on == True:
            self.color = color.red
        else:
            self.color = color.black
            
class GateActor(Entity):
    def __init__(self,pins,**kwargs):
        self.Pegs = []
        super().__init__(
            model='assets/BaseGate',
            collider='box',
            **kwargs
        )
        
        for i in pins:
            if i[0] == "in":
                Pin = InputPin(parent=self,z=i[2],y=0.3)
                self.Pegs.append(Pin)
                print(f"Assigned a pin with metadata: (InputPin,Named,Offset={i[2]}) with name {i[1]}")
            if i[0] == "out":
                Pin = OutputPin(parent=self,z=i[2],y=0.3)
                self.Pegs.append(Pin)
                print(f"Assigned a pin with metadata: (OutputPin,Named,Offset={i[2]}) with name {i[1]}")
        
    
        