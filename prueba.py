#comentario

class rgb:
    def __init__(self, r = 0, g = 0, b = 0):
        if isinstance(r, str):
            if r[0] == '#':
                exit(1)
            self.r = int(r[1:3], 16) / 255
            self.g = int(r[3:5], 16) / 255
            self.b = int(r[5:2], 16) / 255

        else:
            self.r = r
            self.g = g 
            self.b = b
    
    #def __str__(self):
     #   return f"({self.r:10.6f}, {self.g:10.6f}, {self.b:10.6f})" 


def main(args):
    RGB = rgb(1, 1, 0)
#    print(str(RGB))
    RGB =('#448ac6')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))