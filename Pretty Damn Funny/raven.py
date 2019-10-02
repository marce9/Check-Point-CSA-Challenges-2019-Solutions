import re
import zlib

pdf = open("raven.pdf", "rb").read()
stream = re.compile(r'stream(.*?)endstream', re.S)
f = open("output.txt", "a")

counter = 1
for s in stream.findall(pdf):
    s = s.strip('\r\n')
    try:
        f.write('obj: {}\n'.format(counter) + zlib.decompress(s) + '\n\n\n')
        counter+=1
        # print(zlib.decompress(s))
        # print("")
    except Exception as e:
        pass

f.close()