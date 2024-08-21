a,b = input().split(" ")

a = float(a)
b = float(b)

intA = int(a)
decA = a - intA

intB = int(b)
decB = b - intB

if decA - decB >= 0:
    t_seg = decA - decB
else:
    intA -= 1
    t_seg = (decA+0.60) - decB

t_min = intA - intB
t_sobra = t_min+round(t_seg,2)

print(t_sobra)