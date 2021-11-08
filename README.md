# DIY Busylight

## Modules
* Light module
* Button module
* Screen module

## Serial communication commands
To talk to the different modules, serial commands are sent from a host device (this can also be another module) to a module that executes the command and reply back.

### Light module
The light module accepts the following commands,
| Command | Name | Description | Argument(s) | Reply | Example |
| ----------- | ----------- |  ----------- | ----------- | ----------- | ----------- |
| `s` | set | Sets the rgb light to a specific color | hex | **On success:** Returns the color that you sent <br> **On failure:**  | `s 0x44a832` |
| `b` | brightness | Sets the brightness level | float | **On success:** Returns the brightness that you sent <br> **On failure:**  | `b 0.4` |
| `i` | info | Get info about the light module device | | **On success:** Returns json object with device and version information<br> **On failure:** | `i` |
| `p` | ping | Send a ping to check if the light module is active | | **On success:** Pong <br> **On failure:** | `p` |

## Repository structure
* `com`
  * Folder with serial communication helpers to communicate with the modules 
* `gui`
  * Graphical interface to control the modules
