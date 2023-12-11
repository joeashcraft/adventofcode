## process the named coordinates
named_coords=list()  # e.g. [ {loc: (1, 2), count_nearest: 42}, {}... ]
""" INDEX: arbitrary "name" of coord
    VALUE: dictionary with two items: the location as tuple([x,y]), count of nearest coords as integer """
named[n]={ loc: tuple([x, y]), count_nearest: int(0) }

determine grid size:
  min(x), min(y)
  max(x), max(y)

## populate the grid with all points
coords=dict()  # e.g. { (x,y): "A" }
""" KEY: tuple that represents x,y coordinates
    VALUE: string that is the nearest named coord"""
coords[tuple([x, y])] = str('x')


## shortcut
ignore the 4 corners which are Named coords
### determine which named coords have infinite areas
if x is min_x,
or if y is min_y,
or if x is max(x),
or if y is max(y):
  then nearest named coord has an infinite area (let count_nearest=-1 maybe)

## brute force
for every x,y coord in grid,
  for each named_coord not ignored:
  compute distance to all named coords.
  if nearest is 0, then this is a NAMED COORD: move along
  if the two nearest named coords are at same distance, then it's a tie: record nearest named coord as None
  ^^^ stuck trying to detect ties for nearest
  otherwise,
    record the nearest named coords, and
    increment named.x.count_nearest.


## of named coords, return greatest "count_nearest"
max([named_coords.ii.count_nearest for ii in named_coords])
