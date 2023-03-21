import math
from triangle_drawer import Triangle
from fuzzywuzzy import process
func = input(("Enter the trigonometric ratio (sin/sine, cos/cosine or tan/tangent): "))

sides = {}
sides.update(dict.fromkeys(["sin", "sine"], ["perpendicular", "hypotenuse"]))
sides.update(dict.fromkeys(["cos", "cosine"], ["base", "hypotenuse"]))
sides.update(dict.fromkeys(["tan", "tangent"], ["perpendicular", "base"])) #could probably improve this

list_of_ratios = list(sides)
searched_ratio = process.extract(func, list_of_ratios)

if searched_ratio[0][1] >= 60:
    print(f"Not a valid ratio, perhaps you made a typo but meant '{searched_ratio[0][0]}'")
    exit()

elif searched_ratio[0][1] < 60:
    print("Please ONLY type the ratio as hinted in the prompt")
    exit()

chosen_sides_by_ratio = sides[func] 
try:
    side1 = eval((input(f"Input {chosen_sides_by_ratio[0]} measurement: ")))
    side2 = eval((input(f"Input {chosen_sides_by_ratio[1]} measurement: ")))
except NameError:
    print("Make sure you ONLY input the integer/decimal value of the measure of the side.")
    exit()
decimal_value = side1/side2

ratios = {}
ratios.update(dict.fromkeys(["sin", "sine"], math.asin(decimal_value)))
ratios.update(dict.fromkeys(["cos", "cosine"], math.acos(decimal_value)))
ratios.update(dict.fromkeys(["tan", "tangent"], math.atan(decimal_value))) #and this, somehow

radian = ratios[func]
theta = radian * 180/math.pi

print(f"{round(theta, 2)} degrees (at ∠B)")
Triangle(side1, side2, angle=90.0).draw()