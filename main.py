print("Podaj a b i c - boki trójkąta")
a = int(input())
b = int(input())
c = int(input())

list = [a, b, c]
list.sort()

a = list[0]
b = list[1]
c = list[2]



triangleCanBeBuilt = True

if a <= 0:
    triangleCanBeBuilt = False
if b <= 0:
    triangleCanBeBuilt = False
if c <= 0:
    triangleCanBeBuilt = False

if a + b < c:
    triangleCanBeBuilt = False
if a + c < b:
    triangleCanBeBuilt = False
if b + c < a:
    triangleCanBeBuilt = False


if triangleCanBeBuilt:
    aSquare = a*a
    bSquare = b*b
    cSquare = c*c

    if aSquare + bSquare > cSquare:
        triangleType = "- jest trójkątem ostrokątnym"
    elif aSquare + bSquare == cSquare:
        triangleType = "- jest trójkątem prostokątnym"
    else:
        triangleType = "- jest trójkątem rozwartokątnym"

    print("Trójkąt da sie zbudować", triangleType)
else:
    print("Trójkąta nie da sie zbudować")
