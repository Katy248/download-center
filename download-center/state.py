DOWNLOADING = False
NOTIFY_FUNC = None


def notify(msg: str):
    if NOTIFY_FUNC == None:
        return
    NOTIFY_FUNC(msg)
