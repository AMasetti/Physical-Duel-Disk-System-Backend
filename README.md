# Duel Disk System

This repo serves as an add on to run alongside BramDC3's `smart-duel-server` to feed the `smart-duel-gazer` with data from user action in a physical duel disk. For that the use should have a physical duel disk that can use the Duel Disk Protocol to connect to this program.

Unfortunately Docker does not allow the local machine's COM ports to be exposed to the container so this has to be run locally.

In order to get things running we'll first create a virtual environment for our code to run and install the required dependencies all from the following code.

```bash
pyenv virtualenv 3.7.2 duel-disk-serial-add-on
pyenv activate duel-disk-serial-add-on
pyenv local duel-disk-serial-add-on
pip3 install -r requirements.txt
```

Then go to the [`constants.py`](http://constants.py) file and modify the serial port to which your duel disk connects and the port on which the `smart-duel-server` runs (which should be 52300 by default, don't need to modify that if you didn't change the port on the server)

```python
# Part of the constants.py file
DUEL_DISK_COMM_PORT = 'COM10'
SMART_DUEL_SERVER_PORT = 52300
BACK = 'b'
NEXT_PHASE = 'n'

SUMMON_DATA = {
    'yugiohCardId': '',
    'zoneName': '',
}

MONSTER_ZONES_STR = ['mainMonster1', 'mainMonster2', 'mainMonster3']
```

For running the Add-on first launch the `smart-duel-server` container and then launch the add on from the command line as such:

```python
python3 main.py
```
