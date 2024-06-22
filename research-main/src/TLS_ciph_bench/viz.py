

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
 
# Read CSV into pandas
df_12_cl = pd.read_csv(r"../data/TLS_ciph_bench/df_12_cl.csv")
df_12_srv = pd.read_csv(r"../data/TLS_ciph_bench/df_12_srv.csv")
df_13_cl = pd.read_csv(r"../data/TLS_ciph_bench/df_13_cl.csv" )
df_13_srv = pd.read_csv(r"../data/TLS_ciph_bench/df_13_srv.csv")

# Generate a list of colors from the 'viridis' colormap
print(df_12_cl, df_12_srv , df_13_cl, df_13_srv)
cmap = plt.get_cmap('viridis')  # You can choose any colormap you like

def plotBenchmark(dataframe):
    # Make colors 
    # colors = [cmap(i / len(dataframe)) for i in range(len(dataframe))]
    # Create plot
    colors = [cmap(i / len(dataframe)) for i in range(len(dataframe))]
    fig, axs = plt.subplots(figsize=(12, 12))
    axs.set_xlabel('Connect time average ms')
    axs.set_ylabel('Cipher suite and group')
    frame = plt.gca()
    Labels = dataframe['Label']
    plt.barh(Labels, dataframe['Connect Avg ms'],color=colors)
    plt.tight_layout()
    label = dataframe['Label'].values
    axs.set_title('TLS_13 Average connection time over attempts within 15 seconds')
    plt.show()

    axs.set_title('TLS_13 Cipher groups Average connection time')
    plt.show()




def plotTransmittedBytes(dataframe):
    # Make colors 
    # colors = [cmap(i / len(dataframe)) for i in range(len(dataframe))]
    # Create plot
    colors = [cmap(i / len(dataframe)) for i in range(len(dataframe))]
    fig, axs = plt.subplots(figsize=(12, 12))
    axs.set_xlabel('Total bytes transmitted')
    axs.set_ylabel('Cipher suite and group')
    frame = plt.gca()
    Labels = dataframe['Label']
    plt.barh(Labels, dataframe['Total Bytes'],color=colors)
    plt.tight_layout()
    label = dataframe['Label'].values
    axs.set_title('TLS_13 total bytes transmitted over attempts within 15 seconds (RX+TX)')
    plt.show()

def addNewLineToLabels(dataframe):
    values = dataframe['Label'].values
    x_ticks = [str('\n'*(i%4) + txt) for (i, txt) in enumerate(dataframe['Label'])]
    return x_ticks

plotBenchmark(df_13_cl)
# plotBytes(df_13_cl)
# plotBufferRx(df_13_cl)

# plotTransmittedBytes(df_13_cl)

# addNewLineToLabels(df_13_cl)

