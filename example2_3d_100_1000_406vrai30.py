#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Demonstrate usage of LFPy.Network with network of ball-and-stick type
morphologies with active HH channels inserted in the somas and passive-leak
channels distributed throughout the apical dendrite. The corresponding
morphology and template specifications are in the files BallAndStick.hoc and
BallAndStickTemplate.hoc.
Execution (w. MPI):
    mpirun -np 2 python example_network.py
Copyright (C) 2017 Computational Neuroscience Group, NMBU.
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
# import modules:
import faulthandler
faulthandler.enable()
import time
import tkinter
# start_time = time.time()
from datetime import timedelta
start_time = time.monotonic()
import gc
import os
import matplotlib
# matplotlib.use('Agg')
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
# import seaborn as sns
from scipy import signal
from scipy.integrate import simps
# import seaborn as sns
from scipy import signal
from scipy.integrate import simps
import json
import scipy.fftpack as ff
# import seaborn as sns
import pickle
import sys
import random
from scipy.signal import savgol_filter
np.set_printoptions(threshold=sys.maxsize)

# np.set_printoptions(threshold=sys.maxsize)

# set up MPI variables:
COMM = MPI.COMM_WORLD
SIZE = COMM.Get_size()
RANK = COMM.Get_rank()

# avoid same sequence of random numbers from numpy and neuron on each RANK,
# e.g., in order to draw unique cell and synapse locations and random synapse
# activation times
# GLOBALSEED = 1234
# np.random.seed(GLOBALSEED + RANK)
# GLOBALSEED = [1234, 1430]
# GLOBALSEED = [1234, 1430, 1500, 1570, 1640, 1700, 1800]
# GLOBALSEED = [1330, 1370, 1430, 1500, 1570, 1640, 1700, 1800, 1900, 2345]
# dictEEG = {}
# dictEEG_xarr = {}
# dictEEG_FFT = {}
# a_ratio = []
# b_ratio = []
network_size = 300

freq_sim = 120

#this number here will allow one to set the number of neurons contained within a network of neurons
# network_size = 30


# [up5gYTZ

# //home/agoulouzegouna

# probalities =  [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# ratios = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# probabilities = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# probabilities1 = [ 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# probabilities2 = [ 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# probabilities =  [0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 0.9]
# probabilities1 = [0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 0.9]
# probabilities2 = [0.1, 0.2, 0.4, 0.5, 0.6, 0.8 , 0.9]


# probl = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# prob = 0.8
# ratios = [ 3, 4


##########################
# THE idea of this code is to run 2 dimensional simulations over network of neurons
#where the 2 variables are probability of connection between E-I and the ratio E-I

# 51.133368492126465  72.84180450439453 65.02235698699951 92.92984867095947

# here we set the ratio between E and I  before we run simulations
# ratios = [3]
# ratios = [ 2]
# for rat in ratios:
rat = 4
#here we set the probability of connection between E and I newurons
# probabilities = [0.6]
# probabilities = [ 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
# probabilities = [ 0.8]
# ratios = [16, 20]
# ratios = [ 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for prob in probabilities:

# prob_i_e = 0.4
# prob=0.6
probabilities =  [  0.2, 0.5, 0.6, 0.7, 0.9]
# probabilities3 =  [ 0.3, 0.7]
# probabilities1 = [ 0.3, 0.7]
# probabilities2 = [  0.3, 0.7]

probabilities3 =  [ 0.5, 0.6]
probabilities1 = [ 0.5, 0.6]
probabilities2 = [  0.5, 0.6]
for prob in probabilities:
    for prob_i_e in probabilities3:
        for prob_e_e in probabilities1:
            # prob_i_i = prob_e_e-0.2
            for prob_i_i in probabilities2:

        #for 0.8 -0.9 -== 50.52465379428308~
        #for 0.8 - 0.2 == 59.99802638071116
        # for 0.3 - 0.2 == 60.52432485773494
        #for 0.8 - 0.6 === 59.99802638071116
        # for i-i 0.1 and e-e =0.9 , e-i=0.4, i-e=0.1 59.99802638071116

        #
        # lower end
                # prob=0.8
            # prob_e_e = 0.2
            # # prob_i_e = 0.7
            # prob_i_e = 0.1
            # prob_i_i = 0.9
                # prob_e_e = 0.1
                # prob_i_e = 0.7

                # prob_i_i = 0.9

                prob_name = 'E-I'
                #64.7347126739252
                # radomness_seed = random.sample(range(1100, 10000), 2000)
                # radomness_seed = random.sample(range(1100, 10000), 5)
                # GLOBALSEED = radomness_seed
                # GLOBALSEED = [1234]
                # GLOBALSEED = 1234

                ## we will use the following seeds 1234, 1430, 1570, 1680,, 1800
                GLOBALSEED = 1234
                np.random.seed(GLOBALSEED + RANK)
                dictEEG = {}
                dictEEG_xarr = {}
                dictEEG_FFT = {}
                a_ratio = []
                b_ratio = []
                ratio = rat
                spikes = []
                # for glob in GLOBALSEED:
                #     np.random.seed(glob + RANK)
                # for prob in probabilities:
                    # np.random.seed(x + RANK)
                oli = 0

                # sns.set(font_scale= 1)
                ################################################################################
                # Function declarations
                ################################################################################

                def decimate(x, q=10, n=4, k=0.8, filterfun=ss.cheby1):
                    """
                    scipy.signal.decimate like downsampling using filtfilt instead of lfilter,
                    and filter coeffs from butterworth or chebyshev type 1.
                    Parameters
                    ----------
                    x : ndarray
                        Array to be downsampled along last axis.
                    q : int
                        Downsampling factor.
                    n : int
                        Filter order.
                    k : float
                        Aliasing filter critical frequency Wn will be set as Wn=k/q.
                    filterfun : function
                        `scipy.signal.filter_design.cheby1` or
                        `scipy.signal.filter_design.butter` function
                    Returns
                    -------
                    ndarray
                        Downsampled signal.
                    """
                    if not isinstance(q, int):
                        raise TypeError("q must be an integer")

                    if n is None:
                        n = 1

                    if filterfun == ss.butter:
                        b, a = filterfun(n, k / q)
                    elif filterfun == ss.cheby1:
                        b, a = filterfun(n, 0.05, k / q)
                    else:
                        raise Exception('only ss.butter or ss.cheby1 supported')

                    try:
                        y = ss.filtfilt(b, a, x)
                    except: # Multidim array can only be processed at once for scipy >= 0.9.0
                        y = []
                        for data in x:
                            y.append(ss.filtfilt(b, a, data))
                        y = np.array(y)

                    try:
                        return y[:, ::q]
                    except:
                        return y[::q]

                def remove_axis_junk(ax, lines=['right', 'top']):
                    """remove chosen lines from plotting axis"""
                    for loc, spine in ax.spines.items():
                        if loc in lines:
                            spine.set_color('none')
                    ax.xaxis.set_ticks_position('bottom')
                    ax.yaxis.set_ticks_position('left')

                def draw_lineplot(
                        ax, data, dt=0.1,
                        T=(0, 200),
                        scaling_factor=1.,
                        vlimround=None,
                        label='local',
                        scalebar=True,
                        unit='mV',
                        ylabels=True,
                        color='r',
                        ztransform=True,
                        filter_data=False,
                        filterargs=dict(N=2, Wn=0.02, btype='lowpass')):
                    """helper function to draw line plots"""
                    tvec = np.arange(data.shape[1])*dt
                    tinds = (tvec >= T[0]) & (tvec <= T[1])

                    # apply temporal filter
                    if filter_data:
                        b, a = ss.butter(**filterargs)
                        data = ss.filtfilt(b, a, data, axis=-1)

                    #subtract mean in each channel
                    if ztransform:
                        dataT = data.T - data.mean(axis=1)
                        data = dataT.T

                    zvec = -np.arange(data.shape[0])
                    vlim = abs(data[:, tinds]).max()
                    if vlimround is None:
                        vlimround = 2.**np.round(np.log2(vlim)) / scaling_factor
                    else:
                        pass

                    yticklabels = []
                    yticks = []

                    for i, z in enumerate(zvec):
                        if i == 0:
                            ax.plot(tvec[tinds], data[i][tinds] / vlimround + z, lw=1,
                                    rasterized=False, label=label, clip_on=False,
                                    color=color)
                        else:
                            ax.plot(tvec[tinds], data[i][tinds] / vlimround + z, lw=1,
                                    rasterized=False, clip_on=False,
                                    color=color)
                        yticklabels.append('ch. %i' % (i+1))
                        yticks.append(z)

                    if scalebar:
                        ax.plot([tvec[-1], tvec[-1]],
                                [-1, -2], lw=2, color='k', clip_on=False)
                        ax.text(tvec[-1]+np.diff(T)*0.02, -1.5,
                                '$2^{' + '{}'.format(np.log2(vlimround)
                                                    ) + '}$ ' + '{0}'.format(unit),
                                color='k', rotation='vertical',
                                va='center')

                    ax.axis(ax.axis('tight'))
                    ax.yaxis.set_ticks(yticks)
                    if ylabels:
                        ax.yaxis.set_ticklabels(yticklabels)
                        ax.set_ylabel('channel', labelpad=0.1)
                    else:
                        ax.yaxis.set_ticklabels([])
                    remove_axis_junk(ax, lines=['right', 'top'])
                    ax.set_xlabel(r't (ms)', labelpad=0.1)

                    return vlimround

                ################################################################################
                # Set up shared and population-specific parameters
                ################################################################################
                # relative path for simulation output:
                OUTPUTPATH = 'example_network3_output_oli_||' + prob_name + '_' +str(rat)+"_"+str(prob)+"_| prob E-E"+str(prob_e_e)+"_"+ " |prob i i "+ str(prob_i_i)+ " |prob i e "+ str(prob_i_e)+ " network_"+ str(network_size) + " freq" + str(freq_sim) + "Hz"

                # class NetworkCell parameters:
                cellParameters = dict(
                    morphology='BallAndStick.hoc',
                    templatefile='BallAndStickTemplate.hoc',
                    templatename='BallAndStickTemplate',
                    templateargs=None,
                    delete_sections=False,
                )

                # class NetworkPopulation parameters:
                populationParameters = dict(
                    Cell=NetworkCell,
                    cell_args=cellParameters,
                    pop_args=dict(
                        radius=100.,
                        loc=0.,
                        scale=20.),
                    rotation_args=dict(x=0., y=0.),
                )

                # class Network parameters:
                networkParameters = dict(
                    dt=2**-4,
                    tstop=2000.,
                    v_init=-65.,
                    celsius=6.5,
                    OUTPUTPATH=OUTPUTPATH
                )

                # class RecExtElectrode parameters:
                electrodeParameters = dict(
                    x=np.zeros(13),
                    y=np.zeros(13),
                    z=np.linspace(1000., -200., 13),
                    N=np.array([[0., 1., 0.] for _ in range(13)]),
                    r=5.,
                    n=50,
                    sigma=0.3,
                    method="soma_as_point"
                )

                # method Network.simulate() parameters:
                networkSimulationArguments = dict(
                    rec_current_dipole_moment=True,
                    rec_pop_contributions=True,
                    to_memory=True,
                    to_file=False
                )

                # population names, sizes and connection probability:
                population_names = ['E', 'I']
                # population_names = ['E', ]
                unite = network_size /(ratio+1)
                population_sizes = [round(unite*ratio), round(unite)]
                # population_sizes = [ 80, 20]
                connectionProbability = [[prob_e_e, prob], [prob_i_e, prob_i_i]]

                # synapse model. All corresponding parameters for weights,
                # connection delays, multapses and layerwise positions are
                # set up as shape (2, 2) nested lists for each possible
                # connection on the form:
                # [["E:E", "E:I"],
                #  ["I:E", "I:I"]].
                synapseModel = neuron.h.Exp2Syn
                # synapse parameters
                synapseParameters = [[dict(tau1=0.2, tau2=1.8, e=0.),
                                      dict(tau1=0.2, tau2=1.8, e=0.)],
                                     [dict(tau1=0.1, tau2=9.0, e=-80.),
                                      dict(tau1=0.1, tau2=9.0, e=-80.)]]
                # synapse max. conductance (function, mean, st.dev., min.):
                weightFunction = np.random.normal
                weightArguments = [[dict(loc=0.002, scale=0.0002),
                                    dict(loc=0.002, scale=0.0002)],
                                   [dict(loc=0.02, scale=0.002),
                                    dict(loc=0.02, scale=0.002)]]
                minweight = 0.
                # conduction delay (function, mean, st.dev., min.):
                delayFunction = np.random.normal
                delayArguments = [[dict(loc=1.5, scale=0.3),
                                   dict(loc=1.5, scale=0.3)],
                                  [dict(loc=1.5, scale=0.3),
                                   dict(loc=1.5, scale=0.3)]]
                mindelay = 0.3
                multapseFunction = np.random.normal
                multapseArguments = [[dict(loc=2., scale=.5), dict(loc=2., scale=.5)],
                                     [dict(loc=5., scale=1.), dict(loc=5., scale=1.)]]
                # method NetworkCell.get_rand_idx_area_and_distribution_norm
                # parameters for layerwise synapse positions:
                synapsePositionArguments = [[dict(section=['soma', 'apic'],
                                                  fun=[st.norm, st.norm],
                                                  funargs=[dict(loc=500., scale=100.),
                                                           dict(loc=500., scale=100.)],
                                                  funweights=[0.5, 1.]
                                                 ) for _ in range(2)],
                                            [dict(section=['soma', 'apic'],
                                                  fun=[st.norm, st.norm],
                                                  funargs=[dict(loc=0., scale=100.),
                                                           dict(loc=0., scale=100.)],
                                                  funweights=[1., 0.5]
                                                 ) for _ in range(2)]]

                if __name__ == '__main__':
                    ############################################################################
                    # Main simulation
                    ############################################################################
                    # create directory for output:
                    if not os.path.isdir(OUTPUTPATH):
                        if RANK == 0:
                            os.mkdir(OUTPUTPATH)
                    COMM.Barrier()

                    # instantiate Network:
                    network = Network(**networkParameters)

                    # create E and I populations:
                    for name, size in zip(population_names, population_sizes):
                        network.create_population(name=name, POP_SIZE=size,
                                                  **populationParameters)


                        # create excitatory background synaptic activity for each cell
                        # with Poisson statistics
                        for cell in network.populations[name].cells:
                            idx = cell.get_rand_idx_area_norm(section='allsec', nidx=64)
                            for i in idx:
                                syn = Synapse(cell=cell, idx=i, syntype='Exp2Syn',
                                              weight=0.002,
                                              **dict(tau1=0.2, tau2=1.8, e=0.))
                                # syn.set_spike_times_w_netstim(noise= 0.1,interval=90)

                                # spiking options
                                syn.set_spike_times_w_netstim( noise= 0.2, interval=1000/freq_sim)


                    # create connectivity matrices and connect populations:
                    for i, pre in enumerate(population_names):
                        for j, post in enumerate(population_names):
                            # boolean connectivity matrix between pre- and post-synaptic neurons
                            # in each population (postsynaptic on this RANK)
                            connectivity = network.get_connectivity_rand(
                                pre=pre, post=post,
                                connprob=connectionProbability[i][j]
                                )

                            # connect network:
                            (conncount, syncount) = network.connect(
                                pre=pre, post=post,
                                connectivity=connectivity,
                                syntype=synapseModel,
                                synparams=synapseParameters[i][j],
                                weightfun=np.random.normal,
                                weightargs=weightArguments[i][j],
                                minweight=minweight,
                                delayfun=delayFunction,
                                delayargs=delayArguments[i][j],
                                mindelay=mindelay,
                                multapsefun=multapseFunction,
                                multapseargs=multapseArguments[i][j],
                                syn_pos_args=synapsePositionArguments[i][j],
                                )

                    # set up extracellular recording device:
                    electrode = RecExtElectrode(**electrodeParameters)

                    # run simulation:
                    SPIKES, OUTPUT, DIPOLEMOMENT = network.simulate(
                        electrode=electrode,
                        **networkSimulationArguments
                    )

                    # collect somatic potentials across all RANKs to RANK 0:
                    if RANK == 0:
                        somavs = []
                        for i, name in enumerate(population_names):
                            somavs.append([])
                            somavs[i] += [cell.somav
                                          for cell in network.populations[name].cells]
                            for j in range(1, SIZE):
                                somavs[i] += COMM.recv(source=j, tag=15)
                    else:
                        somavs = None
                        for name in population_names:
                            COMM.send([cell.somav for cell in network.populations[name].cells],
                                      dest=0, tag=15)

                    ############################################################################
                    # Plot some output on RANK 0
                    ############################################################################
                    if RANK == 0:
                                # spike raster
                        fig, ax = plt.subplots(1, 1)

                        spikes_per_neuron_E = {}
                        spikes_gids_per_neuron_E = {}
                        spikes_per_neuron_E_arr = []
                        spikes_per_neuron_I = {}
                        spikes_gids_per_neuron_I = {}
                        spikes_per_neuron_I_arr = []

                        for name, spts, gids in zip(population_names, SPIKES['times'], SPIKES['gids']):
                            t = []
                            g = []
                            for spt, gid in zip(spts, gids):
                                t = np.r_[t, spt]
                                g = np.r_[g, np.zeros(spt.size)+gid]
                            ax.plot(t[t >= 200], g[t >= 200], '|', label=name)
                            print("the value of time for spiking")
                            print(g)
                            print("the value at which there are spikes")
                            print(t)
                            ax.legend(loc=1)
                            remove_axis_junk(ax, lines=['right', 'top'])
                            ax.set_xlabel('t (ms)')
                            ax.set_ylabel('gid')
                            ax.set_title('spike raster')
                            nom = 'spike_raster_'+str(prob)+'.pdf'
                            fig.savefig(os.path.join(OUTPUTPATH, 'spike_raster.pdf'),
                                        bbox_inches='tight')
                            ax.set_xlim([800, 900])
                            fig.savefig(os.path.join(OUTPUTPATH, 'spike_raster_800_900.pdf'),
                                        bbox_inches='tight')
                            ax.set_xlim([830, 870])
                            fig.savefig(os.path.join(OUTPUTPATH, 'spike_raster_830_870.pdf'),
                                        bbox_inches='tight')

                        # plt.close(fig)
                            # data = np.hstack(SPIKES['times'])
                            data = spts
                            data_count = []
                            # data_time = [0.2 , 0.38, 0.56, 0.74, 0.92, 1.1 , 1.28, 1.46, 1.64, 1.82]
                            start_time = 0.2
                            end_time = 2
                            # data_time = np.arange(start_time, end_time, (end_time - start_time)/)
                            # data1= []
                            # data2 =[]
                            # for x in data:


                            if name=="E":
                                # print(spt)
                                # data_count.append(x.size)
                                data1 = np.hstack(spts)
                                spikes_per_neuron_E["E"] = data1
                                data3 = np.hstack(gids)
                                spikes_gids_per_neuron_E["E"] = data3
                                print("E spiking rate")
                                print(spikes_per_neuron_E)
                                f = open(OUTPUTPATH + "/E_spiking"  +".txt","w")
                                f.write( str(spikes_per_neuron_E ))
                                f.close()


                            elif name=="I":
                                data2 = np.hstack(spts)
                                spikes_per_neuron_I["I"] = data2
                                spikes_per_neuron_I_arr = data2
                                data4 = np.hstack(gids)
                                spikes_gids_per_neuron_E["I"] = data4

                            # for datax in data:
                            #     data_count.append(datax.size/1.8)
                            #     print("the firing rate is ")
                            #     print(datax.size/1.8)
                                # print(data_count)


                                # print(x.size/1.8)
                                # if population_names == "E":
                                #     spikes_per_neuron_E["E"] = data
                                # else:
                                # print("the value of E number of spike")
                                # print(spikes_per_neuron_E)
                                # print("the value of I number of spike")
                                #     spikes_per_neuron_I["I"] = data
                                # print(spikes_per_neuron_I)
                            # print(data_count)
                            # # interval_range = len(data_count)
                            # interval_range =
                            # data_time = np.arange(start_time, end_time, (end_time - start_time)/interval_range)
                            # print( "the value of the max for this simulation is")
                            # print(max(data_count))
                            # f = open(OUTPUTPATH + "/max_spike_" + "spike_count" + str(glob) +".txt","w")
                            # f.write( str(max(data_count) ))
                            # f.close()
                            #
                            # f = open(OUTPUTPATH + "/average_spike_" + "spike_count"+ str(glob) + ".txt","w")
                            # f.write( str(np.average(data_count) ))
                            # f.close()

                            spikes.append(np.average(data_count))
                            print(spikes)


                            # plt.show()



                                # print(spikes_per_neuron_I)
                            # data_count = []
                            # data1= []
                            # data2 =[]
                            # print("the data is ")
                            # print(data.size)
                            # print("the data indice 0 is  ")
                            # print(data[0].size)
                            # print("the data indice 1 is  ")
                            # print(data[1].size)
                            # print("the data indice 2 is  ")
                            # print(data[2].size)
                            # for x in data:
                            #     data_count.append(x.size/1.8)
                            #     print(x.size/1.8)
                            #     if population_names == "E":
                            #         spikes_per_neuron_E["E"] = data
                            #     else:
                                # print("the value of E number of spike")
                                # print(spikes_per_neuron_E)
                                # print("the value of I number of spike")
                                    # spikes_per_neuron_I["I"] = data
                                # print(spikes_per_neuron_I)

                            # if spikes_per_neuron_E == spikes_per_neuron_I:
                            #     print("array are the same again")

                            print("the value of E number of spike")
                            print(spikes_per_neuron_E)
                            print("The length of E is ")
                            print(len(spikes_per_neuron_E['E']))
                            print("the average spking rate for E ")
                            E_spiking_rate= len(spikes_per_neuron_E['E'])/1.8
                            f = open(OUTPUTPATH + "/E_spiking_rate" + str(prob) + ".txt","w")
                            E_spiking_rate = np.array(E_spiking_rate, dtype=np.float32)
                            f.write( str(E_spiking_rate))
                            f.close()
                            print("array for E")
                            print(spikes_per_neuron_E_arr)
                            print("the length of the array")
                            print(len(spikes_per_neuron_E_arr))
                            # print("the average spking rate for I ")
                            # print(len(spikes_per_neuron_E_arr)/1.8)
                            # print("here is the gids")
                            # print(spikes_gids_per_neuron_E["E"])
                            print("the value of I number of spike")
                            print(spikes_per_neuron_I)
                            print("the length of I is ")
                            print(len(spikes_per_neuron_I))
                            print("array for I")
                            print(spikes_per_neuron_I_arr)
                            print("the length of the array ")
                            print(len(spikes_per_neuron_I_arr))
                            print("the average spking rate for I ")
                            print(len(spikes_per_neuron_I_arr)/1.8)

                            I_spiking_rate= len(spikes_per_neuron_I_arr)/1.8
                            f = open(OUTPUTPATH + "/I_spiking_rate" + str(prob) + ".txt","w")
                            I_spiking_rate = np.array(I_spiking_rate, dtype=np.float32)
                            f.write( str(I_spiking_rate ))
                            f.close()
                            # print("here is the gids for I")
                            # print(spikes_gids_per_neuron_E["I"])
                            # print("the data count is  ")
                            # print(data_count)
                            # f = open(OUTPUTPATH + "/prob_a_full_" + "spike count "+ str(prob) + ".txt","w")
                            # f.write( str(data_count ))
                            # f.close()
                # print(data_count)
                            # f = open(OUTPUTPATH + "/prob_a_full_" + "spike count "+ str(prob) + ".txt","w")
                            # f.write( str(data_count ))
                            # f.close()
                        # ax.hist(data, bins=bins, color=colors[i][:-1], label=m_name)


                        # Test the spike count code


                        # somatic potentials
                        fig = plt.figure()
                        gs = GridSpec(5, 1)
                        ax = fig.add_subplot(gs[:4])
                        draw_lineplot(ax, decimate(np.array(somavs)[0], q=16), dt=network.dt*16,
                                      T=(200, 2000),
                                      scaling_factor=1.,
                                      vlimround=16,
                                      label='E',
                                      scalebar=True,
                                      unit='mV',
                                      ylabels=False,
                                      color='C0',
                                      ztransform=True
                                     )
                        ax.set_yticks([])
                        ax.set_xticklabels([])
                        ax.set_ylabel('E')
                        ax.set_title('somatic potentials')
                        ax.set_xlabel('')

                        ax = fig.add_subplot(gs[4])
                        draw_lineplot(ax, decimate(np.array(somavs)[1], q=16), dt=network.dt*16,
                                      T=(200, 2000),
                                      scaling_factor=1.,
                                      vlimround=16,
                                      label='I',
                                      scalebar=True,
                                      unit='mV',
                                      ylabels=False,
                                      color='C1',
                                      ztransform=True
                                     )
                        ax.set_yticks([])
                        ax.set_ylabel('I')

                        fig.savefig(os.path.join(OUTPUTPATH, 'soma_potentials.pdf'),
                                    bbox_inches='tight')
                        plt.close(fig)


                        # extracellular potentials, E and I contributions, sum
                        fig, axes = plt.subplots(1, 3, figsize=(6.4, 4.8))
                        fig.suptitle('extracellular potentials')
                        for i, (ax, name, label) in enumerate(zip(axes, ['E', 'I', 'imem'],
                                                                  ['E', 'I', 'sum'])):
                            draw_lineplot(ax, decimate(OUTPUT[0][name], q=16), dt=network.dt*16,
                                          T=(200, 2000),
                                          scaling_factor=1.,
                                          vlimround=None,
                                          label=label,
                                          scalebar=True,
                                          unit='mV',
                                          ylabels=True if i == 0 else False,
                                          color='C{}'.format(i),
                                          ztransform=True
                                         )
                            ax.set_title(label)
                        fig.savefig(os.path.join(OUTPUTPATH, 'extracellular_potential.pdf'),
                                    bbox_inches='tight')
                        plt.close(fig)


                        # current-dipole moments, E and I contributions, sum
                        fig, axes = plt.subplots(3, 3, figsize=(6.4, 4.8))
                        fig.subplots_adjust(wspace=0.45)
                        fig.suptitle('current-dipole moments')
                        for i, u in enumerate(['x', 'y', 'z']):
                            for j, label in enumerate(['E', 'I', 'sum']):
                                t = np.arange(DIPOLEMOMENT.shape[0])*network.dt
                                inds = (t >= 200) & (t <= 2000)
                                if label != 'sum':
                                    axes[i, j].plot(t[inds][::16],
                                                    decimate(DIPOLEMOMENT[label][inds, i],
                                                             q=16),
                                                    'C{}'.format(j))
                                else:
                                    axes[i, j].plot(t[inds][::16],
                                                    decimate(DIPOLEMOMENT['E'][inds, i] +
                                                             DIPOLEMOMENT['I'][inds, i], q=16),
                                                    'C{}'.format(j))

                                if j == 0:
                                    axes[i, j].set_ylabel(r'$\mathbf{p}\cdot\mathbf{e}_{' +
                                                          '{}'.format(u) +'}$ (nA$\mu$m)')
                                if i == 0:
                                    axes[i, j].set_title(label)
                                if i != 2:
                                    axes[i, j].set_xticklabels([])
                                else:
                                    axes[i, j].set_xlabel('t (ms)')
                        fig.savefig(os.path.join(OUTPUTPATH, 'current_dipole_moment.pdf'),
                                    bbox_inches='tight')
                        plt.close(fig)


                    # population illustration (per RANK)
                    fig = plt.figure(figsize=(6.4, 4.8*2))
                    ax = fig.add_subplot(111, projection='3d')
                    ax.view_init(elev=5)
                    ax.plot(electrode.x, electrode.y, electrode.z, 'ko', zorder=0)
                    for i, (name, pop) in enumerate(network.populations.items()):
                        for cell in pop.cells:
                            c = 'C0' if name == 'E' else 'C1'
                            ax.plot([cell.xstart[0], cell.xend[0]],
                                    [cell.ystart[0], cell.yend[0]],
                                    [cell.zstart[0], cell.zend[0]], c,
                                    lw=5, zorder=-cell.xmid[0]-cell.ymid[0])
                            ax.plot([cell.xstart[1], cell.xend[-1]],
                                    [cell.ystart[1], cell.yend[-1]],
                                    [cell.zstart[1], cell.zend[-1]], c,
                                    lw=0.5, zorder=-cell.xmid[0]-cell.ymid[0])
                    ax.set_xlabel('$x$ ($\mu$m)')
                    ax.set_ylabel('$y$ ($\mu$m)')
                    ax.set_zlabel('$z$ ($\mu$m)')
                    ax.set_title('network populations')
                    # fig.savefig(os.path.join(OUTPUTPATH, 'population_RANK_{}.pdf'.format(RANK)),
                                # bbox_inches='tight')
                    # plt.close(fig)



                    fig, axes = plt.subplots(3, 3, figsize=(6.4, 4.8))
                    fig.subplots_adjust(wspace=0.45)
                    fig.suptitle('current-dipole moments')
                    for i, u in enumerate(['x', 'y', 'z']):
                        for j, label in enumerate(['E', 'I', 'sum']):
                            t = np.arange(DIPOLEMOMENT.shape[0])*network.dt
                            current_dipole_moment = DIPOLEMOMENT['E'] + DIPOLEMOMENT['I']
                            t = np.arange(DIPOLEMOMENT.shape[0])*network.dt
                            radii = [79000., 80000., 85000., 90000.]
                            sigmas = [0.3, 1.5, 0.015, 0.3]
                            rad_tol = 1e-2
                            r_mid = np.array([0., 0., 77500])
                            inds = (t >= 200) & (t <= 2000)
                            if label != 'sum':
                                axes[i, j].plot(t[inds][::16],
                                                decimate(DIPOLEMOMENT[label][inds, i],
                                                         q=16),
                                                'C{}'.format(j))
                            else:
                                axes[i, j].plot(t[inds][::16],
                                                decimate(DIPOLEMOMENT['E'][inds, i] +
                                                         DIPOLEMOMENT['I'][inds, i], q=16),
                                                'C{}'.format(j))

                            if j == 0:
                                axes[i, j].set_ylabel(r'$\mathbf{p}\cdot\mathbf{e}_{' +
                                                      '{}'.format(u) +'}$ (nA$\mu$m)')
                            if i == 0:
                                axes[i, j].set_title(label)
                            if i != 2:
                                axes[i, j].set_xticklabels([])
                            else:
                                axes[i, j].set_xlabel('t (ms)')
                    # fig.savefig(os.path.join(OUTPUTPATH, 'current_dipole_moment.pdf'),
                    #             bbox_inches='tight')
                    eeg_coords_top = np.array([[0., 0., radii[3] - rad_tol]])
                    four_sphere_top = LFPy.FourSphereVolumeConductor(eeg_coords_top, radii, sigmas)
                    # four_sphere_top = LFPy.FourSphereVolumeConductor( radii, sigmas, eeg_coords_top)
                    pot_db_4s_top = four_sphere_top.calc_potential(current_dipole_moment, r_mid)

                    eeg_top = np.array(pot_db_4s_top)[0] * 1e3

                    # eeg_top = [32.0030, 34.1365, 36.2701, 38.4036, 40.5371, 42.6707, 44.8042, 46.9378, 49.0713, 51.2048, 53.3384, 55.4719, 57.6054, 59.7390, 61.8725, 64.0060, 66.1396, 68.2731, 70.4066, 72.5402, 74.6737, 76.8072, 78.9408, 81.0743, 83.2078, 85.3414, 87.4749, 89.6084
                    fig = plt.figure()
                    ax = fig.add_subplot(111, xlabel="Time (ms)", ylabel="$\mu$V", title='EEG')
                    ax.plot(t, eeg_top)
                    # print('i came to line 473')
                    fig.savefig(os.path.join(OUTPUTPATH, 'population_EEG.pdf'), bbox_inches='tight')
                    # print('will i print the graphs')


                #===============================================================================================================
                    eeg_converti = eeg_top[1600:]
                    t_converti = t[1600:]
                    ax.plot(t_converti, eeg_converti)
                    ax.set_xlim([200, 2000])
                    fig.savefig(os.path.join(OUTPUTPATH, 'population_EEG_processed.pdf'), bbox_inches='tight')
                    # print("the value of t[10000]")
                    # print(t[10000])
                    ax.set_xlim([800, 900])
                    fig.savefig(os.path.join(OUTPUTPATH, 'population_EEG_800_900.pdf'), bbox_inches='tight')

                    ax.set_xlim([830, 870])
                    fig.savefig(os.path.join(OUTPUTPATH, 'population_EEG_830_870.pdf'), bbox_inches='tight')

                    # print("the value of eeg[10000]")
                    # print(eeg_top[10000])

                #     def find_nearest(array, value):
                #         array = np.asarray(array)
                #         idx = (np.abs(array - value)).argmin()
                #         return array[idx]
                #     array = t
                #     print(array)
                # # [ 0.21069679  0.61290182  0.63425412  0.84635244  0.91599191  0.00213826
                # #   0.17104965  0.56874386  0.57319379  0.28719469]
                #     print("the value of t[100]")
                #     value = 100
                #     print(find_nearest(t, value))

                    # print("the value of t1600")
                    # print(t[1600])


                    dictEEG[prob] = eeg_converti
                    # a.append()
                #===============================================================================================================
                    # eeg_converti = eeg_top
                    # dictEEG[oli] = eeg_converti



                    foo = eeg_converti
                    with open('file1_205'+'_dataop', 'wb') as abc:
                        np.savetxt(abc, foo, delimiter=",")



                    samplingFrequency   = 200;

                    fig, axis = plt.subplots(1, 1)

                    plt.subplots_adjust(hspace=1)

                    # Time domain representation for sine wave 1

                    # axis[0].set_title('Sine wave with a frequency of 2 Hz')
                    #
                    # axis[0].plot(t_converti, eeg_converti)
                    #
                    # axis[0].set_xlabel('Time')
                    #
                    # axis[0].set_ylabel('Amplitude')

                    fourierTransform = np.fft.fft(eeg_converti)/len(eeg_converti)           # Normalize amplitude

                    fourierTransform = fourierTransform[range(int(len(eeg_converti)/2))] # Exclude sampling frequency


                    thy= np.fft.fft(eeg_converti)/len(eeg_converti)
                    pwspec = 2*(np.abs(fourierTransform)**2)
                    # print(pwspec)
                    # print(len(fourierTransform))
                    # print(len(pwspec))

                    tpCount     = len(eeg_converti)

                    values      = np.arange(int(tpCount/2))

                    timePeriod  = tpCount/samplingFrequency

                    frequencies = values/timePeriod

                    # axis[0].set_title('Fourier transform depicting the frequency components')


                    # axis[0].plot(frequencies, pwspec)
                    #
                    # axis[0].set_xlabel('Frequency')
                    #
                    # axis[0].set_ylabel('Amplitude')
                    #
                    # axis[0].set_title('Fourier transform depicting the frequency components')



                    axis.set_title('Fourier transform depicting the frequency components')


                    axis.plot(frequencies, pwspec)

                    axis.set_xlabel('Frequency')

                    axis.set_ylabel('Amplitude')

                    axis.set_title('Fourier transform depicting the frequency components')


                def return_freq_and_psd(dt, sig):
                    """ Returns the power and freqency of the input signal"""
                    sig = np.array(sig)
                    if len(sig.shape) == 1:
                        sig = np.array([sig])
                    elif len(sig.shape) == 2:
                        pass
                    else:
                        raise RuntimeError("Not compatible with given array shape!")
                    sample_freq = ff.fftfreq(sig.shape[1], d=dt/1000)
                    pidxs = np.where(sample_freq >= 0)
                    freqs = sample_freq[pidxs]

                    Y = ff.fft(sig, axis=1)[:, pidxs[0]]


                    power = np.abs(Y)**2/Y.shape[1]

                    return freqs, power

                # print("the same is the fact that ")
                z= return_freq_and_psd(2**-4, eeg_converti)
                u= z[0]
                k= z[1][0]
                # x= k[0]
                # y= k[1]
                # # k= z[2]
                dictEEG_xarr[prob] = u

                # print("u")
                p = u.tolist()

                p = u.tolist()
                first_val = 32.0030
                indice_init = [ n for n,i in enumerate(p) if i>=first_val][0]
                last_val = 89.6084
                indice_fin = [ n for n,i in enumerate(p) if i>=last_val][0]
                dictEEG_FFT[prob] = k
                k = k[indice_init:indice_fin]
                u = u[indice_init:indice_fin]


                # first_val = 32.0030
                # [ n for n,i in enumerate(p) if i>first_val ][0]


                print("the top is ieas")
                b_ratio.append(u)
                a_ratio.append(k)


                # print(a_ratio)
                # # print("k")
                # print(b_ratio)
                # np.stack((a, k))
                # np.concatenate((a,k), axis =0)


                ################### GET MAX PEAK Frequency #####################
                a_arr = a_ratio[0]
                # print('the b array')
                # print(a_arr)
                max_val_spect = max(a_arr) #get max value in the power spectrum
                print("the max value")
                print(max_val_spect)
                indox = a_arr.tolist().index(max_val_spect) #get the index for the max Value
                print("the max index")
                print(indox)
                b_arr = b_ratio[0]
                max_peak_freq = b_arr[indox]
                print("the max peak freq")
                print(max_peak_freq)
                f = open(OUTPUTPATH + "/max_peak_freq" + str(prob) + ".txt","w")
                max_peak_freq = np.array(max_peak_freq, dtype=np.float32)
                f.write( str(max_peak_freq))
                f.close()



                ###############iiiiii

                plt.plot(b_ratio[0], a_ratio[0])
                plt.xlim(32.0030, 89.6084) # a refaire to limit within bounds
                plt.savefig(os.path.join(OUTPUTPATH, 'Spectrum.png')) #to be saved instead of plotted

                #downsample to 28 elements and save to array
                downsampled =  signal.resample(a_ratio[0], 28)
                f = open(OUTPUTPATH + "/downsampled_spectrum" + str(prob) + ".txt","w")
                f.write( str(downsampled))
                f.close()

                x_axis_processed = [32.0030,   34.1365,   36.2701,   38.4036,   40.5371,   42.6707,   44.8042,   46.9378,   49.0713,   51.2048,   53.3384,   55.4719,   57.6054,   59.7390,   61.8725,   64.0060,   66.1396,   68.2731,   70.4066,   72.5402,   74.6737,   76.8072,   78.9408,   81.0743,   83.2078,   85.3414,   87.4749,   89.6084]
                plt.plot(x_axis_processed, downsampled)
                # plt.xlim(32.0030, 89.6084) # a refaire to limit within bounds
                plt.savefig(os.path.join(OUTPUTPATH, 'downsampledspectrum.png'))


                max_of_array = np.max(downsampled)
                normlized_array_downsampled = downsampled/max_of_array
                f = open(OUTPUTPATH + "/norm_downsampled_spectrum" + str(prob) + ".txt","w")
                f.write( str(normlized_array_downsampled))
                f.close()
                plt.plot(x_axis_processed, normlized_array_downsampled)
                plt.savefig(os.path.join(OUTPUTPATH, 'Normdownsampledspectrum.png'))




                # stavitszky golay
                # f = open(OUTPUTPATH + "/downsampled_spectrum" + str(prob) + ".txt","w")
                # f.write( str(downsampled))
                # f.close()

                #######################jjjjjj
                # maxo_x = u.max()
                # print(maxo_x)

                # maxo_y = k.max()
                # print(maxo_y)

                f = open(OUTPUTPATH + "/prob_a_full_" + str(prob) + ".txt","w")
                a_ratio = np.array(a_ratio, dtype=np.float32)
                f.write( str(a_ratio[0]))
                f.close()

                f = open(OUTPUTPATH + "/prob_b_full_" + str(prob) + ".txt","w")
                b_ratio = np.array(b_ratio, dtype=np.float32)
                f.write( str(b_ratio[0] ) )
                f.close()

                f = open(OUTPUTPATH + "/average_spike_array" + "spike_count"+ ".txt","w")
                f.write( str(spikes ))
                f.close()

                f = open(OUTPUTPATH + "/the_average_spike_array" + "spike_count"+ ".txt","w")
                f.write( str(np.average(spikes )))
                f.close()


                # p = u.tolist()
                # first_val = 32.0030
                # [ n for n,i in enumerate(p) if i>=first_val ][0]

                # plt.fill_between(freqs, psd, where=idx_delta, color='skyblue')
                ####uuuuuuuuu#########

                # plt.xlabel('Frequency (Hz)')
                # plt.ylabel('Power spectral density (uV^2 / Hz)')

                #kkkkkk#
                # plt.xlim([32.0030, 89.6084])
                # plt.xlim([0, 200])
                # plt.ylim([0, 1.4])

                # plt.plot(x, y)
                # plt.plot(u, k)
                # plt.show()
                # sns.despine()
                # print(return_freq_and_psd(2**-4, eeg_converti)[0])







                    ############################################################################
                    # customary cleanup of object references - the psection() function may not
                    # write correct information if NEURON still has object references in memory,
                    # even if Python references has been deleted. It will also allow the script
                    # to be run in successive fashion.
                    ############################################################################
                network.pc.gid_clear() # allows assigning new gids to threads
                electrode = None
                syn = None
                synapseModel = None
                for population in network.populations.values():
                    for cell in population.cells:
                        cell = None
                    population.cells = None
                    population = None
                pop = None
                network = None
                neuron.h('forall delete_section()')



                # print(dictEEG_FFT)
                # dict = dictEEG_FFT
                # print("la valeur de a")
                # print(a_ratio)
                # json = json.dumps(fool)
                # f = open("dict.json","w")
                # f.write(json)
                # f.close()

                # f = open("file.pkl","wb")
                # pickle.dump(dict,f)
                # f.close()



                # del dict
                delete_sections=True

                # end_time = datetime.now()
                # print("--- %s seconds ---" % (time.time() - start_time))
                # print('Duration: {}'.format(end_time - start_time))
                end_time = time.monotonic()
                print(timedelta(seconds=end_time - start_time))




                # with open('file_fft_1k'+'_dataop', 'wb') as fft:
                #     np.savetxt(fft, fool, delimiter=',')
