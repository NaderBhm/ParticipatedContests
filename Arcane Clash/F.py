ch = input()
heavy = "heavy"
metal = "metal"
count = 0
metal_count = 0
heavy_pos = []
metal_pos = []
i = 0
while (i:=ch.find(heavy, i))!=-1:
    heavy_pos.append(i)
    i+=len(heavy)
i = 0
while (i:=ch.find(metal, i))!=-1:
    metal_pos.append(i)
    i+=len(metal)
j = 0
for heavy_pos in heavy_pos:
    while j<len(metal_pos) and metal_pos[j]<heavy_pos:
        j+=1
    count+=len(metal_pos) - j
print(count)