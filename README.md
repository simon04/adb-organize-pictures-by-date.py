Uses` adb` (Android Debug Bridge) to organize pictures into folders YYYY-MM based on their file modification date.

## Usage
* Edit the paths in `adb-organize-pictures-by-date.py`
* `./adb-organize-pictures-by-date.py` generates the `adb shell mv` commands to be executed, thus `./adb-organize-pictures-by-date.py | sh` executes the commands
