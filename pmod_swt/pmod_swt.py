from DesignSpark.Pmod.HAT import createPmod
import time

if __name__ == '__main__':
    
    SWT = createPmod('SWT','JAA')
    time.sleep(0.1)
    
    try:
        while True:
            print(SWT.GetStatus(1),SWT.GetStatus(2),SWT.GetStatus(3),SWT.GetStatus(4))
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        SWT.cleanup()
