import uiautomator2
from random import uniform
from dgfbot.utils import COLOR_REPORT, COLOR_ENDC, COLOR_FAIL
from time import sleep
from enum import Enum, unique
from typing import Optional

UI_TIMEOUT_LONG = 5
UI_TIMEOUT_SHORT = 1

class DeviceFacade:

    def __init__(self, device, ) -> None:
        self.device = device

    def open_app(self, app_id):
        self.device.app_start(app_id)

    def find(self, *args, **kwargs):
        try:
            view = self.device(*args, **kwargs)
        except uiautomator2.JSONRPCError as e:
            raise DeviceFacade.JsonRpcError(e)
        return DeviceFacade.View(is_old=False, view=view, device=self)


    def screen_click_by_coordinates(self, left, top):
            self.device.click(left, top)

    def screenshot(self, path):
            self.device.screenshot(path)

    class View:
        device = None
        viewV1 = None  # uiautomator
        view = None  # uiautomator2

        def __init__(self, is_old, view, device):
            self.device = device
            selfview = view

        def __iter__(self):
            children = []
            try:
                for item in self.view:
                    children.append(DeviceFacade.View(is_old=False, view=item, device=self.device))
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)
            return iter(children)

        def child(self, *args, **kwargs):
            try:
                view = self.view.child(*args, **kwargs)
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)
            return DeviceFacade.View(is_old=False, view=view, device=self.device)

        def right(self, *args, **kwargs) -> Optional['DeviceFacade.View']:
            try:
                view = self.view.right(*args, **kwargs)
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)
            return DeviceFacade.View(is_old=False, view=view, device=self.device)

        def left(self, *args, **kwargs):
            try:
                view = self.view.left(*args, **kwargs)
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)
            return DeviceFacade.View(is_old=False, view=view, device=self.device)

        def up(self, *args, **kwargs):
            try:
                view = self.view.up(*args, **kwargs)
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)
            return DeviceFacade.View(is_old=False, view=view, device=self.device)

        def down(self, *args, **kwargs):
            try:
                view = self.view.down(*args, **kwargs)
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)
            return DeviceFacade.View(is_old=False, view=view, device=self.device)

        def click(self, mode=None, ignore_if_missing=False):
            if ignore_if_missing and not self.exists(quick=True):
                return

            mode = DeviceFacade.Place.WHOLE if mode is None else mode
            if mode == DeviceFacade.Place.WHOLE:
                x_offset = uniform(0.15, 0.85)
                y_offset = uniform(0.15, 0.85)

            elif mode == DeviceFacade.Place.LEFT:
                x_offset = uniform(0.15, 0.4)
                y_offset = uniform(0.15, 0.85)

            elif mode == DeviceFacade.Place.CENTER:
                x_offset = uniform(0.4, 0.6)
                y_offset = uniform(0.15, 0.85)

            elif mode == DeviceFacade.Place.RIGHT:
                x_offset = uniform(0.6, 0.85)
                y_offset = uniform(0.15, 0.85)

            else:
                x_offset = 0.5
                y_offset = 0.5

            try:
                self.view.click(UI_TIMEOUT_LONG, offset=(x_offset, y_offset))
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)

        def long_click(self):
            try:
                self.view.long_click()
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)

        def double_click(self, padding=0.3):
            """
            Double click randomly in the selected view using padding
            padding: % of how far from the borders we want the double click to happen.
            """

            self._double_click_v2(padding)

        def scroll(self, direction):
            try:
                if direction == DeviceFacade.Direction.TOP:
                    self.view.scroll.toBeginning(max_swipes=1)
                else:
                    self.view.scroll.toEnd(max_swipes=1)
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)

        def swipe(self, direction):
            try:
                if direction == DeviceFacade.Direction.TOP:
                    self.view.fling.toBeginning(max_swipes=5)
                else:
                    self.view.fling.toEnd(max_swipes=5)
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)

        def exists(self, quick=False):
            try:
                return self.view.exists(UI_TIMEOUT_SHORT if quick else UI_TIMEOUT_LONG)
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)

        def wait(self):
            try:
                return self.view.wait(timeout=UI_TIMEOUT_LONG)
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)

        def get_bounds(self):
            try:
                return self.view.info['bounds']
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)

        def get_text(self, retry=True):
            max_attempts = 1 if not retry else 3
            attempts = 0

            while attempts < max_attempts:
                attempts += 1
                try:
                    text = self.view.info['text']
                    if text is None:
                        if attempts < max_attempts:
                            print(COLOR_REPORT + "Could not get text. "
                                                    "Waiting 2 seconds and trying again..." + COLOR_ENDC)
                            sleep(2)  # wait 2 seconds and retry
                            continue
                    else:
                        return text
                except uiautomator2.JSONRPCError as e:
                    raise DeviceFacade.JsonRpcError(e)

            print(COLOR_FAIL + f"Attempted to get text {attempts} times. You may have a slow network or are "
                               f"experiencing another problem." + COLOR_ENDC)
            return ""

        def get_selected(self) -> bool:
            try:
                return self.view.info["selected"]
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)

        def is_enabled(self) -> bool:
            try:
                return self.view.info["enabled"]
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)

        def is_focused(self) -> bool:
            try:
                return self.view.info["focused"]
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)

        def set_text(self, text):
            try:
                self.view.set_text(text)
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)
        
        def _double_click_(self, padding):
            visible_bounds = self.get_bounds()
            horizontal_len = visible_bounds["right"] - visible_bounds["left"]
            vertical_len = visible_bounds["bottom"] - visible_bounds["top"]
            horizintal_padding = int(padding * horizontal_len)
            vertical_padding = int(padding * vertical_len)
            random_x = int(
                uniform(
                    visible_bounds["left"] + horizintal_padding,
                    visible_bounds["right"] - horizintal_padding,
                )
            )
            random_y = int(
                uniform(
                    visible_bounds["top"] + vertical_padding,
                    visible_bounds["bottom"] - vertical_padding,
                )
            )
            time_between_clicks = uniform(0.050, 0.200)
            try:
                self.device.deviceV2.double_click(random_x, random_y, duration=time_between_clicks)
            except uiautomator2.JSONRPCError as e:
                raise DeviceFacade.JsonRpcError(e)

    @unique
    class Place(Enum):
        INTERN = 0
        CS = 1
        FS = 2
        AM = 3
        M = 4
        DGM = 5
        GM = 6
        D = 7
        MD = 8
        SMD = 9
        VP = 10