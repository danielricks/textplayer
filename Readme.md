
# textplayer

This code provides an interface for running text-based games using Frotz.

## Requirements

The only requirement is Frotz, a Z-Machine interpreter written by Stefan Jokisch in 1995-1997. More information [here](http://frotz.sourceforge.net/).

Download this source code, then perform the following commands in the text-player folder.

```bash
$ git clone https://github.com/DavidGriffith/frotz.git
$ cd frotz
$ make dumb
```

TextPlayer.py can now be used.

## Usage

This code is set up to run in python. Example commands are below.

```python
t = TextPlayer('zork1.z5', False)
start_info = t.run()
command_output = t.execute_command('go north')
if t.get_score() != None:
    score, possible_score = t.get_score()
t.quit()
```

## Games

Games are provided in this repo, but more games are available [here](http://www.ifarchive.org/indexes/if-archiveXgamesXzcode.html).

## Miscellaneous

If you are the copyright holder for any of these game files and object to their distribution in this repository, e-mail the owner at daniel.ricks4 (-a-t-) gmail.com.
