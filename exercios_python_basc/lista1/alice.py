a,b = input().split(" ")

a = float(a)
b = float(b)

intA = int(a)
decA = a - intA

intB = int(b)
decB = b - intB

segA = intA * 60 + decA * 100
segB = intB * 60 + decB * 100



if segA - segB >= 0:
    t_seg = segA - segB
    restoMin = int(t_seg/60) 
    restoSeg = int(round((t_seg/60 - restoMin) * 60))

t_sobra = restoMin + restoSeg/100

print(t_sobra)
