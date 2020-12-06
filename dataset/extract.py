import re

infile = open('putty1.log', 'r')
outfile = open('putty5(coded).csv', 'w')

for line in infile:
    if 'changed, new' in line:
        searchObj = re.search(r'\[(\d{2}:\d{2}:\d{2}\.\d{3}),\d{3}\] <info> app: RSSI changed, new: (-?\d+), channel: (\d+)', line)
        data = [searchObj.group(1), searchObj.group(2), searchObj.group(3)]
        outfile.write(','.join(data)+'\n')

infile.close()
outfile.close()