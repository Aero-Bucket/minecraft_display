from PIL import Image
from template import *


def pixels_to_hex(px, x, y):
    result = 0

    if px[x,y] > 0:
        result += 8
    if px[x+1,y] > 0:
        result += 4
    if px[x+2,y] > 0:
        result += 2
    if px[x+3,y] > 0:
        result += 1

    return result


# for testing only
def verify(arr, w, h):
    result = Image.new("1", (w,h))
    px = result.load()
    index = 0

    for a in arr:
        count = a[1] * 4
        data = bin(a[0])[2:].rjust(4, "0")
        for j in range(count):
            if data[j%4] == "1":
                px[(index+j)%w, (index+j)//w] = 255
        index += count

    return result


item_arr=[]
with Image.open("output.png") as img:
    width, height = img.size

    if width % 4 != 0:
        print("Invalid Image")
        exit(1)

    px = img.load()
    last_value = pixels_to_hex(px, 0, 0)
    count = 0

    for y in range(height):
        for x in range(0, width, 4):
            current_value = pixels_to_hex(px, x, y)

            if current_value == last_value and count < 16:
                count += 1
            else:
                item_arr.append((last_value, count))
                last_value = current_value
                count = 1 

    item_arr.append((current_value, count))

    # for testing only
    # verify(item_arr, width, height).save("verify.png")
    # print(item_arr)
    # print(f"{len(item_arr)} slots")
    # print(f"{sum([i[1] for i in item_arr])} items")



boxes = []  # many shulker box tags
for s in range(len(item_arr) // 27 + 1):
    boxes.append(SHULKER_BOX.format(
            text=f"{s//27 + 1} - {s%27 + 1}",
            items=",".join(     # packing many banners to a box
                [
                    CHEST_ITEM.format(
                        slot=i,
                        id=BANNERS[bn[0]]["id"],
                        count=bn[1],
                        tag=BANNERS[bn[0]]["tag"]
                    )
                    for i, bn in enumerate(item_arr[27*s:27*s+27])  # 27 as a group
                ]
            )
        )
    )


with open(f"chest.mcfunction", "w") as f:
    for c in range(len(boxes) // 27 + 1):
        cmd = CHEST.format(
            text=c+1,
            items=",".join(     # packing many boxes to a chest
                [
                    CHEST_ITEM.format(
                        slot=i,
                        id="shulker_box",
                        count=1,
                        tag=bx
                    ) 
                    for i,bx in enumerate(boxes[27*c:27*c+27])
                ]
            )
        )
        f.write(f"give @s {cmd}\n")

