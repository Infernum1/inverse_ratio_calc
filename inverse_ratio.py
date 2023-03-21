import math
from triangle_drawer import Triangle

func = input(("Enter the trigonometry ratio (sin, cos or tan): "))

sides = {"sin": ["perpendicular", "hypotenuse"], "cos": ["base", "hypotenuse"], "tan": ["perpendicular", "base"]}

chosen_sides_by_ratio = sides[func] 

side1 = eval((input(f"Input {chosen_sides_by_ratio[0]} measurement: ")))
side2 = eval((input(f"Input {chosen_sides_by_ratio[1]} measurement: ")))

decimal_value = side1/side2

ratios = {"sin" : math.asin(decimal_value), "cos" : math.acos(decimal_value), "tan" : math.atan(decimal_value)}

radian = ratios[func]
theta = radian * 180/math.pi

print(f"{round(theta, 2)} degrees (at Angle B)")
Triangle(side1, side2, angle=90.0).draw()

