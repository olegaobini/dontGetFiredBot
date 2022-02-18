import uiautomator2

def init(device, app_id):
    device.app_stop_all()
    device = connect_device()
    startApp(device, app_id)
    return device

def connect_device():
    try:
        return uiautomator2.connect()
    except RuntimeError as err:
        print(f'\nRuntime Error: {err}')
    except Exception as err:
        print(f'\nError: {err}')

def startApp(device, app_id):
    device.app_start(app_id)
