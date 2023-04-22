input.onButtonPressed(Button.A, function () {
    num += 1
    if (num == 10) {
        num = 0
    }
    basic.showString("" + (num))
})
input.onButtonPressed(Button.B, function () {
    if (count == 0) {
        guess = convertToText(num)
    } else {
        guess = "" + guess + convertToText(num)
    }
    count += 1
    num = -1
    if (count > 2) {
        basic.showString("Your Guess:" + guess)
        if (guess == key) {
            basic.showIcon(IconNames.Yes)
        } else {
            basic.showIcon(IconNames.No)
        }
    }
})
let num = 0
let count = 0
let guess = ""
let key = ""
key = "123"
guess = ""
count = 0
num = -1
basic.forever(function () {
	
})
