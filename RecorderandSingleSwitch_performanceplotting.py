import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# read in data
df = pd.read_excel("fill in path to data\LR_stomata_trackercharacterization_T1andT2.xlsx", sheet_name="T2 summary") 
LRtracker = df.loc[df['differentiation_path'] == "LR"]
stomatatracker = df.loc[df['differentiation_path'] == "stomata"]
LRtracker = LRtracker.drop(columns=['differentiation_path', 'num_US_bxb1_OS_phiC31', 'construct', 'num_seedlings', 'num_switched_seedlings', 'num_as_expected', 'num_overswitched_PB', 'num_overswitched_P', 'num_overswitched_B', 'num_underswitched_P', 'num_underswitched_B', 'num_no_switch', 'total (sanity check)'])
stomatatracker = stomatatracker.drop(columns=['differentiation_path', 'num_US_bxb1_OS_phiC31', 'construct', 'num_seedlings', 'num_switched_seedlings', 'num_as_expected', 'num_overswitched_PB', 'num_overswitched_P', 'num_overswitched_B', 'num_underswitched_P', 'num_underswitched_B', 'num_no_switch', 'total (sanity check)'])

# plot full LR recorder data
plt.rcParams.update({'font.size':30})
fig, ax1 = plt.subplots(figsize=(20, 10))
LRtracker.plot.bar(x='T2_line', stacked=True, ax=ax1, color = ('#217a47','black', '#dcc144', '#612699', 'silver', '#e36cc5', '#e26912'), legend = False, width = 0.6)
ax1.figure.savefig('fill in path to save file\LRtrackerbarplots.svg')

# plot full stomata recorder data
fig, ax2 = plt.subplots(figsize=(20, 10))
stomatatracker.plot.bar(x='T2_line', stacked=True, ax=ax2, color = ('#217a47','black', '#dcc144', '#612699', 'silver', '#e36cc5', '#e26912'), legend = False, width = 0.65)
ax2.figure.savefig('fill in path to save file\stomatatrackerbarplots.svg')

# read in data for single integrase switches
df = pd.read_excel("fill in path to data/Single_switches_Figs2and3.xlsx", sheet_name="summary") 
# subset data to only LR or only stomata genes
LRswitches = df.loc[df['differentiation_path'] == "LR"]
stomataswitches = df.loc[df['differentiation_path'] == "stomata"]
# drop unused data columns
LRswitches = LRswitches.drop(columns=['differentiation_path', 'promoter', 'construct', 'num seedlings', 'num switched seedlings', 'num specific', 'num phic31 overswitched', 'num bxb1 overswitched', 'num phic31 underswitched', 'num no switch', 'total (sanity check)', 'notes'])
stomataswitches = stomataswitches.drop(columns=['differentiation_path', 'promoter', 'construct', 'num seedlings', 'num switched seedlings', 'num specific', 'num phic31 overswitched', 'num bxb1 overswitched', 'num phic31 underswitched', 'num no switch', 'total (sanity check)', 'notes'])

# plot LR single switch data
plt.rcParams.update({'font.size':20})
fig, ax3 = plt.subplots(figsize=(20, 8))
LRswitches.plot.bar(x='construct and T2 line', stacked=True, ax=ax3, color = ('#217a47','black', 'black', 'silver'), legend = False, width=0.6)
ax3.figure.savefig('fill in path to save file\LR_singleswitch_barplots.svg')

# plot stomata single switch data
stomataswitches.plot.bar(x='construct and T2 line', stacked=True, ax=ax4, color = ('#217a47','black', 'black', 'silver'), legend = False, width=0.65)
ax4.figure.savefig('fill in path to save file\stomata_singleswitch_barplots.svg')