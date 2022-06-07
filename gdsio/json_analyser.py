import matplotlib.pyplot as plt
import json
import pandas as pd
import numpy as np

# with open('read.json', 'r') as fp:
#     r_json = json.load(fp)

# write_df = pd.read_json('write.json', convert_axes=False)
# read_df = pd.read_json('read.json', convert_axes=False)


# throughput/latency (Throughput/Avg_Latency)
# across read/write (IoType/XferType/Threads)

def plot_attri(df, IoType, attri, title):
    # sequential_df = df[(df.IoType==" READ")|(df.IoType==" WRITE")]
    io_df = df[df.IoType==IoType]
    Xfertype = df.XferType.drop_duplicates().values
    fig, ax = plt.subplots()
    for xfer in Xfertype:
        xfer_df = io_df[io_df.XferType==xfer]
        x = xfer_df.Threads.astype(str)
        y = xfer_df[attri].apply(lambda x: x.split(" ")[1]).astype(float)
        unit = xfer_df[attri].iloc[0].split(" ")[-1]
        ax.plot(x, y, label=xfer,  marker=".")#, marker=".", color="g", linestyle='dashed')
        ax.set_xlabel("Thread")
        ax.set_ylabel("{} {}".format(attri, unit))
        ax.set_title(title)
    plt.legend()
    plt.savefig("{}.png".format(title))

def plot_attri(df, IoType, attri, x_label, title):
    # sequential_df = df[(df.IoType==" READ")|(df.IoType==" WRITE")]
    io_df = df[df.IoType==IoType]
    Xfertype = df.XferType.drop_duplicates().values
    fig, ax = plt.subplots()
    for xfer in Xfertype:
        xfer_df = io_df[io_df.XferType==xfer]
        x = xfer_df[x_label].astype(str)
        y = xfer_df[attri].apply(lambda x: x.split(" ")[1]).astype(float)
        unit = xfer_df[attri].iloc[0].split(" ")[-1]
        ax.plot(x, y, label=xfer,  marker=".")#, marker=".", color="g", linestyle='dashed')
        ax.set_xlabel(x_label)
        ax.set_ylabel("{} {}".format(attri, unit))
        ax.set_title(title)
    plt.grid()
    plt.legend()
    plt.savefig("{}.png".format(title))

def plot_throughput_across_drives():
    json_dfs =[]
    for i in [1, 2, 4, 6]:
        json_df = pd.read_json(f'0_{i}drives.json', convert_axes=False)
        json_df["tpt"] = json_df.Throughput.apply(lambda x:x.split()[0]).astype(float)
        drive_df = json_df.groupby(by=["XferType", "IoType", "Threads"], as_index=False).sum()
        drive_df["Throughput"] = drive_df["tpt"].apply(lambda x: f" {x} GiB/s")
        drive_df["drivers"] = np.array([i]*len(drive_df))
        json_dfs.append(drive_df)

    json_df = pd.concat(json_dfs)
    plot_attri(json_df, " RANDWRITE" ,"Throughput", 'drivers' , "RANDWRITE_Throughput")
    plot_attri(json_df, " WRITE" ,"Throughput", 'drivers' ,"WRITE_Throughput")
    plot_attri(json_df, " READ" ,"Throughput", 'drivers' ,"READ_Throughput")
    plot_attri(json_df, " RANDREAD" ,"Throughput", 'drivers' ,"RANDREAD_Throughput")

# json_df = pd.read_json(f'0_{1}drives.json', convert_axes=False)

# plot_attri(json_df, " RANDWRITE" ,"Throughput", 'Threads' , "RANDWRITE_Throughput")
# plot_attri(json_df, " WRITE" ,"Throughput", 'Threads' ,"WRITE_Throughput")
# plot_attri(json_df, " READ" ,"Throughput", 'Threads' ,"READ_Throughput")
# plot_attri(json_df, " RANDREAD" ,"Throughput", 'Threads' ,"RANDREAD_Throughput")