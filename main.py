import turtle
import pandas


FONT = ('Courier', 6, 'bold')
screen = turtle.Screen()
screen.title("Nepal Districts Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-7, 223)
t.color('cyan')
t.write('Knowing Nepal\'s Districts Place Game', font=('Emilys Candy', 10, 'bold'), align='center')
t.goto(-244, -171)
t.color('DarkRed')
t.write('To end game Type: Exit',font=('Comic Sans', 10, 'italic'), align='center')

data = pandas.read_csv("77_districts.csv")
all_districts = data.districts.to_list()
guessed_districts = []

while len(guessed_districts) < 77:
    answer_district = screen.textinput(title=f"{len(guessed_districts)}/77 Districts Correct",
                                    prompt="What's another district's name?").title()

    if answer_district == "Exit":
        missing_districts = [district for district in all_districts if district not in guessed_districts]
        new_data = pandas.DataFrame(missing_districts)
        new_data.to_csv("districts_to_learn.csv")
        break
    if answer_district in all_districts:
        guessed_districts.append(answer_district)
        t = turtle.Turtle()
        t.hideturtle()
        t.color("red")
        t.penup()
        district_data = data[data.districts == answer_district]
        t.goto(int(district_data.x), int(district_data.y))
        t.write(answer_district, font=FONT)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
