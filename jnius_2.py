from jnius import autoclass
PS = autoclass('org.renpy.android.PythonService')
PM = autoclass('android.os.PowerManager')
MP = autoclass('android.media.MediaPlayer')
power_manager = context.getSystemService(PS.POWER_SERVICE)


def wake_up(unlock=False):
    if power_manager.isScreenOn():
        wl = None
    else:
        wl = power_manager.newWakeLock(PM.SCREEN_BRIGHT_WAKE_LOCK | PM.FULL_WAKE_LOCK | PM.ACQUIRE_CAUSES_WAKEUP, "TAG")
        wl.acquire()

    if unlock:
        keyguard = context.getSystemService(PS.KEYGUARD_SERVICE)
        kgl = keyguard.newKeyguardLock('TAG')
        kgl.disableKeyguard()
        kgl.reenableKeyguard()

    if wl:
        wl.release()
