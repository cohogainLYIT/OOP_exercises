# Author        : Ciaran O hOgain
# Version       : v1.0.0
# Description   : Print machine, node, os and PATH information

import platform
import sys

machine = platform.machine()
node = platform.node()
os = platform.system()
sys_path = sys.path

print("Machine: {},  Node: {}, Operating System: {}, PATH: {}".format(machine, node, os, sys_path[0]))
