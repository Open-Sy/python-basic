def volume(width = 3, length= 3 , heigth= 3):
    volume = width*length*width 
    return volume

def volume_args(width, length , heigth):
    volume = width*length*width 
    return volume

if __name__ == '__main__':

    # kw args

    v = volume()
    print('The volume is ', v)

    v = volume(width=5, heigth=5, length=5)
    print('The volume is ', v)

    # args
    # if we pass the argumetns not as keyword arguments, calling the function without passing any arguments will lead to error.
    #v = volume_args()