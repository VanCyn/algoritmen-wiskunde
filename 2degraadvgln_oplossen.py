from math import sqrt


def vgl(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        print("D=", d, ">0 =) 2 wortels")
        x1 = (-b - sqrt(d)) / 2 * a
        x2 = (-b + sqrt(d)) / 2 * a
        return "x1={0:1.3f} en x2 ={1:1.3f}".format(x1, x2)
    elif d == 0:
        print("D=", d, "=) 1 wortel")
        x1 = -b / 2 * a
        return "x1 = {0:1.3f}".format(x1)
    else:
        print("D=", d, "<0 =) geen reële wortels")


a = int(input("geef de a van de vgl ax²+bx+c in:"))
b = int(input("geef de b van de vgl ax²+bx+c in:"))
c = int(input("geef de c van de vgl ax²+bx+c in:"))

vgl(a, b, c)
