Last login: Sat Mar 20 22:41:24 on ttys001
(base) Azalis-MacBook-Pro:good data theman$ ssh -Y mabt5140@beluga.computecanada.ca
mabt5140@beluga.computecanada.ca's password:
Last login: Wed Mar 10 19:27:14 2021 from lnsm2-montreal02-142-119-42-239.internet.virginmobile.ca
###############################################################################
  _       __ _
 | |__   /_/| |_   _  __ _  __ _   Bienvenue sur Béluga / Welcome to Béluga
 | '_ \ / _ \ | | | |/ _` |/ _` |
 | |_) |  __/ | |_| | (_| | (_| |  Aide/Support:    support@calculcanada.ca
 |_.__/ \___|_|\__,_|\__, |\__,_|  Globus endpoint: computecanada#beluga-dtn
                     |___/         Documentation:   docs.calculcanada.ca

2021-02-03    Mode turbo des CPU - CPU Turbo Mode

(FR) Le mode "turbo" est maintenant activé sur l'ensemble des nœuds de calcul
     de Béluga.

(EN) Turbo mode has now been activated on all of Béluga's compute nodes.
###############################################################################
Lmod Warning:  Warning, in April 2021, the default standard
environment module will be changed to a more recent one.
To test your jobs with the new environment, please run:
module load StdEnv/2020

To change your default version immediately, please run the following command:

echo "module-version StdEnv/2020 default" >> $HOME/.modulerc

For more information, please see:
https://docs.computecanada.ca/wiki/Standard_software_environments
While processing the following module(s):
    Module fullname  Module Filename
    ---------------  ---------------
    StdEnv/2018.3    /cvmfs/soft.computecanada.ca/custom/modules/StdEnv/2018.3.lua

[mabt5140@beluga4 ~]$ ls
nearline  projects  scratch
[mabt5140@beluga4 ~]$ cd scratcj
-bash: cd: scratcj: No such file or directory
[mabt5140@beluga4 ~]$ cd scratch
[mabt5140@beluga4 scratch]$ ls
BallAndStick.hoc          core.26654  environ             file1_205_dataop
BallAndStickTemplate.hoc  core.3813   environnement       lfpystart.sh
core.16178                env         example2_3d_100.py  req.txt
[mabt5140@beluga4 scratch]$ cd environnement
[mabt5140@beluga4 environnement]$ ls
BallAndStick.hoc              example2_3d_20000_E_I_706.py
BallAndStickTemplate.hoc      example2_3d_20000_E_I_707.py
bin                           example2_3d_20000_E_I_708.py
cho.py                        example2_3d_20000_E_I_709.py
core.17503                    example_net.py
core.179076                   example_net_ui.py
core.179080                   example_network_output
core.179395                   file1_205_dataop
core.23564                    formaty.py
core.28379                    lfpystart_20000_E_I_404.sh
core.28380                    lfpystart_20000_E_I_405.sh
core.28381                    lfpystart_20000_E_I_406.sh
core.28382                    lfpystart_20000_E_I_407.sh
core.28383                    lfpystart_20000_E_I_408.sh
core.30264                    lfpystart_20000_E_I_409.sh
core.31476                    lfpystart_20000_E_I_504.sh
core.31737                    lfpystart_20000_E_I_505.sh
core.7674                     lfpystart_20000_E_I_506.sh
core.9846                     lfpystart_20000_E_I_507.sh
env                           lfpystart_20000_E_I_508.sh
environ                       lfpystart_20000_E_I_509.sh
example2_3d_100_1000_406.py   lfpystart_20000_E_I_604.sh
example2_3d_20000_E_I_304.py  lfpystart_20000_E_I_605.sh
example2_3d_20000_E_I_305.py  lfpystart_20000_E_I_606.sh
example2_3d_20000_E_I_306.py  lfpystart_20000_E_I_607.sh
example2_3d_20000_E_I_307.py  lfpystart_20000_E_I_608.sh
example2_3d_20000_E_I_308.py  lfpystart_20000_E_I_609.sh
example2_3d_20000_E_I_309.py  lfpystart_20000_E_I_705.sh
example2_3d_20000_E_I_404.py  lfpystart_20000_E_I_706.sh
example2_3d_20000_E_I_405.py  lfpystart_20000_E_I_707.sh
example2_3d_20000_E_I_406.py  lfpystart_20000_E_I_708.sh
example2_3d_20000_E_I_407.py  lfpystart_20000_E_I_709.sh
example2_3d_20000_E_I_408.py  lib
example2_3d_20000_E_I_409.py  nlmeans_1000_404.out
example2_3d_20000_E_I_504.py  nlmeans_1000_406_1234.out
example2_3d_20000_E_I_505.py  nlmeans_1000_406k.out
example2_3d_20000_E_I_506.py  nlmeans_1000_407_1234.out
example2_3d_20000_E_I_507.py  nlmeans_1000_407k.out
example2_3d_20000_E_I_508.py  nlmeans_1000_407.out
example2_3d_20000_E_I_509.py  nlmeans_1000_408_1234.out
example2_3d_20000_E_I_604.py  nlmeans_1000_409_1234.out
example2_3d_20000_E_I_605.py  nlmeans_1000.out
example2_3d_20000_E_I_606.py  pyvenv.cfg
example2_3d_20000_E_I_607.py  req.txt
example2_3d_20000_E_I_608.py  requirements.txt
example2_3d_20000_E_I_609.py  test_arr.py
example2_3d_20000_E_I_704.py  ttye
example2_3d_20000_E_I_705.py
[mabt5140@beluga4 environnement]$ pip list
pip (8.1.2)
setuptools (26.1.1)
[mabt5140@beluga4 environnement]$ source env/bin/activate
(env) [mabt5140@beluga4 environnement]$ ls
BallAndStick.hoc              example2_3d_20000_E_I_706.py
BallAndStickTemplate.hoc      example2_3d_20000_E_I_707.py
bin                           example2_3d_20000_E_I_708.py
cho.py                        example2_3d_20000_E_I_709.py
core.17503                    example_net.py
core.179076                   example_net_ui.py
core.179080                   example_network_output
core.179395                   file1_205_dataop
core.23564                    formaty.py
core.28379                    lfpystart_20000_E_I_404.sh
core.28380                    lfpystart_20000_E_I_405.sh
core.28381                    lfpystart_20000_E_I_406.sh
core.28382                    lfpystart_20000_E_I_407.sh
core.28383                    lfpystart_20000_E_I_408.sh
core.30264                    lfpystart_20000_E_I_409.sh
core.31476                    lfpystart_20000_E_I_504.sh
core.31737                    lfpystart_20000_E_I_505.sh
core.7674                     lfpystart_20000_E_I_506.sh
core.9846                     lfpystart_20000_E_I_507.sh
env                           lfpystart_20000_E_I_508.sh
environ                       lfpystart_20000_E_I_509.sh
example2_3d_100_1000_406.py   lfpystart_20000_E_I_604.sh
example2_3d_20000_E_I_304.py  lfpystart_20000_E_I_605.sh
example2_3d_20000_E_I_305.py  lfpystart_20000_E_I_606.sh
example2_3d_20000_E_I_306.py  lfpystart_20000_E_I_607.sh
example2_3d_20000_E_I_307.py  lfpystart_20000_E_I_608.sh
example2_3d_20000_E_I_308.py  lfpystart_20000_E_I_609.sh
example2_3d_20000_E_I_309.py  lfpystart_20000_E_I_705.sh
example2_3d_20000_E_I_404.py  lfpystart_20000_E_I_706.sh
example2_3d_20000_E_I_405.py  lfpystart_20000_E_I_707.sh
example2_3d_20000_E_I_406.py  lfpystart_20000_E_I_708.sh
example2_3d_20000_E_I_407.py  lfpystart_20000_E_I_709.sh
example2_3d_20000_E_I_408.py  lib
example2_3d_20000_E_I_409.py  nlmeans_1000_404.out
example2_3d_20000_E_I_504.py  nlmeans_1000_406_1234.out
example2_3d_20000_E_I_505.py  nlmeans_1000_406k.out
example2_3d_20000_E_I_506.py  nlmeans_1000_407_1234.out
example2_3d_20000_E_I_507.py  nlmeans_1000_407k.out
example2_3d_20000_E_I_508.py  nlmeans_1000_407.out
example2_3d_20000_E_I_509.py  nlmeans_1000_408_1234.out
example2_3d_20000_E_I_604.py  nlmeans_1000_409_1234.out
example2_3d_20000_E_I_605.py  nlmeans_1000.out
example2_3d_20000_E_I_606.py  pyvenv.cfg
example2_3d_20000_E_I_607.py  req.txt
example2_3d_20000_E_I_608.py  requirements.txt
example2_3d_20000_E_I_609.py  test_arr.py
example2_3d_20000_E_I_704.py  ttye
example2_3d_20000_E_I_705.py
(env) [mabt5140@beluga4 environnement]$ pip lists
ERROR: unknown command "lists" - maybe you meant "list"
(env) [mabt5140@beluga4 environnement]$ pip list
Package            Version
------------------ -----------
absl-py            0.11.0
cachetools         4.1.1
certifi            2020.11.8
cloudpickle        1.6.0
cycler             0.10.0
dask               2.30.0
future             0.18.2
grpcio             1.32.0
h5py               2.10.0
importlib-metadata 3.1.1
kiwisolver         1.2.0
LFPy               2.1.2
LFPykit            0.3
Markdown           3.3.3
matplotlib         3.3.2
MEAutility         1.4.8
networkx           2.5
numpy              1.19.2
oauthlib           3.1.0
Pillow             7.2.0
Pillow-SIMD        7.0.0.post3
pip                20.0.2
protobuf           3.14.0
pyasn1             0.4.8
pyasn1-modules     0.2.8
pyparsing          2.4.7
python-dateutil    2.8.1
PyWavelets         1.1.1
PyYAML             5.3.1
requests           2.25.0
requests-oauthlib  1.3.0
rsa                4.6
scikit-image       0.14.2
scipy              1.4.1
setuptools         46.1.3
six                1.15.0
toolz              0.11.1
torch              1.7.0
torchvision        0.8.1
tqdm               4.53.0
typing-extensions  3.7.4.3
urllib3            1.26.2
Werkzeug           1.0.1
wheel              0.34.2
zipp               3.4.0
(env) [mabt5140@beluga4 environnement]$ deactivate
[mabt5140@beluga4 environnement]$ ls
BallAndStick.hoc              example2_3d_20000_E_I_709.py
BallAndStickTemplate.hoc      example_net.py
bin                           example_net_ui.py
cho.py                        example_network_output
core.17503                    file1_205_dataop
core.179076                   formaty.py
core.179080                   lfpystart_20000_E_I_304.sh
core.179395                   lfpystart_20000_E_I_305.sh
core.23564                    lfpystart_20000_E_I_306.sh
core.28379                    lfpystart_20000_E_I_307.sh
core.28380                    lfpystart_20000_E_I_308.sh
core.28381                    lfpystart_20000_E_I_309.sh
core.28382                    lfpystart_20000_E_I_404.sh
core.28383                    lfpystart_20000_E_I_405.sh
core.30264                    lfpystart_20000_E_I_406.sh
core.31476                    lfpystart_20000_E_I_407.sh
core.31737                    lfpystart_20000_E_I_408.sh
core.7674                     lfpystart_20000_E_I_409.sh
core.9846                     lfpystart_20000_E_I_504.sh
env                           lfpystart_20000_E_I_505.sh
environ                       lfpystart_20000_E_I_506.sh
example2_3d_100_1000_406.py   lfpystart_20000_E_I_507.sh
example2_3d_20000_E_I_304.py  lfpystart_20000_E_I_508.sh
example2_3d_20000_E_I_305.py  lfpystart_20000_E_I_509.sh
example2_3d_20000_E_I_306.py  lfpystart_20000_E_I_604.sh
example2_3d_20000_E_I_307.py  lfpystart_20000_E_I_605.sh
example2_3d_20000_E_I_308.py  lfpystart_20000_E_I_606.sh
example2_3d_20000_E_I_309.py  lfpystart_20000_E_I_607.sh
example2_3d_20000_E_I_404.py  lfpystart_20000_E_I_608.sh
example2_3d_20000_E_I_405.py  lfpystart_20000_E_I_609.sh
example2_3d_20000_E_I_406.py  lfpystart_20000_E_I_705.sh
example2_3d_20000_E_I_407.py  lfpystart_20000_E_I_706.sh
example2_3d_20000_E_I_408.py  lfpystart_20000_E_I_707.sh
example2_3d_20000_E_I_409.py  lfpystart_20000_E_I_708.sh
example2_3d_20000_E_I_504.py  lfpystart_20000_E_I_709.sh
example2_3d_20000_E_I_505.py  lib
example2_3d_20000_E_I_506.py  nlmeans_1000_404.out
example2_3d_20000_E_I_507.py  nlmeans_1000_406_1234.out
example2_3d_20000_E_I_508.py  nlmeans_1000_406k.out
example2_3d_20000_E_I_509.py  nlmeans_1000_407_1234.out
example2_3d_20000_E_I_604.py  nlmeans_1000_407k.out
example2_3d_20000_E_I_605.py  nlmeans_1000_407.out
example2_3d_20000_E_I_606.py  nlmeans_1000_408_1234.out
example2_3d_20000_E_I_607.py  nlmeans_1000_409_1234.out
example2_3d_20000_E_I_608.py  nlmeans_1000.out
example2_3d_20000_E_I_609.py  pyvenv.cfg
example2_3d_20000_E_I_704.py  req.txt
example2_3d_20000_E_I_705.py  requirements.txt
example2_3d_20000_E_I_706.py  test_arr.py
example2_3d_20000_E_I_707.py  ttye
example2_3d_20000_E_I_708.py
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_304.sh
Submitted batch job 17232903
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_305.sh lfpystart_20000_E_I_306.sh lfpystart_20000_E_I_307.sh lfpystart_20000_E_I_308.sh lfpystart_20000_E_I_309.sh
Submitted batch job 17232906
[mabt5140@beluga4 environnement]$ scancel 17232906
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_305.sh
Submitted batch job 17232909
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_306.sh
Submitted batch job 17232910
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_307.sh
Submitted batch job 17232911
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_308.sh
Submitted batch job 17232912
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_309.sh
Submitted batch job 17232913
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_409.sh
Submitted batch job 17232914
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_408.sh
Submitted batch job 17232915
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_407.sh
Submitted batch job 17232916
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_406.sh
Submitted batch job 17232917
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_405.sh
Submitted batch job 17232918
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_404.sh
Submitted batch job 17232919
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_504.sh
Submitted batch job 17232920
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_505.sh
Submitted batch job 17232921
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_506.sh
Submitted batch job 17232922
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_507.sh
Submitted batch job 17232923
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_508.sh
Submitted batch job 17232924
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_509.sh
Submitted batch job 17232926
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_609.sh
Submitted batch job 17232927
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_608.sh
Submitted batch job 17232928
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_607.sh
Submitted batch job 17232939
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_606.sh
Submitted batch job 17232940
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_605.sh
Submitted batch job 17232941
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_604.sh
Submitted batch job 17232942
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_704.sh
sbatch: error: Unable to open file lfpystart_20000_E_I_704.sh
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_704.sh
Submitted batch job 17232954
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_705.sh
Submitted batch job 17232955
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_706.sh
Submitted batch job 17232956
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_707.sh
Submitted batch job 17232957
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_708.sh
Submitted batch job 17232958
[mabt5140@beluga4 environnement]$ sbatch lfpystart_20000_E_I_709.sh
Submitted batch job 17232959
[mabt5140@beluga4 environnement]$ sq
          JOBID     USER      ACCOUNT           NAME  ST  TIME_LEFT NODES CPUS TRES_PER_N MIN_MEM NODELIST (REASON)
       17232903 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232909 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232910 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232911 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232912 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232913 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232914 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232915 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232916 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232917 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232918 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232919 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232920 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232921 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232922 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232923 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232924 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232926 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232927 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232928 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232939 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232940 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232941 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232942 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232954 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232955 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232956 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232957 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232958 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
       17232959 mabt5140 def-kwhittin lfpystart_2000  PD   20:00:00     1   30        N/A    250G  (Priority)
[mabt5140@beluga4 environnement]$ packet_write_wait: Connection to 132.219.136.4 port 22: Broken pipe
(base) Azalis-MacBook-Pro:good data theman$ ls
BallAndStick.hoc
BallAndStickTemplate.hoc
Figure_100_406.png
Figure_5_1000_407.png
Figure_5_100_407.png
Figure_5_200_508.png
Figure_5_400_407.png
Figure_5_408_1000.png
example2_3d_100_1000_406.py
example2_3d_100_1000_406lk.py
example2_3d_100_1000_408.py
example_network3_output_oli_3_0.4
example_network3_output_oli_4_0.4
example_network3_output_oli_4_0.6
example_network3_output_oli_4_0.7
example_network3_output_oli_4_0.8
example_network3_output_oli_5_0.8
example_network3_output_oli_6_0.8
example_network3_output_oli_E-I4_0.8
example_network3_output_oli_E-I_4_0.6
example_network3_output_oli_E-I_4_0.6 | I-E_0.5
example_network3_output_oli_E-I_4_0.6 | I-E_0.5 jkj
example_network3_output_oli_E-I_4_0.6 | I-E_0.5 po
example_network3_output_oli_E-I_4_0.6 | I-E_0.8
example_network3_output_oli_E-I_4_0.7 | I-E_0.6
example_network3_output_oli_E-I_4_0.8
file1_205_dataop
final for server
op
power.png
(base) Azalis-MacBook-Pro:good data theman$ python
Python 3.7.3 (default, Mar 27 2019, 16:54:48)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import dictances as dis
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'dictances'
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
(base) Azalis-MacBook-Pro:good data theman$ pip install dictances
Collecting dictances
  Using cached https://files.pythonhosted.org/packages/bc/22/853350c297c53072229c2f94560464ec898fe5fc1fc708423ecbc9107bc7/dictances-1.5.3.tar.gz
Building wheels for collected packages: dictances
  Building wheel for dictances (setup.py) ... done
  Stored in directory: /Users/theman/Library/Caches/pip/wheels/5a/df/45/cd4d5f9742a74b162fe7724889c128ff3fb058715306fb0103
Successfully built dictances
Installing collected packages: dictances
Successfully installed dictances-1.5.3
(base) Azalis-MacBook-Pro:good data theman$ python
Python 3.7.3 (default, Mar 27 2019, 16:54:48)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import dictances as dis
>>> arr1 = [ 8.52895974e-05  1.09556515e-04  6.20116143e-05  2.16130774e-04
  File "<stdin>", line 1
    arr1 = [ 8.52895974e-05  1.09556515e-04  6.20116143e-05  2.16130774e-04
                                          ^
SyntaxError: invalid syntax
>>>   2.42203409e-04  1.25433867e-04  1.35148266e-04  4.79886304e-04
  File "<stdin>", line 1
    2.42203409e-04  1.25433867e-04  1.35148266e-04  4.79886304e-04
    ^
IndentationError: unexpected indent
>>>   3.81419729e-04  4.34204380e-04  4.76280184e-04  2.63636228e-04
  File "<stdin>", line 1
    3.81419729e-04  4.34204380e-04  4.76280184e-04  2.63636228e-04
    ^
IndentationError: unexpected indent
>>>   3.23658548e-04  5.59189667e-04  2.58565640e-04  6.66805963e-04
  File "<stdin>", line 1
    3.23658548e-04  5.59189667e-04  2.58565640e-04  6.66805963e-04
    ^
IndentationError: unexpected indent
>>>   8.57291639e-04  3.59571430e-04  4.44450946e-04  6.26958341e-04
  File "<stdin>", line 1
    8.57291639e-04  3.59571430e-04  4.44450946e-04  6.26958341e-04
    ^
IndentationError: unexpected indent
>>>   5.91712773e-05  5.36732485e-04  7.17162415e-05  3.81858618e-04
  File "<stdin>", line 1
    5.91712773e-05  5.36732485e-04  7.17162415e-05  3.81858618e-04
    ^
IndentationError: unexpected indent
>>>   5.53946775e-05  1.80365134e-04 -2.21442828e-05  2.11608731e-04]
  File "<stdin>", line 1
    5.53946775e-05  1.80365134e-04 -2.21442828e-05  2.11608731e-04]
    ^
IndentationError: unexpected indent
>>> arr = [ 8.52895974e-05, 1.09556515e-04,  6.20116143e-05,  2.16130774e-04,
...   2.42203409e-04,  1.25433867e-04,  1.35148266e-04,  4.79886304e-04,
...   3.81419729e-04,  4.34204380e-04,  4.76280184e-04,  2.63636228e-04,
...   3.23658548e-04,  5.59189667e-04 , 2.58565640e-04 , 6.66805963e-04,
...   8.57291639e-04,  3.59571430e-04,  4.44450946e-04,  6.26958341e-04,
...   5.91712773e-05,  5.36732485e-04,  7.17162415e-05,  3.81858618e-04,
...   5.53946775e-05,  1.80365134e-04, -2.21442828e-05 , 2.11608731e-04]
>>> arr
[8.52895974e-05, 0.000109556515, 6.20116143e-05, 0.000216130774, 0.000242203409, 0.000125433867, 0.000135148266, 0.000479886304, 0.000381419729, 0.00043420438, 0.000476280184, 0.000263636228, 0.000323658548, 0.000559189667, 0.00025856564, 0.000666805963, 0.000857291639, 0.00035957143, 0.000444450946, 0.000626958341, 5.91712773e-05, 0.000536732485, 7.17162415e-05, 0.000381858618, 5.53946775e-05, 0.000180365134, -2.21442828e-05, 0.000211608731]
>>> norm = [float(i)/max(arr) for i in arr]
>>> norm
[0.09948726141723166, 0.12779375187630868, 0.072334327641798, 0.2521088089137424, 0.2825216040629086, 0.14631411446671067, 0.15764561305840522, 0.5597701904100805, 0.4449124564482076, 0.5064838617888352, 0.555563780553796, 0.3075222199851642, 0.3775361070563293, 0.6522747237477724, 0.3016075606448321, 0.7778052796336673, 1.0, 0.4194271979829725, 0.518436114130818, 0.7313244553875791, 0.06902117623475387, 0.6260792250652055, 0.08365442777868967, 0.4454244047514851, 0.06461590779610998, 0.2103894705078303, -0.02583051296969432, 0.24683400767425423]
>>> assert sum(norm.values()) ==1.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'values'
>>> assert sum(norm) ==1.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>> norm
[0.09948726141723166, 0.12779375187630868, 0.072334327641798, 0.2521088089137424, 0.2825216040629086, 0.14631411446671067, 0.15764561305840522, 0.5597701904100805, 0.4449124564482076, 0.5064838617888352, 0.555563780553796, 0.3075222199851642, 0.3775361070563293, 0.6522747237477724, 0.3016075606448321, 0.7778052796336673, 1.0, 0.4194271979829725, 0.518436114130818, 0.7313244553875791, 0.06902117623475387, 0.6260792250652055, 0.08365442777868967, 0.4454244047514851, 0.06461590779610998, 0.2103894705078303, -0.02583051296969432, 0.24683400767425423]
>>> sum(norm)
10.011057536045795
>>> arr
[8.52895974e-05, 0.000109556515, 6.20116143e-05, 0.000216130774, 0.000242203409, 0.000125433867, 0.000135148266, 0.000479886304, 0.000381419729, 0.00043420438, 0.000476280184, 0.000263636228, 0.000323658548, 0.000559189667, 0.00025856564, 0.000666805963, 0.000857291639, 0.00035957143, 0.000444450946, 0.000626958341, 5.91712773e-05, 0.000536732485, 7.17162415e-05, 0.000381858618, 5.53946775e-05, 0.000180365134, -2.21442828e-05, 0.000211608731]
>>> for x in arr:
...
...
  File "<stdin>", line 3

    ^
IndentationError: expected an indented block
>>> normz = []
>>> for x in arr:
...     z = (x - min(arr))/(max(arr) - min(arr))
...
>>> for x in arr:
...     z = (x - min(arr))/(max(arr) - min(arr))
...     normz.append(z)
...
>>> normz
[0.12216226053185085, 0.14975599078377333, 0.09569304029309213, 0.27094078248737735, 0.30058778047062484, 0.1678100088269558, 0.17885617917227997, 0.5708552202103145, 0.4588896152592888, 0.5189106465721355, 0.5667547281669386, 0.3249588784309311, 0.39320980895597524, 0.6610304803221424, 0.31919315079312693, 0.7834001644939402, 1.0, 0.43404607810278784, 0.5305619400274082, 0.7380897319630048, 0.09246331436355937, 0.6354945868666698, 0.10672809919782379, 0.4593886726540581, 0.08816897101643956, 0.23027194111597182, 0.0, 0.26579880126065597]
>>> import numpy as np
>>> def softmax(x):
...     e_x = np.exp(x - np.max(x))
...     return e_x / e_x.sum()
...
>>> scores = [3.0, 1.0, 0.2]
>>> print(softmax(scores))
[0.8360188  0.11314284 0.05083836]
>>> hh1 = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
>>> h1= [ 1, 2, 3, 4, 5, 6, 7, 8 ]
>>> print(softmax(h1))
[5.76612770e-04 1.56739601e-03 4.26062410e-03 1.15815771e-02
 3.14819905e-02 8.55769227e-02 2.32622194e-01 6.32332683e-01]
>>> hh1 = softmax(h1)
>>> sum(hh1)
1.0
>>> norm = softmax(arr)
>>> norm
array([0.03570638, 0.03570725, 0.03570555, 0.03571106, 0.03571199,
       0.03570782, 0.03570817, 0.03572048, 0.03571696, 0.03571885,
       0.03572035, 0.03571275, 0.0357149 , 0.03572331, 0.03571257,
       0.03572715, 0.03573396, 0.03571618, 0.03571921, 0.03572573,
       0.03570545, 0.03572251, 0.0357059 , 0.03571698, 0.03570532,
       0.03570978, 0.03570255, 0.0357109 ])
>>> np.sum(norm)
1.0
>>> from dictances import bhattacharyya
>>> bhattacharyya(norm, norm)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/bhattacharyya.py", line 47, in bhattacharyya
    distance = -np.log(bhattacharyya_coefficient(a, b))
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/bhattacharyya.py", line 25, in bhattacharyya_coefficient
    for k, small_value in small.items():
AttributeError: 'numpy.ndarray' object has no attribute 'items'
>>> k = norm.tolist()
>>> k
[0.035706384882874045, 0.03570725137728732, 0.035705553719924114, 0.035711057053933765, 0.03571198814742777, 0.03570781831838714, 0.035708165200066574, 0.03572047728497829, 0.035716960185083906, 0.03571884554212057, 0.035720348472882996, 0.03571275356420836, 0.035714897190862946, 0.035723310151281384, 0.03571257248000779, 0.035727154768468744, 0.03573396092791373, 0.03571617983878306, 0.03571921153950397, 0.03572573115467439, 0.03570545230426281, 0.035722507915411685, 0.03570590023069331, 0.035716975860868284, 0.0357053174593134, 0.035709779847963335, 0.03570254901345302, 0.035710895567363315]
>>> bhattacharyya(k,k)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/bhattacharyya.py", line 47, in bhattacharyya
    distance = -np.log(bhattacharyya_coefficient(a, b))
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/bhattacharyya.py", line 25, in bhattacharyya_coefficient
    for k, small_value in small.items():
AttributeError: 'list' object has no attribute 'items'
>>> assert bhattacharyya(k,k) == 0.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/bhattacharyya.py", line 47, in bhattacharyya
    distance = -np.log(bhattacharyya_coefficient(a, b))
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/bhattacharyya.py", line 25, in bhattacharyya_coefficient
    for k, small_value in small.items():
AttributeError: 'list' object has no attribute 'items'
>>> assert bhattacharyya(hh1, hh1) == 0.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/bhattacharyya.py", line 47, in bhattacharyya
    distance = -np.log(bhattacharyya_coefficient(a, b))
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/bhattacharyya.py", line 25, in bhattacharyya_coefficient
    for k, small_value in small.items():
AttributeError: 'numpy.ndarray' object has no attribute 'items'
>>> assert bhattacharyya(hh1, k) == 0.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/bhattacharyya.py", line 47, in bhattacharyya
    distance = -np.log(bhattacharyya_coefficient(a, b))
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/bhattacharyya.py", line 25, in bhattacharyya_coefficient
    for k, small_value in small.items():
AttributeError: 'numpy.ndarray' object has no attribute 'items'
>>> op = ['1', '2', '3','4','5']
>>> opdict = dict(enumerate(op.flatten(), 1)
...
...
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'flatten'
>>> op = np.array(['1', '2', '3','4','5'])
>>> opdict = dict(enumerate(op.flatten(), 1))
>>> opdcit
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'opdcit' is not defined
>>> opdict
{1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}
>>> opdict = dict(enumerate(op.flatten(), 0))
>>> opdict
{0: '1', 1: '2', 2: '3', 3: '4', 4: '5'}
>>> opdict = dict(enumerate(op.flatten())
... )
>>> opdict
{0: '1', 1: '2', 2: '3', 3: '4', 4: '5'}
>>> k
[0.035706384882874045, 0.03570725137728732, 0.035705553719924114, 0.035711057053933765, 0.03571198814742777, 0.03570781831838714, 0.035708165200066574, 0.03572047728497829, 0.035716960185083906, 0.03571884554212057, 0.035720348472882996, 0.03571275356420836, 0.035714897190862946, 0.035723310151281384, 0.03571257248000779, 0.035727154768468744, 0.03573396092791373, 0.03571617983878306, 0.03571921153950397, 0.03572573115467439, 0.03570545230426281, 0.035722507915411685, 0.03570590023069331, 0.035716975860868284, 0.0357053174593134, 0.035709779847963335, 0.03570254901345302, 0.035710895567363315]
>>> value_key = []
>>> for x in k:
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block
>>>
>>> enumval = enumerate(k)
>>> enumval
<enumerate object at 0x103cbefc0>
>>> print(enumval)
<enumerate object at 0x103cbefc0>
>>> val = 0
>>> for i in k:
...     val = val +1
...     print(val)
...
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
>>> string_index = []
>>> val = 0
>>> for i in k:
...     val = val +1
...     str_in = "value" + str(val)
...     string_index.append(str_in)
...
>>> string_index
['value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7', 'value8', 'value9', 'value10', 'value11', 'value12', 'value13', 'value14', 'value15', 'value16', 'value17', 'value18', 'value19', 'value20', 'value21', 'value22', 'value23', 'value24', 'value25', 'value26', 'value27', 'value28']
>>> a = zip(string_index, k)
>>> a
<zip object at 0x103cc3688>
>>> list(a)
[('value1', 0.035706384882874045), ('value2', 0.03570725137728732), ('value3', 0.035705553719924114), ('value4', 0.035711057053933765), ('value5', 0.03571198814742777), ('value6', 0.03570781831838714), ('value7', 0.035708165200066574), ('value8', 0.03572047728497829), ('value9', 0.035716960185083906), ('value10', 0.03571884554212057), ('value11', 0.035720348472882996), ('value12', 0.03571275356420836), ('value13', 0.035714897190862946), ('value14', 0.035723310151281384), ('value15', 0.03571257248000779), ('value16', 0.035727154768468744), ('value17', 0.03573396092791373), ('value18', 0.03571617983878306), ('value19', 0.03571921153950397), ('value20', 0.03572573115467439), ('value21', 0.03570545230426281), ('value22', 0.035722507915411685), ('value23', 0.03570590023069331), ('value24', 0.035716975860868284), ('value25', 0.0357053174593134), ('value26', 0.035709779847963335), ('value27', 0.03570254901345302), ('value28', 0.035710895567363315)]
>>> a.tolist()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'zip' object has no attribute 'tolist'
>>> bhattacharyya(a,a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/bhattacharyya.py", line 47, in bhattacharyya
    distance = -np.log(bhattacharyya_coefficient(a, b))
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/bhattacharyya.py", line 23, in bhattacharyya_coefficient
    big, small = sort(a, b)
  File "/Users/theman/anaconda3/lib/python3.7/site-packages/dictances/distances_utils.py", line 6, in sort
    if len(a) > len(b):
TypeError: object of type 'zip' has no len()
>>> dicta = dict(a)
>>> dicta
{}
>>> a = dict(zip(string_index, k))
>>> a
{'value1': 0.035706384882874045, 'value2': 0.03570725137728732, 'value3': 0.035705553719924114, 'value4': 0.035711057053933765, 'value5': 0.03571198814742777, 'value6': 0.03570781831838714, 'value7': 0.035708165200066574, 'value8': 0.03572047728497829, 'value9': 0.035716960185083906, 'value10': 0.03571884554212057, 'value11': 0.035720348472882996, 'value12': 0.03571275356420836, 'value13': 0.035714897190862946, 'value14': 0.035723310151281384, 'value15': 0.03571257248000779, 'value16': 0.035727154768468744, 'value17': 0.03573396092791373, 'value18': 0.03571617983878306, 'value19': 0.03571921153950397, 'value20': 0.03572573115467439, 'value21': 0.03570545230426281, 'value22': 0.035722507915411685, 'value23': 0.03570590023069331, 'value24': 0.035716975860868284, 'value25': 0.0357053174593134, 'value26': 0.035709779847963335, 'value27': 0.03570254901345302, 'value28': 0.035710895567363315}
>>> bhattacharyya(a,a)
-0.0
>>> print(softmax(scores))
[0.8360188  0.11314284 0.05083836]
>>> arr2 = [2.75892786e-05, 1.67265477e-05, 4.34808060e-05, 7.43525736e-05,
...  3.01914334e-05, 1.26403274e-05, 1.05634540e-04, 7.64196492e-05,
...  8.51308152e-05, 7.52037612e-05, 8.30790049e-05, 1.17217147e-04,
...  1.12957257e-04, 6.45848852e-05, 1.92507028e-04 ,2.13137260e-04,
...  1.15602965e-04, 2.52767621e-04, 2.33243790e-04, 1.01885352e-04,
...  1.48861529e-04, 1.53109565e-04, 1.24991793e-04, 5.73335576e-06,
...  5.55467587e-05, 2.77196114e-05, 3.57168775e-05, 7.41218539e-05]
>>> arr2_dist = softmax(arr2)
>>> arr2_dist
array([0.03571188, 0.03571149, 0.03571245, 0.03571355, 0.03571197,
       0.03571134, 0.03571467, 0.03571362, 0.03571393, 0.03571358,
       0.03571386, 0.03571508, 0.03571493, 0.0357132 , 0.03571777,
       0.0357185 , 0.03571502, 0.03571992, 0.03571922, 0.03571453,
       0.03571621, 0.03571636, 0.03571536, 0.0357111 , 0.03571288,
       0.03571188, 0.03571217, 0.03571354])
>>> arr2_d = array(arra_dist)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'array' is not defined
>>> arr2_d = arr2_dist.tolist()
>>> arr2_d
[0.03571187799707073, 0.03571149007065709, 0.03571244551786781, 0.03571354804120459, 0.035711970925026384, 0.03571134414593956, 0.035714665248688576, 0.03571362186388463, 0.03571393297252821, 0.03571357844014677, 0.03571385969438786, 0.03571507892001598, 0.035714926778032494, 0.035713199204099336, 0.035717768005286955, 0.03571850487872834, 0.03571502126942499, 0.03571992044402056, 0.03571922306113829, 0.03571453134794521, 0.035716209119498625, 0.03571636084356301, 0.03571535659319085, 0.03571109748955014, 0.03571287642514587, 0.03571188265150009, 0.035712168250070585, 0.03571353980138645]
>>> b = dict(zip(string_index, arr2_d))
>>> b
{'value1': 0.03571187799707073, 'value2': 0.03571149007065709, 'value3': 0.03571244551786781, 'value4': 0.03571354804120459, 'value5': 0.035711970925026384, 'value6': 0.03571134414593956, 'value7': 0.035714665248688576, 'value8': 0.03571362186388463, 'value9': 0.03571393297252821, 'value10': 0.03571357844014677, 'value11': 0.03571385969438786, 'value12': 0.03571507892001598, 'value13': 0.035714926778032494, 'value14': 0.035713199204099336, 'value15': 0.035717768005286955, 'value16': 0.03571850487872834, 'value17': 0.03571502126942499, 'value18': 0.03571992044402056, 'value19': 0.03571922306113829, 'value20': 0.03571453134794521, 'value21': 0.035716209119498625, 'value22': 0.03571636084356301, 'value23': 0.03571535659319085, 'value24': 0.03571109748955014, 'value25': 0.03571287642514587, 'value26': 0.03571188265150009, 'value27': 0.035712168250070585, 'value28': 0.03571353980138645}
>>> bhattacharyya(a,b)
5.000023296796279e-09
>>>
