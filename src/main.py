import keypress as kp
import time
import neural_net as nn
from screengrab import snap_grab
import numpy as np

#KEYNAMES = ["W","A","S","D","Q","E","SHIFT","R","F","T","Y","G","H","UP","LEFT","RIGHT","DOWN","NK"]
KEYNAMES = ["UP","LEFT","RIGHT","DOWN","Q"]

gen_nn = []

def main():
    #gen_nn = []
    generation = [0,0,0,0,0]

    gen = 1
    #gen_gen_nns()
    #load_gen_nn(gen)
    load_from_top_two(gen)
    while True:
        top = -1
        two = -1
        for i in range(5):
            GG = run_child(i)
            if GG == -1:
                #Save Current Generation
                for i in range(5):
                    gen_nn[i].save_nn(gen, i)
                return
            generation[i] = GG
        print(generation)
        for i in range(5):
            print('Top: '+str(top)+" Two: "+str(two))
            if top == -1:
                top = i
            elif generation[i] > generation[top]: #Get Top 2
                two = top
                top = i
            elif two == -1:
                two = i
            elif generation[i] > generation[two]:
                two = i
        print('Top: '+str(top)+" Two: "+str(two))
        print(str(len(gen_nn)))
        
        #Swap the top two into the first two slots    
##        temp = gen_nn[0]
##        gen_nn[0] = gen_nn[top]
##        gen_nn[top] = temp
##        temp = gen_nn[1]
##        gen_nn[1] = gen_nn[two]
##        gen_nn[two] = temp
        if top == 1 and two == 0:
            gen_nn[top], gen_nn[two] = gen_nn[top], gen_nn[two]
        elif top == 1:
            gen_nn[top], gen_nn[0] = gen_nn[0], gen_nn[top]
            gen_nn[two], gen_nn[1] = gen_nn[1], gen_nn[two]
        else:
            gen_nn[two], gen_nn[1] = gen_nn[1], gen_nn[two]
            gen_nn[top], gen_nn[0] = gen_nn[0], gen_nn[top]
        gen_nn[0].save_nn(gen, 0)
        gen_nn[1].save_nn(gen, 1)


        print("The top two scores of this generation are: Child "+str(top)+": "+str(generation[top])+" and Child "+str(two)+": "+str(generation[two]))
        #First Five generations dedicated to trying things out
        #Top 2 Stay Alive, 3-5
        #Then comes the competition
        #Top 2 Stay Alive
        #3 and 4 Is Bred between 1 and 2, 5 is random for the first generation, ow 5 is bred too
        gen_nn[2] = gen_nn[0].breed(gen_nn[1])
        gen_nn[3] = gen_nn[1].breed(gen_nn[0])
        if gen < 5:
            gen_nn[4].random_values()
        else:
            gen_nn[4] = gen_nn[0].breed(gen_nn[1])
##        gen_nn[4].random_values()
##        gen_nn[4] = gen_nn[4].breed(gen_nn[0])
        gen += 1
        
        
    
def gen_gen_nns():
    for i in range(5):
        gen_nn.append(nn.snap_nn())
        gen_nn[i].random_values()

def load_gen_nn(gen):
    for i in range(5):
        gen_nn.append(nn.snap_nn())
        gen_nn[i].load_nn_from_file(gen, i)

def load_from_top_two(gen):
    gen_nn.append(nn.snap_nn())
    gen_nn[0].load_nn_from_file(gen-1, 0)
    gen_nn.append(nn.snap_nn())
    gen_nn[1].load_nn_from_file(gen-1, 1)
    
    gen_nn.append(nn.snap_nn())
    gen_nn.append(nn.snap_nn())
    gen_nn.append(nn.snap_nn())
    
    gen_nn[2] = gen_nn[0].breed(gen_nn[1])
    gen_nn[3] = gen_nn[1].breed(gen_nn[0])
    if gen < 5:
        gen_nn[4].random_values()
    else:
        gen_nn[4] = gen_nn[0].breed(gen_nn[1])
##    gen_nn[4].random_values()
##    gen_nn[4] = gen_nn[4].breed(gen_nn[0])
        
        
def score2(child):
    #Score Level Completeness
    score = 0
    eee = False
    while(True):
        eee = False
        complete = input("Did the Child complete the Level (y/n)? ")
        if complete == 'y':
            score += 1500
        elif (complete == 'retry'):
            continue
        elif complete == 'n':
            score -= 1500
        else:
            print("Improper Input, Restarting. . .")
            continue
        #Score Remaining Film
        pictures = input("How many pictures were taken? ")
        if (pictures == 'retry'):
            continue
        elif not pictures.isnumeric():
            print("Improper Input, Restarting. . .")
            continue
        pict = int(pictures)
        if pict < 20:
            score +=  pict*30
        elif pict < 40:
            score +=  pict*40
        elif pict < 60:
            score +=  pict*30
        elif pict == 60:
            score +=  pict*20
        
        oakable = input("How many pictures were sent to Oak? ")
        if (oakable == 'retry'):
            continue
        elif not oakable.isnumeric():
            print("Improper Input, Restarting. . .")
            continue
        score += 300*int(oakable)
        #Oak's Oakable Picture Scores
        for i in range(int(oakable)):
            oak = input("Oak's Score for picture "+str(i+1)+"? ")
            if (oak == 'retry'):
                eee = True
                break
            elif not oak.isnumeric():
                print("Improper Input, Restarting. . .")
                eee = True
                break
                
            score += int(oak)
            oak = "0"
        
    ##    report_poke = int(input("Pokemon in Report: "))
    ##    report_score = int(input("Report Score: "))
    ##    generation[child] += report_score+(300*report_poke)
        if eee:
            continue
        break
    print("Child "+str(child)+" scored "+str(score)+" points")
    return score

def score1(child):
    #Score Level Completeness
    score = 0
    eee = False
    while(True):
        eee = False
        complete = input("Did the Child complete the Level (y/n)? ")
        if complete == 'y':
            score += 1500
        elif (complete == 'retry'):
            continue
        elif complete == 'n':
            score += 0
        else:
            print("Improper Input, Restarting. . .")
            continue
        #Score Remaining Film
        pictures = input("How many pictures were taken? ")
        if (pictures == 'retry'):
            continue
        elif not pictures.isnumeric():
            print("Improper Input, Restarting. . .")
            continue
        score+= int(pictures)*30
        
        oakable = input("How many pictures were sent to Oak? ")
        if (oakable == 'retry'):
            continue
        elif not oakable.isnumeric():
            print("Improper Input, Restarting. . .")
            continue
        score += 300*int(oakable)
        #Oak's Oakable Picture Scores
        for i in range(int(oakable)):
            oak = input("Oak's Score for picture "+str(i+1)+"? ")
            if (oak == 'retry'):
                eee = True
                break
            elif not oak.isnumeric():
                print("Improper Input, Restarting. . .")
                eee = True
                break
                
            score += int(oak)
            oak = "0"
        
    ##    report_poke = int(input("Pokemon in Report: "))
    ##    report_score = int(input("Report Score: "))
    ##    generation[child] += report_score+(300*report_poke)
        if eee:
            continue
        break
    print("Child "+str(child)+" scored "+str(score)+" points")
    return score

def score3(child):
    #Score Level Completeness
    eee = False
    while(True):
        eee = False
        ppp = True
        score = 0
        complete = input("How far did the child progress? (qs/krock/snor/c1/riv/c2/eevee/finish)? ")
        if complete == 'qs':
            score -= 10000
            break
        elif complete == 'krock':
            score -= 1500
        elif (complete == 'retry'):
            continue
        elif complete == 'snor':
            score += 0
        elif complete == 'c1':
            score += 250
        elif complete == 'riv':
            score += 500
        elif complete == 'c2':
            score += 750
        elif complete == 'eevee':
            score += 1000
        elif complete == 'finish':
            score += 1500
            ppp = False
            #Score Remaining Film
            pictures = input("How many pictures were taken? ")
            if (pictures == 'retry'):
                continue
            elif not pictures.isnumeric():
                print("Improper Input, Restarting. . .")
                continue
            pict = int(pictures)
            if pict == 0:
                break
            elif pict < 20:
                score +=  pict*30
            elif pict < 40:
                score +=  pict*40
            elif pict < 60:
                score +=  pict*30
            elif pict == 60:
                score +=  pict*20
        else:
            print("Improper Input, Restarting. . .")
            continue
        if ppp:
            score +=  60*20
        

        oakable = input("How many pictures were sent to Oak? ")
        if (oakable == 'retry'):
            continue
        elif not oakable.isnumeric():
            print("Improper Input, Restarting. . .")
            continue
        score += 300*int(oakable)
        #Oak's Oakable Picture Scores
        for i in range(int(oakable)):
            oak = input("Oak's Score for picture "+str(i+1)+"? ")
            if (oak == 'retry'):
                eee = True
                break
            elif not oak.isnumeric():
                print("Improper Input, Restarting. . .")
                eee = True
                break
                
            score += int(oak)
            oak = "0"
        
    ##    report_poke = int(input("Pokemon in Report: "))
    ##    report_score = int(input("Report Score: "))
    ##    generation[child] += report_score+(300*report_poke)
        if eee:
            continue
        break
    print("Child "+str(child)+" scored "+str(score)+" points")
    return score

def run_child(gen):
    paused = True
    end = False
    zoomed = False
    print("Paused")
    while(True):
        keys = kp.key_check()
        if not end:
            if not paused:
                if not zoomed:
                    kp.TapKey(0x2A)
                    zoomed = True
                action = gen_nn[gen].get_output(snap_grab())
                key_press = kp.KEYS[action[0]]
                print("Do Action "+str(KEYNAMES[action[0]])+" with certainty: "+str(action[1]))
                GG = [float("{0:.2f}".format(x)) for x in action[2]]
                print(GG)
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
            return score3(gen)
        if 'L' in keys:
            end = True
        if 'B' in keys:
            return -1
main()
