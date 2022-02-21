from dgfbot.device_facade import *
from dgfbot.utils import similar_arr_in_list, checkImage, ImageDraw, Image
import numpy

"""
hiring process view
dialog view

CS 640x1520
"""

screenPath = "screenshots\\screenshot.png"


class mainView:
    def __init__(self, device: DeviceFacade):
        self.device = device
        self.dimensions = (1080, 2316)
        # TODO Adjust dimension to advice
        # self.dimensions = getDimensions(self.device)

    # TODO fix check image and _get_health_bar
    def is_visible(self) -> bool:
        width, height = self._get_health_bar_location()
        return similar_arr_in_list(
            checkImage(screenPath, width, height), self.workers_alert_indicators
        )

    def _get_health_bar_location(self) -> tuple[int, int]:
        height = 250
        width = 400
        return (width, height)

    #
    def employeeLocations(self) -> list[str:list]:
        _, height = self.dimensions
        first_row_val = int(0.66 * height) - 30
        second_row_val = int(0.725 * height) - 460
        third_row_val = 1020 - 40

        return {
            "INTERN": [900, first_row_val],
            "CS": [673, first_row_val],
            "FS": [420, first_row_val],
            "AM": [180, first_row_val],
            "M": [955, second_row_val],
            "DGM": [715, second_row_val],
            "GM": [430, second_row_val],
            "D": [190, second_row_val],
            "MD": [900, third_row_val],
            "SMD": [570, third_row_val],
            "VP": [200, third_row_val],
        }

    def testing(self):
        with Image.open(screenPath) as im:
            draw = ImageDraw.Draw(im)
            for location in self.employeeLocations().items():
                r = 18
                x = location[1][0]
                y = location[1][1]
                draw.ellipse([(x - r, y - r), (x + r, y + r)], fill="red", width=10)
        im.show()

    workers_alert_indicators = [
        # yellow
        numpy.array([254, 230, 129, 255]),
        # yellow
        numpy.array([255, 230, 129, 255]),
        # red
        numpy.array([227, 43, 56, 255]),
        # red
        numpy.array([228, 43, 56, 255]),
        # health bar red
        numpy.array([227, 32, 32, 255]),
        # health bar red
        numpy.array([247, 32, 32, 255]),
        # green
        numpy.array([0, 230, 0, 255]),
        # green
        numpy.array([0, 43, 0, 255]),
    ]


class hiringView:
    def __init__(self, device: DeviceFacade):
        self.device = device

    def is_visible(self) -> bool:
        width, height = self._get_hiring_building()
        return similar_arr_in_list(
            checkImage(screenPath, width, height), self.workers_alert_indicators
        )

    def _get_hiring_indicator():
        width = 540
        height = 20
        return (width, height)

    hiring_view_indicators = [numpy.array(169, 173, 172, 255)]
