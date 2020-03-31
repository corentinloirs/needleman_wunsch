from . import Ruler
import sys
from colorama import Fore, Style
import numpy as np
import pandas as pd
DATASET = sys.argv[1]

csvfile = pd.read_csv(DATASET) #en supposant que DATASET arrive au format CSV

def traitement(df):
    id = (df.columns)[0]
    list = df[id].to_list()
    l = len(list)
    loop = 0
    if l//2 == 1:
        l = l-1
    while loop < l:
        res = Ruler(list[loop],list[loop+1])
        res.compute()
        distance = res.distance
        top, bottom = res.report()
        print(f"====== example # {loop//2+1} - distance = {distance}")
        print(top)
        print(bottom)
        loop = loop + 2

traitement(DATASET)