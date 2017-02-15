
# textplayer

This code provides a Python interface for running text-based games using Frotz.

## Requirements

The only requirement is Frotz, a Z-Machine interpreter written by Stefan Jokisch in 1995-1997. More information [here](http://frotz.sourceforge.net/).

Download this source code, then perform the following commands in the textplayer folder.

```bash
$ git clone https://github.com/DavidGriffith/frotz.git
$ cd frotz
$ make dumb
```

TextPlayer.py can now be used.

## Usage

Example commands are below.

```python
import textplayer.textplayer as tp
t = tp.TextPlayer('zork1.z5')
start_info = t.run()
command_output = t.execute_command('go north')
if t.get_score() != None:
    score, possible_score = t.get_score()
t.quit()
```

To run games interactively in the terminal, run the bash command below in the textplayer folder.

```bash
$ frotz/dfrotz games/zork1.z5
```

## Games

Games are provided in this repo, but more games are available [here](http://www.ifarchive.org/indexes/if-archiveXgamesXzcode.html).

## Miscellaneous

If you are the copyright holder for any of these game files and object to their distribution in this repository, e-mail the owner at daniel.ricks4 (-a-t-) gmail.com.
