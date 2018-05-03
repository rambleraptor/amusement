# amusement

amusement is a Python package and CLI (command-line interface) to get the current wait times and show times of attractions at many popular theme parks. These are the official times straight from the official mobile apps of the respective parks. No unreliable crowdsouring required! We currently support:

* All Disney parks in USA
* All Universal parks worldwide (with the exception of Singapore)
* Hersheypark

## Example
### CLI
Get wait times right from your terminal
```
amusement islands-adventure --type rides
```

### Library
```
from amusement.parks.universal.IslandsOfAdventure import IslandsOfAdventure

ioa = IslandsOfAdventure()
print ioa.rides()
# or print ioa.shows() if you want show times instead
```
A full list of the rides and shows in the park will be displayed!

## Getting Started
```
pip install amusement
```
That's it!

## Parks
amusement supports a lot of parks. Here's a breakdown of which parks are supported and which features have been implemented.

| Park Name                     | Rides       | Shows       |
| ------------------------------|-------------|-------------|
| Magic Kingdom                 |x            |             |
| Epcot                         |x            |             |
| Hollywood Studios             |x            |             |
| Animal Kingdom                |x            |             |
| Disneyland                    |x            |             |
| Disney's California Adventure |x            |             |
| Universal Studios Florida     |x            |x            |
| Islands of Adventure          |x            |x            |
| Universal Studios Hollywood   |x            |x            |
| Universal Studios Japan       |x<sup>1</sup>|x<sup>1</sup>|
| Hersheypark                   |x            |             |

<sup>1</sup> If the park is closed, nothing will appear. We hope to address this in a future release.

## Contributors
I welcome any and all contributions! Please view CONTRIBUTING.md for more information.I'm more than happy to help first-timers and anybody else, so don't be shy and respond on the issues if you're interested in helping out.
 
## Tests
```
python -m unittest discover test/
```
Run this from the root directory to run tests.

## License
MIT
