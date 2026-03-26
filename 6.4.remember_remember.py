from PIL import Image

def rember_remeber(img):
    code=""
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            if pixels[x, y] < 5:
                code+=chr(y)
                break
    return code

if __name__ == "__main__":
    img = Image.open("resources/code.png")
    print(rember_remeber(img))
