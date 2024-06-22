import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
 
# Read CSV into pandas
df_simple = pd.read_csv(r"../data/CRYPTO_bench/no_acceleration.csv")
df_fast = pd.read_csv(r"../data/CRYPTO_bench/fastmath.csv")
df_fast_huge = pd.read_csv(r"../data/CRYPTO_bench/fasthugemath.csv")
df_sp = pd.read_csv(r"../data/CRYPTO_bench/math-sp-all.csv")




cmap = plt.get_cmap('viridis')  # You can choose any colormap you like




def plotBenchmark(dataframe, dataframe2, dataframe3 , dataframe4, row):
    colors = [cmap(i / len(dataframe)) for i in range(len(dataframe))]

    fig, axs = plt.subplots(figsize=(12, 12))
    axs.set_ylabel('Mb/s')
    axs.set_xlabel('Symmetric hash')

    frame = plt.gca()
    Labels = dataframe['Algorithm']

    print(Labels.values)
    X_axis =np.arange(len(Labels))
    width = 0.25
    plt.xticks(X_axis + width ,Labels.values, rotation=90)
    plt.bar(X_axis, dataframe['MB/s'],width, color='green',label='no acceleration')
    plt.bar(X_axis + width, dataframe2['MB/s'],width,color='blue', label='fastmath')
    plt.bar(X_axis + 2*width, dataframe3['MB/s'],width,color='orange', label='fasthugemath')
    axs.legend()
    plt.tight_layout()
    label = dataframe['Algorithm'].values
    axs.set_title('Performing encryption (block bytes 1048576, min 1.0 sec each) in MB/s for hash in wolfcrypt')
    plt.show()


plotBenchmark(df_simple,df_fast, df_fast_huge, df_sp, 'SHA-256')

