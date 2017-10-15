# USB shuffler
The script renames all MP3 files on a USB drive to `000.mp3`, `001.mp3`, and so on.
It stores the original file names in a file `pairs` in the root directory.

Used to make a random order of songs on a dumb FM transmitter.

## Usage
To rename all mp3 files
```
python shuffle.py %path_to_drive%
```
To restore the initial state
```
python unshuffle.py %path_to_drive%
```
