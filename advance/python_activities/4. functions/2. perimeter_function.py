def rect_perimeter(length,width):
    perimeter = (2*length) + (2*width)
    return perimeter

l1 = 8
w1 = 10
l2 = 11
w2 = 3

perimeter1 = rect_perimeter(l1,w1)
print("Rectangle 1: Length =", l1, "Width =", w1)
print ("Perimeter:", perimeter1)

perimeter2 = rect_perimeter(l2,w2)
print("Rectangle 2: Length =", l2, "Width =", w2)
print ("Perimeter:", perimeter2)
