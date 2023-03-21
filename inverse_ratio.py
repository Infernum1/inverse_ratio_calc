import math
from triangle_drawer import Triangle

func = input(("Enter the trigonometric ratio (sin/sine, cos/cosine or tan/tangent): "))

sides = {}
sides.update(dict.fromkeys(["sin", "sine"], ["perpendicular", "hypotenuse"]))
sides.update(dict.fromkeys(["cos", "cosine"], ["perpendicular", "hypotenuse"]))
sides.update(dict.fromkeys(["tan", "tangent"], ["perpendicular", "hypotenuse"])) #could probably improve this

if func not in sides:
    print("Please ONLY type the ratio as hinted in the prompt")
    exit()

chosen_sides_by_ratio = sides[func] 

side1 = eval((input(f"Input {chosen_sides_by_ratio[0]} measurement: ")))
side2 = eval((input(f"Input {chosen_sides_by_ratio[1]} measurement: ")))

decimal_value = side1/side2

ratios = {}
ratios.update(dict.fromkeys(["sin", "sine"], math.asin(decimal_value)))
ratios.update(dict.fromkeys(["cos", "cosine"], math.acos(decimal_value)))
ratios.update(dict.fromkeys(["tan", "tangent"], math.atan(decimal_value))) #and this, somehow

radian = ratios[func]
theta = radian * 180/math.pi

print(f"{round(theta, 2)} degrees (at Angle B)")
Triangle(side1, side2, angle=90.0).draw()