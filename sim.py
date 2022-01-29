
# coding: utf-8

# In[16]:


import glob
import re
import numpy as np
from dictances import bhattacharyya
import sys


# In[17]:


# folder_path=r"C:\Users\salma\Downloads\latest simulations copy\latest simulations copy"
# folder_path=sys.argv[1]
# print(folder_path)

all_files=glob.glob("example?*/norm_downsampled_spectrum?*.txt")
file_dict={}
for file_name in all_files:
    try:
        f = open(file_name, "r")
        file_content=f.read()
    except Exception as e:
        print(e)
        print("Error in reading file: "+str(file_name))
        continue
    try:
        file_array=file_content[1:-1].split(' ')
        file_array=[item for item in file_array if item!='']
        file_array=[float(item.replace('\n','')) for item in file_array]
    except Exception as e:
        print(e)
        print("Error in parsing array of folder: "+str(file_name))
        continue
    try:
        temp_string=file_name.split('/')[-2]
        temp_string=re.findall('[0-9]',temp_string[0:temp_string.rfind('network')])[1:]
        file_dict["sim_"+'_'.join(temp_string)]=file_array
    except Exception as e:
        print(e)
        print("Error in parsing naming convention of folder: "+str(file_name))
        continue

# for k,v in file_dict.items():
#     print(k)
#     print(v)
#     print()


# In[18]:


def normalization(array):
    max_of_array = np.max(array)
    normlized_array = array/max_of_array
    return normlized_array


#normalizing the array for processing before comparison
def return_normz(arr1):
    normz = []
    for x in arr1:
        z = (x - min(arr1))/(max(arr1) - min(arr1))
        normz.append(z)
    return normz

# softmax to normalize to a probability distribution
def softmax(x):
    e_x = np.exp(x - np.max(x))
    vals = e_x / e_x.sum()
    return vals

# introduce the array in the function
def making_dictionnaries(py_normz):
    value = 0
    string_index =[]
    for i in py_normz:
        value = value + 1
        str_in = "value" + str(value)
        string_index.append(str_in)
    return string_index


def comparex(patient_array, sims,prec):
    patient_data = softmax(return_normz(normalization(patient_array).tolist())).tolist()
    norm_indices = making_dictionnaries(softmax(return_normz(normalization(patient_array).tolist())).tolist())
    dict_patient = dict(zip(norm_indices, patient_data))
    array_sims_local = []
    sims_matched_arrays={}
    for k,v in sims.items():
        normalized_sim = softmax(return_normz(normalization(v).tolist())).tolist()
        norm_indices = making_dictionnaries(softmax(return_normz(normalization(v).tolist())).tolist())
        dict_sim = dict(zip(norm_indices, normalized_sim ))
        array_sims_local.append(dict_sim.copy())
        comp_val = bhattacharyya(dict_patient, dict_sim)
        if(comp_val<=prec):
            sims_matched_arrays[k]=v
    # smallest = min(array_bhatta_result)
    # small_index = array_bhatta_result.index(smallest)
    # simulation = sims[small_index]
    return sims_matched_arrays


# In[19]:


array1= [ 0.0446, 0.0940, 0.1373, 0.1425, 0.1435, 0.1138, 0.2581, 0.3691, 0.4020, 0.3220, 0.2912, 0.3736, 0.6354, 1.0239, 1.3619, 1.3223, 1.1951, 0.8804, 0.7050, 0.5344, 0.4131, 0.1998, 0.0072,   -0.0411,   -0.1466,   -0.1659,   -0.0788,   -0.0494]


print("Best Fits:")
best_fit_arrays=comparex(array1,file_dict,0.005)
for k,v in best_fit_arrays.items():
    print(k)
    print(v)
