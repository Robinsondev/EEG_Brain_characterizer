1. Place sim.ipynb file where all your folders exist.

2. Open jupyter and then open the file "sim.ipynb" using jupyter.


--read_input_arrays()
This function reads all the arrayX from the file "input_arrays.txt". Place as many arrays as you want in the file "input_arrays.txt" with the format 
[0.1484, 0.1380, 0.0643, 0.0723, 0.1216, 0.1241, 0.1941, 0.2234, 0.3391, 0.3811, 0.4529, 0.5713, 0.6766, 1.0933, 2.0370, 2.7136, 2.9383, 2.7448, 2.1575, 1.5227, 1.1207, 0.8901, 0.6101, 0.4647, 0.3753, 0.2929, 0.3613, 0.3938]
It returns dictionary of array_names and their values.

--find_all_simulations()
This function finds all the simulations in the folders named like "example_network3_output_oli___E-I_4_0.2__ prob E-E0.3_ _prob i i 0.2 _prob i e 0.7 network_300 freq120Hz"
if you wants to add more folder please follow the same naming convention.
It returns dictionary of all the simulations with their names like sim_402_03_02_07.

--comparex(arrays_dict,sims_dict,prec)
This function compare all the arrays in the arrays_dict with all the simulations under the given precision and returns dictionary of array names with their matched simulations.

--create_table(mappings,prec)
This function creates a table from the dictionary created by the function comparex.

--create_viz(mappings,arrays_dict,sims_dict,freq)
This funciton create graphs of arrayX and their matched simualations row by row.