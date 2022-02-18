from subprocess import check_output
'''
regular worker view
hiring process view
fired view

CS 640x1520
'''
def getDimensions():
    output = check_output(['adb', 'shell', 'wm', 'size']).strip().strip(b'Physical size: ')
    width, height = [int(x) for x in output.decode().split('x')]
    return width, height

def mainView():
    width, height = getDimensions()
