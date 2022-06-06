from ctl_exp import cmd_output, ctl_cmd
import json

io_strs = {0: "read", 1: "write", 2:"randread", 3:"randwrite"}

def gdsio_parser(output_str):
    """
    parse the output of gdsio
    e.g., ""
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

def gosio_wrapper(gpu, mount_point, io_mod, xfer_mod, w_list):
    """
    execute gdsio command and save the output to json
    io_mod, xfer_mod, w_list specify the combination of gdsio's 
    parameters.
    """
    ret_list = []
    for io in io_mod:
        for xfer in xfer_mod:
            for w in w_list:
                exp_name = "{}_xfer_{}_io_{}_w_{}".format(io_strs[io], xfer, io, w)
                print("start {}".format(exp_name))
                cmd = "./gdsio -f {} -d {} -w {} -s 100G -x {} -i 16M:32M:4M -I {}".format(mount_point, gpu, w, xfer, io)
                cmd = cmd.split(" ")
                cmd_obj = ctl_cmd(cmd)
                cmd_obj.run_cmd()
                output = cmd_obj.output

                out_obj = cmd_output(gdsio_parser)
                out_obj.parse_output(output)

                json_obj = out_obj.json_output
                json_obj["name"] = exp_name
                ret_list.append(json_obj)
    return ret_list

def read_test(gpu, mount_point="/mnt/gds_test_mnt/test"):
    w_list = [2, 4, 6, 8, 16, 32, 64, 128]
    xfer_mod = [0, 1, 2, 3, 4, 5]
    io_mod = [0, 2]
    ret_list = gosio_wrapper(gpu, mount_point, io_mod, xfer_mod, w_list)

    with open('read.json', 'w') as fp:
        json.dump(ret_list, fp)

def write_test(gpu, mount_point="/mnt/gds_test_mnt/test"):
    w_list = [2, 4, 6, 8, 16, 32, 64, 128]
    xfer_mod = [0, 1, 2, 3, 4, 5]
    io_mod = [1, 3]
    ret_list = gosio_wrapper(gpu, mount_point, io_mod, xfer_mod, w_list)

    with open('write.json', 'w') as fp:
        json.dump(ret_list, fp)

def union_test(gpu, mount_point="/mnt/gds_test_mnt/test"):
    w_list = [2, 4, 6, 8, 16, 32, 64, 128]
    xfer_mod = [0, 1, 2, 3, 4, 5]
    io_mod = [0, 1, 2, 3]
    ret_list = gosio_wrapper(gpu, mount_point, io_mod, xfer_mod, w_list)

    with open('{}.json'.format(gpu), 'w') as fp:
        json.dump(ret_list, fp)

def one_gpu_multiple_drive(gpu, )

if __name__ == "__main__":
    # read_test(gpu=0)
    # write_test(gpu=0)
    union_test(gpu=0)