import matplotlib.pyplot as plt
import os
import time
import numpy as np
from lifegame import lifegame


def output(game_map):
    for line in game_map:
        out_line=""
        for point in line:
            if point==1:
                out_line+="M"
            else :
                out_line+=" "
            out_line+=" "
        print(out_line)
    return "done"
    
    
if __name__ =="__main__":
    SIZE = 50,150
    updateInterval = 50

    ground=np.random.random(SIZE)>=0.6
    lg=lifegame(ground.astype(np.int))
    lg[5]
    for i,im in enumerate(lg):
        # plt.clf()
        # plt.imshow(im)
        # plt.pause(0.5)
        # plt.ioff
        os.system("clear")
        output(im)
        time.sleep(0.1)
