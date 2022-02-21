import uiautomator2


def device_init(app_id, restart=False):
    device = connect_device()
    # device.unlock()

    # deprecated feature that I want to make work
    sess = startApp(device, app_id, restart)
    return device


def connect_device():
    try:
        return uiautomator2.connect()
    except RuntimeError as err:
        print(f"\nRuntime Error: {err}")
    except Exception as err:
        print(f"\nError: {err}")


def startApp(device, app_id, forceRestart=False):
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
            print("\napp not running")
