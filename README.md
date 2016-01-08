# amusement

amusement is a Python package and CLI (command-line interface) to get the current wait times and show times of attractions at many popular theme parks. We currently support:

* All Disney parks in USA, plus Paris
* All Universal parks worldwide (with the exception of Singapore)
* All Seaworld parks
* Hersheypark

## Example
### CLI
Get wait times right from your terminal
```
amusement islands-adventure --rides
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
| Universal Studios Florida     |x<sup>1</sup>|x<sup>1</sup>|
| Islands of Adventure          |x<sup>1</sup>|x<sup>1</sup>|
| Universal Studios Hollywood   |x<sup>2</sup>|x<sup>2</sup>|
| Universal Studios Japan       |x<sup>3</sup>|x<sup>3</sup>|
| Hersheypark                   |x            |             |
| Seaworld Orlando              |x            |x            |
| Seaworld San Diego            |x            |x            |
| Seaworld San Antonio          |x            |x            |
| Busch Gardens Williamsburg    |x            |x            |
| Busch Gardens Tampa           |x            |x            |

<sup>1</sup> USF/IOA currently only show a subset of attractions in the park. We are looking to address this in a future release.

<sup>2</sup> USH uses the official times based off of the USH website. Because this is a website that does not consistently present times in a predictable format, this may fail from time to time.

<sup>3</sup> If the park is closed, nothing will appear. We hope to address this in a future release.

## Contributors
I welcome any and all contributions! Please view CONTRIBUTING.md for more information.I'm more than happy to help first-timers and anybody else, so don't be shy and respond on the issues if you're interested in helping out.
 
## Tests
```
nosetests
```
Run this from the root directory to run tests.

## License
MIT
