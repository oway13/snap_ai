import keypress as kp
import time
import neural_net as nn
from run_generation import score
from screengrab import snap_grab
KEYNAMES = ["W","A","S","D","Q","E","SHIFT","ENTER","R","F","T","Y","G","H","UP","LEFT","RIGHT","DOWN","NK"]


test_nn = nn.snap_nn()
test_nn.random_values()
print("Paused")

while(True):
    keys = kp.key_check()
    if not end:
        if not paused:
            action = test_nn.get_output(snap_grab())
            key_press = kp.KEYS[action[0]]
            print("Do Action "+str(KEYNAMES[action[0]])+" with certainty: "+str(action[1]))
            if key_press != "NK":
                kp.TapKey(key_press)
        if 'M' in keys:
            if paused:
                paused = False
                print('Unpausing in 5 Seconds')
                time.sleep(1)
                print('4')
                time.sleep(1)
                print('3')
                time.sleep(1)
                print('2')
                time.sleep(1)
                print('1')
                time.sleep(1)
                print('Unpaused!')
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)
    else:
        score(1)
        break
    if 'N' in keys:
        end = True
    if 'B' in keys:
        break
        
