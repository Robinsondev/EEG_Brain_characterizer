import dictances as dis
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy.signal as ss
import scipy.stats as st
from mpi4py import MPI
import neuron
from LFPy import NetworkCell, Network, Synapse, RecExtElectrode
import LFPy
import seaborn as sns
from scipy import signal
from scipy.integrate import simps
import seaborn as sns
from scipy import signal
from scipy.integrate import simps
import json
import scipy.fftpack as ff
import seaborn as sns
from scipy.signal import savgol_filter

from dictances import bhattacharyya

# Real human data from data
array1= [ 0.0446, 0.0940, 0.1373, 0.1425, 0.1435, 0.1138, 0.2581, 0.3691, 0.4020, 0.3220, 0.2912, 0.3736, 0.6354, 1.0239, 1.3619, 1.3223, 1.1951, 0.8804, 0.7050, 0.5344, 0.4131, 0.1998, 0.0072,   -0.0411,   -0.1466,   -0.1659,   -0.0788,   -0.0494]
array2 = [ 0.1166, 0.1950, 0.1854, 0.2806, 0.2614, 0.2298, 0.1280, 0.1189, 0.1817, 0.2267, 0.2991, 0.4006, 0.5688, 0.8082, 1.1543, 1.3991, 1.3748, 1.1128, 0.7694, 0.4928, 0.3921, 0.3751, 0.2335, 0.0976, -0.1022, -0.1405, -0.0458, 0.0014]
array3= [   0.1636, 0.1324, 0.0766, 0.0593, 0.0980, 0.0825, 0.2113, 0.2429, 0.2882, 0.2402, 0.2631, 0.1551, 0.1923, 0.3801, 0.4602, 0.5387, 0.7077, 0.8585, 1.0035, 0.9711, 0.8873, 0.7647, 0.5998, 0.3790, 0.2889, 0.3895, 0.4385, 0.3478]
array4= [   0.2136, 0.2815, 0.4158, 0.5617, 0.5535, 0.5281, 0.4820, 0.5313, 0.4453, 0.4169, 0.4070, 0.3072, 0.3377, 0.4130, 0.5167, 0.6239, 0.8869, 1.0389, 1.1357, 1.0909, 0.9312, 0.7392, 0.4916, 0.2838, 0.1444, 0.1022, 0.1771, 0.2582]
array5= [   0.1593, 0.0913, 0.0708, 0.1195, 0.1612, 0.1675, 0.1763, 0.2506, 0.3312, 0.3998, 0.4222, 0.4303, 0.4373, 0.4428, 0.4530, 0.4906, 0.6844, 0.9004, 1.0529, 1.1012, 0.8239, 0.7107, 0.6327, 0.5654, 0.4546, 0.2831, 0.2569, 0.2339]
array6= [   0.1216, 0.1899, 0.2195, 0.2390, 0.1554, 0.3662, 0.6139, 0.7493, 0.7555, 0.6721, 0.5686, 0.5531, 0.6668, 1.1508, 1.8735, 2.2836, 2.3646, 2.3263, 2.0934, 1.7842, 1.3856, 1.1178, 0.8790, 0.7642, 0.6310, 0.4610, 0.3686, 0.3932]
array7= [   0.2286, 0.3276, 0.4465, 0.4331, 0.4389, 0.4495, 0.3817, 0.3174, 0.3171, 0.5401, 0.6484, 0.6980, 0.8248, 1.1930, 1.6147, 1.9108, 2.0708, 2.0977, 1.8560, 1.5455, 1.1646, 0.9368, 0.7401, 0.6267, 0.4735, 0.3160, 0.1753, 0.1329]
array8= [  -0.2308, 0.0430, 0.2834, 0.4520, 0.3568, 0.2795, 0.2723, 0.2804, 0.3193, 0.3544, 0.4240, 0.6077, 0.8210, 1.2388, 1.6095, 1.5710, 1.2235, 0.8082, 0.5470, 0.3588, 0.3490, 0.2642, 0.1805, 0.1225, 0.1791, 0.2722, 0.3380, 0.3066]
array9= [ -0.4602 ,  -0.3868 ,  -0.2702,   -0.1659, 0.0480, 0.1563, 0.1931, 0.2311, 0.2474, 0.2291, 0.2593, 0.3803, 0.4615, 0.7922, 1.3891, 1.6691, 1.8085, 1.8185, 1.7116, 1.5464, 1.2176, 0.8588, 0.5957, 0.3872, 0.3559, 0.2859, 0.1408, 0.0467]
#array10= [   0.0454, 0.2185, 0.4159, 0.6189, 0.6510, 0.5535, 0.5157, 0.4641, 0.5851, 1.0148, 1.4519, 1.7610, 1.7508, 1.3867, 1.0994, 0.9909, 0.7126, 0.3879, 0.1251, 0.1048, 0.1199, 0.1342, 0.0601, 0.0695, 0.1332, 0.0895 ,  -0.0758 ,  -0.1210]
array11= [   0.5487, 0.6268, 0.6235, 0.6129, 0.5130, 0.3668, 0.3849, 0.4658, 0.6349, 0.7913, 1.0486, 1.3530, 1.5190, 1.5810, 1.3329, 1.1494, 0.8839, 0.4512, 0.2262, 0.1190, 0.0329, 0.0854, 0.0456 ,  -0.0428, 0.0788, 0.2731, 0.2996, 0.1151]
array12= [0.1484, 0.1380, 0.0643, 0.0723, 0.1216, 0.1241, 0.1941, 0.2234, 0.3391, 0.3811, 0.4529, 0.5713, 0.6766, 1.0933, 2.0370, 2.7136, 2.9383, 2.7448, 2.1575, 1.5227, 1.1207, 0.8901, 0.6101, 0.4647, 0.3753, 0.2929, 0.3613, 0.3938]

#x-axis for the real human data

x_axis_processed = [32.0030,   34.1365,   36.2701,   38.4036,   40.5371,   42.6707,   44.8042,   46.9378,   49.0713,   51.2048,   53.3384,   55.4719,   57.6054,   59.7390,   61.8725,   64.0060,   66.1396,   68.2731,   70.4066,   72.5402,   74.6737,   76.8072,   78.9408,   81.0743,   83.2078,   85.3414,   87.4749,   89.6084]

# the array that we want to compare witht he networkSimulationArguments
array10= [   0.0454, 0.2185, 0.4159, 0.6189, 0.6510, 0.5535, 0.5157, 0.4641, 0.5851, 1.0148, 1.4519, 1.7610, 1.7508, 1.3867, 1.0994, 0.9909, 0.7126, 0.3879, 0.1251, 0.1048, 0.1199, 0.1342, 0.0601, 0.0695, 0.1332, 0.0895 ,  -0.0758 ,  -0.1210]


#Normalizing the real human data before comparison

#sim_405_03_02_02 = [0.04475568, 0.15663551, 0.09380935, 0.20494816, 0.01654902, 0.4181603, 0.22081506, 0.3779075,  0.95584888, 1. , 0.73930221, 0.36539561, 0.55754875, 0.21792918, 0.28428877, 0.1032936,  0.26318357, 0.1168861, 0.2540913,  0.43207699, 0.25550859, 0.10100809, 0.13203308, 0.12674578, 0.07251096, 0.04947468, 0.10082682, 0.0183058 ]
sim_408_07_07_07 = [0.06088566, 0.08855665, 0.16802996, 0.06458868, 0.21600541, 0.26218055, 0.5035246,  0.30323319, 0.32158617, 0.35260187, 1. ,  0.8311905, 0.22376011, 0.45916791, 0.26148447, 0.12643471, 0.16777741, 0.0789757, 0.06843635, 0.04328013, 0.08741993, 0.07139075, 0.03543661, 0.04848461, 0.08927507, 0.04304059, 0.0316131,  0.06696181]
sim_405_03_02_03 = [0.09327422, 0.00128564, 0.05703022, 0.00308001, 0.16894213, 0.22799808, 0.14732479, 0.0708311,  0.24618505, 0.14395115, 0.30829829, 0.38669485, 0.48833761, 0.51314913, 1. ,        0.85959831, 0.65476398, 0.38419473, 0.12696597, 0.12699201, 0.18714718, 0.16879248, 0.07327476, 0.07188532, 0.01474168, 0.07895097, 0.07501708, 0.07418635]
sim_402_07_02_07 = [0.07091595, 0.05729714, 0.07950814, 0.06205042, 0.03748132, 0.03181748, 0.12078556, 0.11457622, 0.08508095, 0.24498871, 0.14334235, 0.15197863, 0.3906375,  0.11266467, 0.80819902, 1. , 0.43866317, 0.39514136, 0.30765683, 0.29394605, 0.04576725, 0.08821936, 0.124423,   0.24609837, 0.14514166, 0.09069992, 0.12158804, 0.04047152]
sim_403_07_07_07 = [ 0.07928989,  0.1671782,   0.10262232,  0.04586247,  0.14225843,  0.20725557, 0.24885392,  0.24328209,  0.27092176,  0.34595862,  0.76994872,  1., 0.52878247,  0.44445121,  0.19806458 , 0.62530732 , 0.01970831,  0.16182968, 0.02067354,  0.16499298 ,-0.00315233 , 0.09173092, 0.04143652 , 0.15984127 , 0.04543381,  0.06360749,  0.05936053,  0.05753955]
sim_409_07_03_03 = [ 0.02196754,  0.05219792,  0.03229701,  0.04216996,  0.02705415,  0.07033195, 0.05078725,  0.18977413,  0.08501861,  0.29748259,  0.24550531,  0.24734658, 1.,          0.52746267,  0.15468576,  0.3588017,   0.25065708,  0.11585509, -0.00832731,  0.09302816,  0.07714416,  0.0358728,   0.06876557,  0.04301948, 0.02653134,  0.01363168,  0.01699846,  0.01045564]
def normalization(array):
    max_of_array = np.max(array)
    normlized_array = array/max_of_array
    return normlized_array


#normalizing the array for processing before comparison
normz = []
for x in arr1:
    z = (x - min(arr1))/(max(arr1) - min(arr1))
    normz.append(z)

# softmax to normalize to a probability distribution
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()



#print(sum(check_normz)) # to check

# turn numpy array into a python array

py_normz = check_normz.tolist()

string_index =[]

value = 0
for i in py_normz:
    value = value + 1
    str_in = "value" + str(value)
    string_index.append(str_in)


dict_a = dict(zip(string_index, py_normz))
