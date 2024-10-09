from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Tuple, Union, Optional, Any, NoReturn

Color = Tuple[int, int, int]

@dataclass
class Constant:
    # string
    name: str = 'first try'
    
    # coloc
    black: Color= (0, 0, 0)
    white: Color= (255, 255, 255)

class ColorEnum(Enum):
    white: Color = (255, 255, 255)
    black: Color= (0, 0, 0)
    red: Color = (255, 0, 0)
    green: Color = (0, 255, 0)
    blue: Color = (0, 0, 255)
