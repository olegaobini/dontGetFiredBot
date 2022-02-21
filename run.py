from dgfbot.device_init import device_init
from dgfbot.utils import screenshot, checkImage, similar_arr_in_list, Popen


from dgfbot import views

app_id = 'com.quickturtle.EmployeeSurvival_en'
device = device_init(app_id)
view = views.mainView(device)

def debug(location):
    print(
        location[0],
         similar_arr_in_list(checkImage(view.mainViewReferancePath, location[1][1], location[1][0]), view.work_alert_colors),
          checkImage(view.mainViewReferancePath, location[1][1], location[1][0])
          )
    # view.testing()

def loop():
    screenshot(device, view.screenPath)
    if view.is_visible():
        for location in view.employeeLocations(device).items():
            if similar_arr_in_list(checkImage(view.screenPath, location[1][1], location[1][0]), view.work_alert_colors):
                    print(location[0])
                    Popen(['adb', 'shell', 'input', 'tap', str(location[1][0]- 100) , str(location[1][1]+ 100) ])

while True:
    loop()