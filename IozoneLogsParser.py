import sys
import json

formatOperation = ''
formatType = ''
Iozone = {}
IOFormats = {}

def setDictionary(fType, fOperation, Read=False, Write=False):
    if fType not in IOFormats.keys():
        IOFormats[fType] = {}
    if fOperation not in IOFormats[fType].keys():
        IOFormats[fType][fOperation] = {}
    if (Write):
        IOFormats[fType][fOperation]['Write'] = round(Write, 2)(Read):
    elif:
        IOFormats[fType][fOperation]['Read'] = round(Read, 2)
    Iozone[sys.argv[1]] = IOFormats

with open(sys.argv[1]) as f:
    for line in f:
        if "Command line used:" in line:
            #print(line.split("/"))
            formatType = line.split("/")[6] # Ext4, Vfat, f2fs etc
            formatOperation = line.split("/")[7].split(".")[0] # Rand buff, seq buff etc
            #print(formatOperation)

        if formatOperation == "rand_direct":
            if '"Random read report"' in line:
                f.next()
                rand_direct_read = float(f.next().split("  ")[1])/4
                #print(rand_direct_read)
                setDictionary(formatType, formatOperation, Read=rand_direct_read)

            if '"Random write report"' in line:
                f.next()
                rand_direct_write = float(f.next().split("  ")[1])/4
                #print(rand_direct_write)
                setDictionary(formatType, formatOperation, Write=rand_direct_write)

        if formatOperation == "seq_direct":
            if '"Reader report"' in line:
                f.next()
                seq_direct_read = float(f.next().split("  ")[1])/1024
                #print(seq_direct_read)
                setDictionary(formatType, formatOperation, Read=seq_direct_read)


            if'"Writer report"' in line:
                f.next()
                seq_direct_write = float(f.next().split("  ")[1])/1024
                #print(seq_direct_write)
                setDictionary(formatType, formatOperation, Write=seq_direct_write)


        if formatOperation == "rand_buffered":
            if '"Random read report"' in line:
                f.next()
                rand_buff_read = float(f.next().split("  ")[1])/4
                #print(rand_buff_read)
                setDictionary(formatType, formatOperation, Read=rand_buff_read)

            if '"Random write report"' in line:
                f.next()
                rand_buff_write = float(f.next().split("  ")[1])/4
                #print(rand_buff_write)
                setDictionary(formatType, formatOperation, Write=rand_buff_write)

        if formatOperation == "seq_buffered":
            if '"Reader report"' in line:
                f.next()
                seq_buff_read = float(f.next().split("  ")[1])/1024
                #print(seq_buff_read)
                setDictionary(formatType, formatOperation, Read=seq_buff_read)

            if '"Writer report"' in line:
                f.next()
                seq_buff_write = float(f.next().split("  ")[1])/1024
                #print(seq_buff_write)
                setDictionary(formatType, formatOperation, Write=seq_buff_write)

print(json.dumps(Iozone, indent=4, sort_keys=True))
