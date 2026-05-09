from ursina import *
from GateActorEngine import *
import tkinter as tk
from tkinter import simpledialog

class ResizerTool:
    def __init__(self,board):
        root = tk.Tk()
        root.withdraw()
        
        Height = simpledialog.askstring(title="Resizer", prompt="Enter pegboard HEIGHT")
        Width = simpledialog.askstring(title="Resizer", prompt="Enter pegboard WIDTH")
        
        board.world_scale_x = int(Height)
        board.world_scale_z = int(Width)

class BasePegboard(Entity):
    def __init__(self,sizex,sizez,**kwargs):
        super().__init__(
        
            model='assets/PegboardBase',
            texture='white_cube',
            type="Board",
            texture_scale=(sizex,sizez),
            world_scale=(sizex,1,sizez),
            collider='box',
            **kwargs
        )
        
    def update(self):
        self.texture_scale = (self.world_scale_x,self.world_scale_z)
       