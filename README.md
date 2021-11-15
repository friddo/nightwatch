# Starstruck

A minimalist interpreter for [Starry](https://esolangs.org/wiki/starry) written in Python

```
        + + +* +  * + + +* + .*
 +         + +* * +      +* .
  + + . + . +        + +   +* +
 . +          +   * +* + .
         + +  * +* . +*      +
 * . + .* . . .  + * .
```

## Getting started

Download `starry.py` or clone the repo to your local disc.

Run the script with:
```
$ ./starry.py [filename]
```

Script will throw generic Python errors, if file contains invalid code


## Examples

Small examples to demonstrate

### Hello World

input:
```
        + + +* +  * + + +* + .*
 +         + +* * +      +* .
  + + . + . +        + +   +* +
 . +          +   * +* + .
         + +  * +* . +*      +
 * . + .* . . .  + * .
```
output:
```
Hello, World!
```

### Fibonacci

input:
```
     +      + ` +   +     * +
  .               + . '
```
output:
```
1
2
3
5
8
etc.
```

## Credits

Yutaka Hara for inventing Starry and providing reference sourcecode for the original [Ruby interpreter](https://github.com/yhara/esolang-book-sources/tree/master/starry)
