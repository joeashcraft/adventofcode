## Lessons Learned

1.  logzero.logger could use a handy feature to indent STDOUT based on loop level. That'd be handy.
2.  do not modify an iterable while you're iterating thru it! see "list.copy()"
3.  logic bug: my initial solution missed the idea that several steps could be ready with no requirements, and I'd have to alpha-sort to find the right next step. This is clear in the problem, but I did not implement it well.
