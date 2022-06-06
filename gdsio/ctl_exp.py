import subprocess

from yaml import parse

class ctl_cmd():
    """
    execute an ctl cmd (Linux) and save the output string.
    """
    def __init__(self, cmd) -> None:
        self.cmd = cmd
        self.output = ""

    def set_cmd(self, cmd: str):
        self.cmd = cmd

    def run_cmd(self):
        result = subprocess.check_output(self.cmd)
        self.output = result.decode('utf-8')

class cmd_output():
    """
    Parse the output string of a ctl cmd as defined in parser.
    Return a json object.
    """
    def __init__(self, parser) -> None:
        self.parser = parser
        self.json_output = None

    def parse_output(self, output: str):
        self.json_output = self.parser(output)

def gdsio_parser(output_str):
    word_list = output_str.split(" ")
    json_output = {}
    i = 0
    while(i<len(word_list)):
        if word_list[i][-1]==":" or word_list[i]=="total_time":
            key = word_list[i][:-1]
            json_output[key] = ""
        else:
            json_output[key] += " {}".format(word_list[i]) 
        i += 1
    return json_output

if __name__=="__main__":
    cmd = "./gdsio -f /mnt/gds_test_mnt/test -d 7 -w 64 -s 10G -x 0 -i 16M:32M:1M -I 1"
    cmd = cmd.split(" ")
    cmd_obj = ctl_cmd(cmd)
    cmd_obj.run_cmd()
    output = cmd_obj.output

    out_obj = cmd_output(gdsio_parser)
    out_obj.parse_output(output)

    json_obj = out_obj.json_output
