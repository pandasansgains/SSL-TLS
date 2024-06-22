import pandas as pd
from matplotlib import pyplot as plt


def mergeCols(df):
    df['Label'] = df['Cipher'].astype(str) +'_'+ df['Group'].astype(str) 


# Read CSV into pandas
data_12 = pd.read_csv(r"../data/TLS_ciph_bench/TLS_connection_benchmarks_1.2.csv")
data_13 = pd.read_csv(r"../data/TLS_ciph_bench/TLS_connection_benchmarks_1.3.csv")

mergeCols(data_12)
mergeCols(data_13)

df_12 = pd.DataFrame(data_12)
df_13 = pd.DataFrame(data_13)

df_12_cl = df_12[df_12['Side'] == 'Client']
df_12_srv = df_12[df_12['Side'] == 'Server']

df_13_cl = df_13[df_13['Side'] == 'Client']
df_13_srv = df_13[df_13['Side'] == 'Server']

df_12_cl.to_csv('../data/TLS_ciph_bench/df_12_cl.csv')
df_12_cl.to_csv('../data/TLS_ciph_bench/df_12_srv.csv')

df_13_cl.to_csv('../data/TLS_ciph_bench/df_13_cl.csv')
df_13_cl.to_csv('../data/TLS_ciph_bench/df_13_srv.csv')


import pandas as pd
from matplotlib import pyplot as plt


def mergeCols(df):
    df['Label'] = df['Cipher'].astype(str) +'_'+ df['Group'].astype(str) 


# Read CSV into pandas
data_12 = pd.read_csv(r"../data/TLS_ciph_bench/TLS_connection_benchmarks_1.2.csv")
data_13 = pd.read_csv(r"../data/TLS_ciph_bench/TLS_connection_benchmarks_1.3.csv")

mergeCols(data_12)
mergeCols(data_13)

df_12 = pd.DataFrame(data_12)
df_13 = pd.DataFrame(data_13)

df_12_cl = df_12[df_12['Side'] == 'Client']
df_12_srv = df_12[df_12['Side'] == 'Server']

df_13_cl = df_13[df_13['Side'] == 'Client']
df_13_srv = df_13[df_13['Side'] == 'Server']

df_12_cl.to_csv('../data/TLS_ciph_bench/df_12_cl.csv')
df_12_cl.to_csv('../data/TLS_ciph_bench/df_12_srv.csv')

df_13_cl.to_csv('../data/TLS_ciph_bench/df_13_cl.csv')
df_13_cl.to_csv('../data/TLS_ciph_bench/df_13_srv.csv')

