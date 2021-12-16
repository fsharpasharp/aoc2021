from functools import reduce
from typing import Tuple, Union

with open('input', 'r') as f:
    line = f.read().strip()

def parse_char_to_binary(char):
    binary = int(char, 16)
    return(f'{binary:04b}')

def parse_binary(string : str, n_chars : int) -> Tuple[int, str]:
    output, string = parse_string(string, n_chars)
    return int(output, 2), string

def parse_string(string : str, n_chars : int) -> Tuple[str, str]:
    return string[:n_chars], string[n_chars:]


class LiteralValue:
    def __init__(self, version):
        self.version = version
        self.val = 0

    def parse(self, string : str) -> str:
        binary = ""
        while True:
            flag, string = parse_binary(string, 1)
            extra, string = parse_string(string, 4)
            binary += extra

            if flag == 0:
                break
        self.val, _ = parse_binary(binary, len(binary))
        return string


    def value(self):
        return self.val

    def add_versions(self):
        return self.version

    def __str__(self):
        return f'LiteralValue with version:{self.version} value: {self.value}'

class OperatorPacket:
    def __init__(self, version, type_id, length_type):
        self.version = version
        self.length_type = length_type
        self.length = 0
        self.sub_packets = []

        if type_id == 0:
            self.reduction = sum
        elif type_id == 1:
            self.reduction = lambda xs: reduce(lambda x,y: x*y, xs, 1)
        elif type_id == 2:
            self.reduction = min
        elif type_id == 3:
            self.reduction = max
        elif type_id == 5:
            self.reduction = lambda xs: xs[0] > xs[1]
        elif type_id == 6:
            self.reduction = lambda xs: xs[0] < xs[1]
        elif type_id == 7:
            self.reduction = lambda xs: xs[0] == xs[1]

    def value(self) -> int:
        return self.reduction([x.value() for x in self.sub_packets])

    def parse(self, string : str) -> str:
        if not self.length_type:
            self.length, string = parse_binary(string, 15)
            i = 0
            while i < self.length:
                before = len(string)
                sh, string = parse_standard_header(string)
                after = len(string)
                self.sub_packets.append(sh)
                i += before - after
        else:
            self.length, string = parse_binary(string, 11)
            for _ in range(self.length):
                sh, string = parse_standard_header(string)
                self.sub_packets.append(sh)

        return string


    def add_versions(self):
        return self.version + sum([sh.add_versions() for sh in self.sub_packets])

    def __str__(self):
        string = f'Operator with version: {self.version}, length_type: {self.length_type}, length: {self.length}, has {len(self.sub_packets)} sub_packets\n'
        for sh in self.sub_packets:
            string += f'\t{sh}\n'
        return string


def parse_standard_header(string : str) -> tuple[Union[LiteralValue,OperatorPacket], str] :
    version, string = parse_binary(string, 3)
    type_id, string = parse_binary(string, 3)

    sh = None
    if type_id == 4:
        sh = LiteralValue(version)
        string = sh.parse(string)
    else:
        n, string = parse_binary(string, 1)
        sh = OperatorPacket(version, type_id, n)
        string = sh.parse(string)
        
        

    return sh, string

binary_repr = ""
for c in line:
    binary_repr += parse_char_to_binary(c)

sh, binary_repr = parse_standard_header(binary_repr)

print(sh.add_versions())
print(sh.value())
