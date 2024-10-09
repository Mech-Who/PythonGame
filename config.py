from typing import List, Dict, Tuple, Union, Optional, Any, NoReturn

class Config:
    screen_size: Tuple[int, int] = [1280, 720]
    background_color: str = 'purple' 
    limit_fps: int = 60
    ball_speed: Tuple[int, int] = [2, 2]
    default_font_size: int = 20
