# nyc-districtr-helper

To prevent super-dense tiles, this hosts all columns other than Total Population
in memory on a server.

Atomic changes are sent and returned with the delta in each column value for each
edited district.

TODO

- resolve which columns - might need to calculate one
- client-side
- undo/redo
- handling errors in a transaction (repeat server req or undo?)
- new layer for % subgroups visualization (bg or tract?)
