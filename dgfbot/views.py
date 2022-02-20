from dgfbot.device_facade import *
from dgfbot.utils import *
import numpy

'''
hiring process view
fired view

CS 640x1520
'''

employess = {'cs':'yes',
}


class mainView():

    def __init__(self, device: DeviceFacade):
        self.device = device
        self.screenPath = 'screenshots\\test2.png'
        # self.screenPath = 'screenshots\\screenshot.png'
        self.mainViewReferancePath = 'screenshots\\referance.png'

#TODO fix check image and _get_health_bar
    def is_visible(self) -> bool:
        width, height = self._get_health_bar_location()
        return similar_arr_in_list(checkImage(self.screenPath,width,height),self.work_alert_colors )

    def _get_health_bar_location(self):
        width = 250 
        length = 400
        return length, width 
# 
    def employeeLocations(self,device):
        width, height = getDimensions(device)
        first_row_val = int(.66 * height) - 30
        second_row_val = int(.725 * height) - 460
        third_row_val = 1020 - 40
        return  { 'INTERN':[900,first_row_val],
            'CS' :[673,first_row_val],
            'FS':[420,first_row_val],
            'AM': [166,first_row_val],
            'M':[915,second_row_val],
            'DGM':[665,second_row_val],
            'GM':[420,second_row_val],
            'D' :[166,second_row_val],
            'MD':[900,third_row_val],
            'SMD':[570,third_row_val],
            'VP':[200,third_row_val]}

    work_alert_colors = [
    #yellow
    numpy.array([254, 230, 129, 255]),
    #red
    numpy.array([227,  43,  56, 255]),
    #red
    numpy.array([227,  32,  32, 255]),
    #red
    numpy.array([247,  32,  32, 255]),

    ]

def testing(device: DeviceFacade, view: mainView):
    with Image.open("screenshots\\test2.png") as im:
        #250, 400
        width, height = view._get_health_bar_location()
        r = 30
        draw = ImageDraw.Draw(im)


        for location in view.employeeLocations(device).items():
            r = 18
            x = location[1][0]
            y = location[1][1]
            draw.ellipse([(x-r, y-r), (x+r, y+r)],fill='red', width=10)


        print(width,height)
        draw.ellipse([(width-r, height-r), (width+r, height+r)],fill='yellow', width=10)
        im.show()