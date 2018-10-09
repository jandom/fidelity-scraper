#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json("results.json")

columns = [
    'GBRReturnM0',
    'GBRReturnM12',
    'GBRReturnM36',
    'GBRReturnM60',
    'GBRReturnM120',
]

fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(5*4, 6), dpi=300)

# plot violin plot
for i, column in enumerate(columns):
    ax = axes[i]
    series = df[column]
    values = series[~series.isnull()]
    # ax.hist(values)
    ax.violinplot(values, showmeans=False, showmedians=True)
    ax.set_title("{} (N={})".format(column, len(values)))
    ax.set_ylabel('Percentage return', fontsize=18)
    ax.set_ylim(-40, 40)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(18)

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(18)

# adding horizontal grid lines
for ax in axes:
    ax.yaxis.grid(True)

fig.tight_layout()
fig.savefig("plot.png")
