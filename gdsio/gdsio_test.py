from ctl_exp import cmd_output, ctl_cmd
import json
import multiprocessing as mp

io_strs = {0: "read", 1: "write", 2:"randread", 3:"randwrite"}

def gdsio_parser(output_str):
    """
    parse the output of gdsio.
    e.g., 
    "IoType: READ XferType: GPUD Threads: 16 DataSetSize: 103993344/104857600(KiB) 
    IOSize: 16384-32768-4096(KiB) Throughput: 6.168589 GiB/sec, Avg_Latency: 60200.233629 usecs 
    ops: 4236 total_time 16.077547 secs"
    """
    word_list = output_str.split(" ")
    json_output = {}
    i = 0
    while(i<len(word_list)):
        # the key is always followed by a colon
        if word_list[i][-1]==":" or word_list[i]=="total_time":
            key = word_list[i][:-1]
            json_output[key] = ""
        else:
            json_output[key] += " {}".format(word_list[i]) 
        i += 1
    return json_output

def gdsio_wrapper(gpu, mount_point, thread, xfer, io, return_list=[]):
    """
    execute gdsio command and save the output to return_list.
    """
    exp_name = "{}_xfer_{}_io_{}_w_{}".format(io_strs[io], xfer, io, thread)
    print("start {}".format(exp_name))
    cmd = "/usr/local/cuda/gds/tools/gdsio -f {} -d {} -w {} -s 100G -x {} -i 16M:32M:4M -I {}".format(mount_point, gpu, thread, xfer, io)
    cmd = cmd.split(" ")
    cmd_obj = ctl_cmd(cmd)
    cmd_obj.run_cmd()
    output = cmd_obj.output

    out_obj = cmd_output(gdsio_parser)
    out_obj.parse_output(output)

    json_obj = out_obj.json_output
    json_obj["name"] = exp_name
    json_obj["mount_point"] = mount_point
    return_list.append(json_obj)
    return return_list

def union_test(gpu, mount_point):
    w_list = [2]
    xfer_mod = [0]
    io_mod = [0, 1, 2, 3]
    return_list = []
    for io in io_mod:
        for xfer in xfer_mod:
            for thread in w_list:
                return_list.extend(gdsio_wrapper(gpu, mount_point, thread, xfer, io))

    with open('{}.json'.format(gpu), 'w') as fp:
        json.dump(return_list, fp)

def one_gpu_multiple_drive(gpu, files):
    w_list = [16]
    xfer_mod = [0, 4, 5]
    io_mod = [0, 1, 2, 3]
    ps_group = []
    manager = mp.Manager()
    return_list = manager.list()
    for io in io_mod:
        for xfer in xfer_mod:
            for thread in w_list:
                for mount_point in files:
                    ps = mp.Process(target=gdsio_wrapper, args=(gpu, mount_point, thread, xfer, io, return_list))
                    ps_group.append(ps)
                    ps.start()
                for ps in ps_group:
                    ps.join()

    with open('{}_{}drives.json'.format(gpu, len(files)), 'w') as fp:
        json.dump(list(return_list), fp)

    return list(return_list)

if __name__ == "__main__":
    # union_test(gpu=0, mount_point="/mnt/nvme7/test")

    files = [f"/mnt/nvme{i}/test" for i in [0, 1, 4, 5, 6, 7]]
    return_list = one_gpu_multiple_drive(gpu=0, files=files)