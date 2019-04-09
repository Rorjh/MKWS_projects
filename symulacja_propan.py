# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:39:49 2019

@author: Maciej
"""

import cantera as ct
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.xml')
gas.TPX=1000, 101325, 'O2:5, N2:18.8, C3H8:1'
r = ct.Reactor(gas)
sim = ct.ReactorNet([r])
times = []
T = []
OH_fraction = []
C3H8_fraction = []
O2_fraction = []
time = 1.e-1
for i in range (1,2000):
    time += 5.e-4
    sim.advance(time)
    times.append(time)
    T.append(r.T)
    OH_fraction.append(r.thermo['OH'].X)
    C3H8_fraction.append(r.thermo['C3H8'].X)
    O2_fraction.append(r.thermo['O2'].X)
    
plt.plot(times,T)
plt.xlabel('Time [ms]')
plt.ylabel('Temperature [K]')
plt.savefig('propane_sim_T', dpi=1000)
plt.show()
plt.plot(times, OH_fraction)
plt.xlabel('Time [ms]')
plt.ylabel('OH mole fraction')
plt.arrow(0, 0.008, 0.56, 0, width=0.0001, head_width=0.001, head_length=0.05, length_includes_head=True, color='r', shape='full')
plt.annotate(r'$Ignition Delay$',xy=(0.2, 0.0085), fontsize=12)
plt.savefig('propane_sim_OH', dpi=1000)
plt.show()
plt.plot(times,C3H8_fraction)
plt.xlabel('Time [ms]')
plt.ylabel('C3H8 mole fraction')
plt.savefig('propane_sim_fuel', dpi=1000)
plt.show()
plt.plot(times,O2_fraction)
plt.xlabel('Time [ms]')
plt.ylabel('O2 mole fraction')
plt.savefig('propane_sim_O2', dpi=1000)
plt.show()