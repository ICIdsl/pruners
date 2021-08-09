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

from base import BasicPruning

import torch
import torch.nn as nn

class MobileNetV2Pruning(BasicPruning):
#{{{
    def __init__(self, params, model):
    #{{{
        self.fileName = 'mobilenetv2_{}.py'.format(int(params.pruner['pruning_perc']))
        self.netName = 'MobileNetV2'
        
        super().__init__(params, model)
    #}}}
#}}}
