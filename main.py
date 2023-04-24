def on_button_pressed_a():
    global num
    num += 1
    if num == 10:
        num = 0
    basic.show_string("" + str((num)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global guess, count, num
    if count == 0:
        guess = convert_to_text(num)
    else:
        guess = "" + guess + convert_to_text(num)
    count += 1
    num = -1
    if count > 2:
        basic.show_string("Your Guess:" + guess)
        if guess == key:
            basic.show_icon(IconNames.YES)
        else:
            basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

num = 0
count = 0
guess = ""
key = ""
key = "123"
guess = ""
count = 0
num = -1

def on_forever():
    pass
basic.forever(on_forever)
