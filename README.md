
# text-player

This code provides an interface for running text-based games using Frotz.

Keep in mind that if there is more than one instance of Frotz running, everything will break.

## Requirements

The only requirement aside from this source code is Frotz, a z-machine interpreter written by Stefan Jokisch in 1995-1997. More information [here](http://frotz.sourceforge.net/).

'''bash
$ sudo apt-get install frotz
'''

## Usage

This code is set up to run both from the terminal or in python. Running the following bash command from the terminal will run the commands contained in command.txt.

'''bash
$ python TextPlayer -g zork1.z5
'''

The python code is demonstrated in mass_run.py.

## Games

Games are provided in this repo, but more games are available [here](http://www.ifarchive.org/indexes/if-archiveXgamesXzcode.html).

