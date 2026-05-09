from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import sys
import time

from GateActors import *
from GateActorEngine import *
from GameElements import *
from Pegboard import *



OpenLogicWorld = Ursina(title="LogicSandbox")
GamePlayer = FPCAdvanced()
SelectedGate = None
SelectedToolText = Text(f"Tool: {SelectedGate}",position=(-0.89,0.5))


ghost = Entity(model='assets/BaseGate', color=color.rgba(0, 255, 0, 100), scale=1, enabled=False)

def update():
    if ghost.enabled and mouse.hovered_entity:
        ghost.position = mouse.world_point
        ghost.rotation = GamePlayer.rotation
    SelectedToolText.text = f"Tool: {SelectedGate}"
    
    
LastKey = ''
LastTime = 0
DTS = 0.3

SelectedPin = None

# lord forgive me for the 3 seperate left mouse down calls here
def input(key):
    global SelectedPin
    global ghost
    global SelectedGate
    global LastKey
    global LastTime
    
    # flying
    if key == 'k':
        GamePlayer.fly = not GamePlayer.fly
    
    
    
    
    
    # here #1
    if key == 'left mouse down':
        if SelectedGate == 'Wire Spool':
            if mouse.hovered_entity and isinstance(mouse.hovered_entity, (InputPin,OutputPin)):
                if SelectedPin is None:
                    SelectedPin = mouse.hovered_entity
                else:
                    if mouse.hovered_entity != SelectedPin:
                        WireActor(SelectedPin, mouse.hovered_entity)
                        SelectedPin = None
    if key == '1':
        ghost.enabled = True
        SelectedGate = 'NAND'
        ghost.model = 'assets/BaseGate'
        
    if key == '2':
        ghost.enabled = True
        SelectedGate = 'Switch'
        ghost.model = 'assets/BaseGate'
        
    if key == '3':
        ghost.enabled = True
        SelectedGate = 'Button'
        ghost.model = 'assets/BaseGate'
        
    if key == 'g':
        ghost.enabled = False
        SelectedGate = 'Wire Spool'
        ghost.model = 'assets/BaseGate'
        
    if key == 'f':
        ghost.enabled = False
        SelectedGate = 'Wire Cutters'
        ghost.model = 'assets/BaseGate'
    
    # STOP! HAMMER TIME!
    if key == 'h':
        ghost.enabled = False
        SelectedGate = 'Hammer'
        ghost.model = 'assets/BaseGate'
        
    if key == 'r':
        ghost.enabled = False
        SelectedGate = 'Resizer'
        ghost.model = 'assets/BaseGate'
        
    if key == 'b':
        ghost.enabled = True
        SelectedGate = 'Board'
        ghost.model = 'assets/PegboardBase'
        
    
    
    # and #2
    if key == 'left mouse down' and ghost.enabled:
        if SelectedGate == 'NAND':
            NandActor(position=ghost.position,rotation=ghost.rotation)
            
        if SelectedGate == 'Switch':
            SwitchActor(position=ghost.position,rotation=ghost.rotation)
            
        if SelectedGate == 'Button':
            ButtonActor(position=ghost.position,rotation=ghost.rotation)
            
        if SelectedGate == 'Board':
            BasePegboard(1,1,position= ghost.position,rotation=ghost.rotation)
    # and #3
    if key == 'left mouse down':
        try:
            if SelectedGate == 'Hammer' and mouse.hovered_entity.type == "PlaceableObject":
                if mouse.hovered_entity:
                    destroy(mouse.hovered_entity)
        except Exception as PlacementException:
            pass
            #leave the debug shit here for now
            #print(f"Action::DeleteObject::Exception : {PlacementException}")
            
        try:
            if mouse.hovered_entity.type == "Board":
                if SelectedGate == 'Resizer':
                    ResizerTool(mouse.hovered_entity)
        except:
            pass
            
    if key == '0':
        ghost.enabled = False
        SelectedGate = None
        



#ground
Entity(model='plane',texture='assets/grass.png',scale=10000,collider='mesh',texture_scale=(1000,1000), double_sided=True)

Sky(texture='sky_sunset')

OpenLogicWorld.run()