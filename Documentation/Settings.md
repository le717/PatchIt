# PatchIt! Settings #

## Details ##
* The PatchIt! settings contains all the required information to install a Patch into the proper location.
* Settings are stored as string [JSON](http://www.json.org/) key-value pairs using a [`UTF-8-NOBOM`](http://en.wikipedia.org/wiki/UTF-8#Byte_order_mark) encoding.
* The `Settings` direction, in which the settings are saved, is located in the same directory as the PatchIt! executable.

### `Racers.json` ###
* The `firstRun` key contains the current state of settings configuration. In a new or cleans installation of PatchIt!,
the value is `"0"` (zero), indicating required settings have not been configured. After configuration, the value is updated to `"1"`,
indicating all is configured and no further action from the user is needed.
* The `installPath` key contains the installation path to the user's copy of LEGO&reg; Racers.
* The `releaseVersion` key contains user's release version of LEGO Racers. There are only two possible values: `1999` and `2001`.

### `PatchIt.json` ###
* The `minVer` key states the type of PatchIt! build in use. Possible values are `Unstable`, `RC1`, `RC2`, and `Stable`.
* The `version` key lists the PatchIt! major, minor, and patch versions in use.
* The `buildNum` key contains the build number of that release of PatchIt!.

## Examples ##
Due to the nature of Python dictionaries (how the data is internally stored before being written to disk),
the exact order of these examples may differ from your copy.

### General PatchIt! Settings ###
* File name: _**PatchIt.json**_

```json
{
    "version": "1.1.2",
    "minVer": "Unstable",
    "buildNum": "217"
}
```

### LEGO Racers Settings ###
* File name: _**Racers.json**_

```json
{
    "firstRun": "1",
    "installPath": "C:/Program Files (x86)/LEGO Media/Games/LEGO Racers",
    "releaseVersion": "2001"
}
```
