from lib.conf import *
from lib.GetCOVID19 import GetCOVID19

covi19_info = GetCOVID19(USER, PASSWORD, HOST, COVID19API)
covi19_info.get_enter_sort()
