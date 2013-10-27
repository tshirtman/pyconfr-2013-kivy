from pyobjus import autoclass

def run():
    Bridge = autoclass('bridge')
    br = Bridge.alloc().init()
    br.motionManager.setAccelerometerUpdateInterval_(0.1)
    br.startAccelerometer()

    for i in range(10000):
        print 'x: {0} y: {1} z: {2}'.format(br.ac_x, br.ac_y, br.ac_z)


if __name__ == "__main__":
    run()
