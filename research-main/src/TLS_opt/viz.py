
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
 
# Read CSV into pandas
df_13_throughput = pd.read_csv(r"../data/TLS_opt/TLS_13/throughput.csv")
df_13_psk_throughput = pd.read_csv(r"../data/TLS_opt/TLS_13_PSK/throughput.csv")
df_13_res_throughput = pd.read_csv(r"../data/TLS_opt/TLS_13_RES/throughput.csv")
df_dtls_13_throughput = pd.read_csv(r"../data/DTLS_opt/DTLS/throughput.csv")


df_13_conn_average = pd.read_csv(r"../data/TLS_opt/TLS_13/conn_average.csv")
df_13_psk_conn_average = pd.read_csv(r"../data/TLS_opt/TLS_13_PSK/conn_average.csv")
df_13_res_conn_average = pd.read_csv(r"../data/TLS_opt/TLS_13_RES/conn_average.csv")
df_dtls_13_conn_average = pd.read_csv(r"../data/DTLS_opt/DTLS/conn_average.csv")

cmap = plt.get_cmap('viridis')  # You can choose any colormap you like


def plotThroughput(df_tls_13, df_tls_psk_13,df_tls_res_13, df_dtls_13):
    #does it make sense to do since it is one connection and then only echange of data
    fig, axs = plt.subplots(figsize=(12, 12),nrows=2, ncols=2)
    frame = plt.gca()

    plot_1 = axs[0,0]
    plot_1.set_ylabel('Mb/s')
    plot_1.set_title('RX Buffer server')

    plotOneThroughput(df_tls_13,'green','TLS_13 Throughput ','server','RX MBps', plot_1)
    plotOneThroughput(df_tls_psk_13,'blue','TLS_13_PSK Throughput ','server','RX MBps', plot_1)
    plotOneThroughput(df_tls_res_13,'orange','TLS_13_RES Throughput ','server','RX MBps', plot_1)
    plotOneThroughput(df_dtls_13,'red','DTLS_13 Throughput ','server','RX MBps', plot_1)

    plot_1.legend()


    plot_2 = axs[0,1]
    plot_2.set_ylabel('Mb/s')
    plot_2.set_title('TX Buffer server')
    plotOneThroughput(df_tls_13,'green','TLS_13 Throughput ','server','TX MBps', plot_2)
    plotOneThroughput(df_tls_psk_13,'blue','TLS_13_PSK Throughput ','server','TX MBps', plot_2)
    plotOneThroughput(df_tls_res_13,'orange','TLS_13_res throughput ','server','TX MBps', plot_2)
    plotOneThroughput(df_dtls_13,'red','DTLS_13 throughput ','server','TX MBps', plot_2)
    plot_2.legend()


    plot_3 = axs[1,1]
    plot_3.set_ylabel('Mb/s')
    plot_3.set_xlabel('Number of bytes transmitted')
    plot_3.set_title('TX Buffer client')
    plotOneThroughput(df_tls_13,'green','TLS_13 Throughput ','client','TX MBps', plot_3)
    plotOneThroughput(df_tls_psk_13,'blue','TLS_13_PSK Throughput ','client','TX MBps', plot_3)
    plotOneThroughput(df_tls_res_13,'orange','TLS_13_RES Throughput ','client','TX MBps', plot_3)
    plotOneThroughput(df_dtls_13,'red','DTLS_13 Throughput ','client','TX MBps', plot_3)
    plot_3.legend()

    plot_4 = axs[1,0]
    plot_4.set_ylabel('Mb/s')
    plot_4.set_xlabel('Number of bytes transmitted')
    plot_4.set_title('RX Buffer client')
    plotOneThroughput(df_tls_13,'green','TLS_13 Throughput ','client','RX MBps', plot_4)
    plotOneThroughput(df_tls_psk_13,'blue','TLS_13_PSK Throughput ','client','RX MBps', plot_4)
    plotOneThroughput(df_tls_res_13,'orange','TLS_13_RES Throughput ','client','RX MBps', plot_4)
    plotOneThroughput(df_dtls_13,'red','DTLS_13 Throughput ','client','RX MBps', plot_4)
    plot_4.legend()

    plt.tight_layout()
    plt.show()

def plotConnAverage(df_tls_13, df_tls_psk_13, df_tls_res_13,df_dtls_13):
    fig, axs = plt.subplots(figsize=(12, 12))
    axs.set_ylabel('Mb/s')
    axs.set_xlabel('Amount of connections')
    axs.set_title('Average connection time over 10, 100, 250, 500, 1000 subsequent connections')
    frame = plt.gca()
    plotOneConnAverage(df_tls_13,'green','TLS_13')
    plotOneConnAverage(df_tls_psk_13,'blue','TLS_13_PSK')
    plotOneConnAverageRes(df_tls_res_13,'orange','TLS_13_RES')
    plotOneConnAverage(df_dtls_13,'red','DTLS_13')
    axs.legend()
    plt.tight_layout()
    plt.show()

def plotOneConnAverage(df, color, label):
    plt.plot(df['num_conn'],df['time_ms'],marker='o', color=color,label=label)

def plotOneThroughput(df, color, label, kind, RX_TX, canvas):
    df_target = df.loc[df['Kind'] == kind]
    canvas.plot(df_target['bytes'],df_target[RX_TX],marker='o', color=color,label=label + RX_TX)

def plotOneConnAverageRes(df, color, label):
    plt.plot(df['num_conn'],df['resume_time_ms'],marker='o', color=color,label='TLS 13 Resume time')

# plotConnAverage(df_13_conn_average,df_13_psk_conn_average,df_13_res_conn_average,df_dtls_13_conn_average)
plotThroughput(df_13_throughput, df_13_psk_throughput,df_13_res_throughput, df_dtls_13_throughput)