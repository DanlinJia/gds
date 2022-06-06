import matplotlib.pyplot as plt
import json
import pandas as pd

# with open('read.json', 'r') as fp:
#     r_json = json.load(fp)

write_df = pd.read_json('write.json', convert_axes=False)
read_df = pd.read_json('read.json', convert_axes=False)


# throughput/latency (Throughput/Avg_Latency)
# across read/write (IoType/XferType/Threads)

def plot_attri_across_workers(df, IoType, attri, title):
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

plot_attri_across_workers(write_df, " RANDWRITE" ,"Throughput", "RANDWRITE_Throughput")
plot_attri_across_workers(write_df, " WRITE" ,"Throughput", "WRITE_Throughput")
plot_attri_across_workers(read_df, " READ" ,"Throughput", "READ_Throughput")
plot_attri_across_workers(read_df, " RANDREAD" ,"Throughput", "RANDREAD_Throughput")