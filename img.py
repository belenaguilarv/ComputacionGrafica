from rgb import rgb
from PIL import Image

def main(args):
    img = Image.open('ruta')
    px = img.load()
    px[100, 120] = (0, 0)
    img.show()
    return 0

    if __name__ == '__main__':
        import sys
