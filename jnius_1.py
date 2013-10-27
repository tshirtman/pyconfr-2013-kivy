from jnius import autoclass

PS = autoclass('org.renpy.android.PythonService')
context = PS.mService
VB = context.getSystemService(PS.VIBRATOR_SERVICE)

def vibrate(duration, interval, times):
    pattern = [int(interval), int(duration)]
    VB.vibrate(pattern * int(times) , -1)
