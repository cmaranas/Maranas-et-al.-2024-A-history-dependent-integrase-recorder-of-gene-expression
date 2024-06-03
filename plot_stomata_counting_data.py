import seaborn as sns
import matplotlib as plt
import pandas as pd
import numpy as np
from scipy import stats

# read in data for plotting
all_data = pd.read_excel(r"C:\Users\cjmar\OneDrive - UW\Nemhauser_things\Hist_dep_tracker_paper\StomataCounting_forplotting.xlsx")
# subset data based on stomata recorder output
state2data = all_data.loc[all_data['tracker state'] == 'two']
statealphadata = all_data.loc[all_data['tracker state'] == 'alpha'] 

# plot state 2 data 
sns.set(font_scale = 1.3)
sns.set_style('whitegrid')
ax1 = sns.boxplot(data = state2data, x = state2data['line'], y = state2data['proportion'], hue = state2data['stomata type'], palette = 'Greys')
ax1.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0, title = 'Stomata type', labels = ['Anisocytic', 'Nonanisocytic', 'both'])
ax1.set_ylim(0.25, 0.75)
sns.set(rc={'figure.figsize':(5,10)})
sns.stripplot(data = state2data, x = state2data['line'], y = state2data['proportion'], hue = state2data['stomata type'], linewidth = 1, palette = 'Greys', dodge = True, ax=ax1, legend = False)
plt.pyplot.savefig(r"fill in path")

# plot state A data
ax2 = sns.boxplot(data = statealphadata, x = statealphadata['line'], y = statealphadata['proportion'], hue = statealphadata['stomata type'], palette = 'Greys')
ax2.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0, title = 'Stomata type', labels = ['Anisocytic', 'Nonanisocytic'])
ax2.set_ylim(0.15, 0.85)
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.stripplot(data = statealphadata, x = statealphadata['line'], y = statealphadata['proportion'], hue = statealphadata['stomata type'], linewidth = 1, palette = 'Greys', dodge = True, ax=ax2, legend = False)
plt.pyplot.savefig(r"fill in path")

