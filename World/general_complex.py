import yaml
import os,sys
import pprint as _pp
import numpy as np


from .Object import *





nan=float('nan')
_p=_pp.PrettyPrinter(indent=2)
def pprint(o):
    _p.pprint(o)
def dirname(f):
    return os.path.dirname(f)
def all_objects_type():
    r=os.listdir(cur_dir+"/Object/")
    r=filter(lambda p:p.endswith('.py'),r)
    r=[p[:-3] for p in r]
    return r

cur_dir=dirname(__file__)