import turtle


def koch_curve(t, order, length):
    if order == 0:
        t.fd(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, length / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 2 / 3 ** 0.5)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == '__main__':
    try:
        recursive_level = int(input("Enter the level of recursion (from 0 to 5): "))

        if recursive_level < 0 or recursive_level > 5:
            raise ValueError

        draw_koch_curve(recursive_level)
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 5.")
