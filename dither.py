import numpy as np
from PIL import Image, ImageEnhance

RESOLUTION = (192, 144)

# each tuple: (relative row coordinate, relative column coordinate, weighting)
def floyd(r, c):
    return [                                  (r, c+1, 7/16),
            (r+1, c-1, 3/16), (r+1, c, 5/16), (r+1, c+1, 1/16)
        ]


def jarvis(r, c):
    return [                                                    (r, c+1, 7/48),   (r, c+2, 5/48),
            (r+1, c-2, 3/48), (r+1, c-1, 5/48), (r+1, c, 7/48), (r+1, c+1, 5/48), (r+1, c+2, 3/48),
            (r+2, c-2, 1/48), (r+2, c-1, 3/48), (r+2, c, 5/48), (r+2, c+1, 3/48), (r+2, c+2, 1/48)
        ]

def atkinson(r, c):
    return [                                (r, c+1, 1/8),   (r, c+2, 1/8),
            (r+1, c-1, 1/8), (r+1, c, 1/8), (r+1, c+1, 1/8),
                             (r+2, c, 1/8)
        ]


def dither(im) -> np.ndarray:
    arr = np.array(im, dtype=float) / 255
    width, height = im.size

    for r in range(height):
        for c in range(width):

            err = arr[r,c] - round(arr[r,c])
            
            for i in atkinson(r,c):     # change error diffusion map here
                if i[0] < height and i[1] < width:
                    arr[i[0], i[1]] += err * i[2]
            
            arr[r,c] = round(arr[r,c])

    arr = np.array(arr / np.max(arr) * 255, dtype=np.uint8)
    return Image.fromarray(arr).convert("1")


with Image.open("input.png") as img:

    img = img.convert("L")

    cenhancer = ImageEnhance.Contrast(img)
    img = cenhancer.enhance(1.4)
    benhancer = ImageEnhance.Brightness(img)
    img = benhancer.enhance(0.9)

    img = dither(img)

    # padding
    width, height = img.size
    if abs(height / width - 3/4) > 0.1:
        if width > height:
            new_width, new_height = width, int(width * 3/4)
        else:
            new_width, new_height = int(height * 4/3), height
        bg = Image.new("1", (new_width, new_height))
        bg.paste(img)
        img = bg
        print("Not in 4:3, Padding Added")
    
    # must use nearest neighbour on pixel art
    img = img.resize(RESOLUTION, Image.NEAREST)
    img.save("output.png")