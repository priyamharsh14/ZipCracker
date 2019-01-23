# ZipCracker

## Installation:

```
$ git clone https://github.com/priyamharsh14/ZipCracker.git
```

## Usage:

In terminal type -
```
$ python zipcracker.py --help
__________.__         _________                       __
\____    /|__|_____   \_   ___ \____________    ____ |  | __ ___________
  /     / |  \____ \  /    \  \/\_  __ \__  \ _/ ___\|  |/ // __ \_  __ \
 /     /_ |  |  |_> > \     \____|  | \// __ \  \___|    <\  ___/|  | \/
/_______ \|__|   __/   \______  /|__|  (____  /\___  >__|_ \___  >__|
        \/   |__|             \/            \/     \/     \/    \/


Author: Priyam Harsh

Usage: zipcracker.py [options] filename

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -l LENGTH, --length=LENGTH
                        Max. length of the password
```

In order to crack an encrypted zip file -
```
$ python zipcarcker.py --length=<max. length of password> <filename>
```
