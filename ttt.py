import turtle

t = turtle.Turtle()

# def drawSpiral(t, lineLen):
#     if lineLen > 0:
#         t.forward(lineLen)
#         t.right(90)
#         drawSpiral(t, lineLen - 5)

# drawSpiral(t, 300)

def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(40)
        tree(branch_len - 15)
        t.left(80)
        tree(branch_len - 15)
        t.right(40)
        t.backward(branch_len)

t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(75)
t.hideturtle()

turtle.done()