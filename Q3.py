class Card:
    def __init__(self):
        self.color = ""
        self.symbol = ""
        self.shading = ""
        self.number = 0

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def set_shading(self, shading):
        self.shading = shading

    def get_shading(self):
        return self.shading

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number


def is_set(card1, card2, card3):
    check_color = False
    check_symbol = False
    check_number = False
    check_shading = False
    check = False

    # Check Colors
    if (
        card1.get_color() != card2.get_color()
        and card2.get_color() != card3.get_color()
        and card1.get_color() != card3.get_color()
    ):
        check_color = True
    if (
        card1.get_color() == card2.get_color()
        and card2.get_color() == card3.get_color()
        and card1.get_color() == card3.get_color()
    ):
        check_color = True

    # Check Symbols
    if (
        card1.get_symbol() != card2.get_symbol()
        and card2.get_symbol() != card3.get_symbol()
        and card1.get_symbol() != card3.get_symbol()
    ):
        check_symbol = True
    if (
        card1.get_symbol() == card2.get_symbol()
        and card2.get_symbol() == card3.get_symbol()
        and card1.get_symbol() == card3.get_symbol()
    ):
        check_symbol = True

    # Check Shadings
    if (
        card1.get_shading() != card2.get_shading()
        and card2.get_shading() != card3.get_shading()
        and card1.get_shading() != card3.get_shading()
    ):
        check_shading = True
    if (
        card1.get_shading() == card2.get_shading()
        and card2.get_shading() == card3.get_shading()
        and card1.get_shading() == card3.get_shading()
    ):
        check_shading = True

    # Check Numbers
    if (
        card1.get_number() != card2.get_number()
        and card2.get_number() != card3.get_number()
        and card1.get_number() != card3.get_number()
    ):
        check_number = True
    if (
        card1.get_number() == card2.get_number()
        and card2.get_number() == card3.get_number()
        and card1.get_number() == card3.get_number()
    ):
        check_number = True

    # Check Set
    if (
        check_number is True
        and check_symbol is True
        and check_color is True
        and check_shading is True
    ):
        check = True

    return check


card1 = Card()
card2 = Card()
card3 = Card()

print("Enter color for 1st card:")
color = input()
card1.set_color(color)
print("Enter symbol for 1st card:")
symbol = input()
card1.set_symbol(symbol)
print("Enter number for 1st card:")
number = int(input())
card1.set_number(number)
print("Enter shading for 1st card:")
shading = input()
card1.set_shading(shading)

print("Enter color for 2nd card:")
color = input()
card2.set_color(color)
print("Enter symbol for 2nd card:")
symbol = input()
card2.set_symbol(symbol)
print("Enter number for 2nd card:")
number = int(input())
card2.set_number(number)
print("Enter shading for 2nd card:")
shading = input()
card2.set_shading(shading)

print("Enter color for 3rd card:")
color = input()
card3.set_color(color)
print("Enter symbol for 3rd card:")
symbol = input()
card3.set_symbol(symbol)
print("Enter number for 3rd card:")
number = int(input())
card3.set_number(number)
print("Enter shading for 3rd card:")
shading = input()
card3.set_shading(shading)

set_check = is_set(card1, card2, card3)

if set_check is True:
    print("Cards form a set!")
else:
    print("Cards do not form a set!")
