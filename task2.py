import turtle
import math

# Функція для малювання дерева Піфагора
def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return
    
    t.forward(branch_length)
    
    pos = t.position()
    angle = t.heading()
    
    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)
    
    t.setposition(pos)
    t.setheading(angle)
    
    # Права гілка
    t.right(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)
    
    t.setposition(pos)
    t.setheading(angle)

# Основна функція
def main():
    screen = turtle.Screen()
    screen.title("Pythagoras Tree Fractal")
    
    t = turtle.Turtle()
    t.speed(0) 
    t.left(90)
    
    level = int(input("Введіть рівень рекурсії: "))
    
    draw_pythagoras_tree(t, 100, level)
    
    turtle.done()

if __name__ == "__main__":
    main()
