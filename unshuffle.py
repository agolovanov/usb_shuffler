import os
import sys
import pickle
usb_path = sys.argv[1]

pairs_file = os.path.join(usb_path, 'pairs')

with open(pairs_file, 'rb') as f:
    pairs = pickle.load(f)

for f, new_f in pairs:
    new_f_full = os.path.join(usb_path, new_f)
    parent = os.path.dirname(new_f_full)
    if not os.path.exists(parent):
        print(f'Creating {parent}')
        os.makedirs(parent)
    print(f'Renaming {f} to {new_f}')
    os.rename(os.path.join(usb_path, f), os.path.join(usb_path, new_f))

os.remove(pairs_file)