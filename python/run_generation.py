import keypress as kp
import time

generation = [0,0,0,0,0,0,0,0,0,0]
gen = 0

def main():
    score(1)
    return

def score(child):
    #Score Level Completeness
    complete = input("Did the Child complete the Level (y/n)? ")
    if complete == 'y':
        generation[child] += 1500
    #Score Remaining Film
    pictures = input("How many pictures were taken? ")
    generation[child] +=  int(pictures)*20
    '''
    #Score Usable Pictures
    usable = input("How many pictures were usable? ")
    generation[child] += 15*int(usable)
    #Score Oakable Pictures
    oakable = input("How many pictures were sent to Oak? ")
    generation[child] += 100*int(oakable)
    #Oak's Oakable Picture Scores
    for i in range(int(oakable)):
        oak = input("Oak's Score for picture "+str(i+1)+"? ")
        generation[child] += int(oak)
        oak = "0"
    '''
    report_poke = int(input("Pokemon in Report: "))
    report_score = int(input("Report Score: "))
    generation[child] += report_score+(300*report_poke)
    print("Child "+str(child)+" in generation "+str(gen)+" scored "+str(generation[child])+" points")
