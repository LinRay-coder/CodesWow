mc=int(input())
sx=1
csgo=0
sb=2
for i in range(mc):
    csgo+=sx
    print("Floor:",i,"Bricks:",sx)
    sx+=sb
    sb+=1
print("Total:",csgo)
