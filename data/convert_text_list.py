import os
import sys

from tqdm import tqdm

with open('char_std_5990.txt',encoding='utf-8') as fd:
    cvt_lines = fd.readlines()

cvt_dict = {}
for i, line in enumerate(cvt_lines):
    key = i
    value = line.strip()
    cvt_dict[key] = value

if __name__ == "__main__":
   cvt_fpath = sys.argv[1]
   dst_fpath = sys.argv[2]

   with open(cvt_fpath,encoding='utf-8') as fd:
       lines = fd.readlines()

   with open(dst_fpath, 'w',encoding='utf-8') as fd:
       for line in tqdm(lines):
           line_split = line.strip().split()
           img_path = line_split[0]
           label = ''
           for i in line_split[1:]:
               label += cvt_dict[int(i)]
           fd.write(img_path, ' ', label)
