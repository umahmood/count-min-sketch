# Count–min Sketch

A very basic implementation of a count-min sketch, good for understanding how the data structure works at the code level.

*the count–min sketch (CM sketch) is a probabilistic data structure that serves as a frequency table of events in a stream of data. It uses hash functions to map events to frequencies, but unlike a hash table uses only sub-linear space, at the expense of overcounting some events due to collisions.* - [Wikipedia](https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch)

# Installation

> git clone https://github.com/umahmood/count-min-sketch.git

# Usage

Python3:

> $ python3 count-min-sketch.py --file=player_names.txt --val="Lionel Messi"

# License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
