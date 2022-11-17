def wall(a, b):

    area = a * b
    return area



def paint():
    wall_height = float(input("Enter height of the wall in metres: "))
    wall_lenght = float(input("Enter lenght of the wall in metres: "))

    paint_needed = wall(wall_lenght, wall_height) / 6
    return paint_needed


print(paint())

