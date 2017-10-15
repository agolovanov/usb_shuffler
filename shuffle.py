import os
import sys
import random
import pickle
usb_path = sys.argv[1]

mp3_list = []

for dirname, _, filelist in os.walk(usb_path):
    for f in filelist:
        if f.endswith('.mp3'):
            mp3_list.append(os.path.join(dirname, f))

random.shuffle(mp3_list)

pairs = []

for i, f in enumerate(mp3_list):
    new_f = os.path.join(usb_path, '%03d.mp3' % i)
    new_f_rel = os.path.relpath(new_f, usb_path)
    f_rel = os.path.relpath(f, usb_path)
    pairs.append((new_f_rel, f_rel))
    print(f'Renaming {f_rel} to {new_f_rel}')
    os.rename(f, new_f)

with open(os.path.join(usb_path, 'pairs'), 'wb') as f:
    pickle.dump(pairs, f)