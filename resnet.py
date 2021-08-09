import sys
import csv
import os
import numpy as np
import time
from tqdm import tqdm
import json
import pickle
import subprocess
import importlib
import math
import copy
from functools import reduce

import torch
import torch.nn as nn

from base import BasicPruning

class ResNetPruning(BasicPruning):
#{{{
    def __init__(self, params, model):  
    #{{{
        self.fileName = 'resnet{}_{}.py'.format(int(params.depth), int(params.pruner['pruning_perc']))
        self.netName = 'ResNet{}'.format(int(params.depth))
        
        super().__init__(params, model)
    #}}}
#}}}
