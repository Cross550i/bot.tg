def draw_triangle(fill, base):
    for i in range(base):
        while i < base:
            print(i * "*")
            i+=1

draw_triangle("*", 6)
