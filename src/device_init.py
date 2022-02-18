import uiautomator2

def device_init(app_id, restart=False):
    device = connect_device(restart)
    sess = startApp(device, app_id, restart)
    return device, sess

def connect_device(restart):
    try:
        return uiautomator2.connect()
    except RuntimeError as err:
        print(f'\nRuntime Error: {err}')
    except Exception as err:
        print(f'\nError: {err}')

def startApp(device, app_id, forceRestart):
    if forceRestart:
        device.app_stop_all()
        device.app_start(app_id)
        return device.session(app_id, attach=True)
 
    else:
        try:
            # launch app if not running, skip launch if already running
            sess = device.session(app_id, attach=True)
            # raise SessionBrokenError if not running
            sess = device.session(app_id, attach=True, strict=True)
            return sess
        except SessionBrokenError as err:
            print('\napp not running')

