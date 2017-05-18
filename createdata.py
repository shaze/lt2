#!/usr/bin/env python3

import random
import sys

tags = ["light","medium","heavy"]
readings = list(range(1000,2000,71))

g=open(sys.argv[2],"w")
for i in range(int(sys.argv[1])):
    res = "{}\t{}\n".format(random.choice(tags),random.choice(readings))
    g.write(res)
g.close()

    
