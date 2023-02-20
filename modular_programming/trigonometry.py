import math
def get_sine(x):
    #x is in degrees
    angle_rad=math.radians(x)
    angle_sine=math.sin(angle_rad)
    return angle_sine

def get_tan(x):
    angle_rad=math.radians(x)
    angle_tan=math.tan(angle_rad)
    return angle_tan

def get_cos(x):
    angle_rad=math.radians(x)
    angle_cos=math.cos(angle_rad)
    return angle_cos 
