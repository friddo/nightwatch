# Nightwatch ✨

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

### Whitespace 

* **Since Starry programs utilize whitespace for instruction parsing, extra caution is needed when copying or modifying code.**


## Examples

Small examples to demonstrate

#### Hello World
Codegolf-ed solution to the `Hello, World!` problem.

file:
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

#### A000252 Sequence
Calculates the n-th term of the [OEIS A000252](https://oeis.org/A000252) sequence.
Made by user "Not a tree" on the [codegolf stackexchange forum](https://codegolf.stackexchange.com/a/135269) 

file:
```
, +      + *     '.     `
 + + + +  *  *  *  +     
 +`      +*       +    ` 
 + +   +  + +   + *  '   
   +   '  ####`  + +   + 
 + +    ####  +*   +    *
    '  #####  +      + ' 
  `    ######+  + +   +  
+ +   + #########   * '  
 +   +  + #####+ +      +
*  +      + * +  *  *   +
   +  *  + + + +  *  *   
+   +  +   *   + `  + +  
 +  + +   + *'    +    +.
```
input:
```
50
```
output:
```
1800000
```

#### Fibonacci
Outputs the Fibonnaci sequence.

file:
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

#### Factorial
Computes the factorial of n

file:
```
, + `      + * +   +
  *  + +      + * '  +.
```
input:
```
6
```
output:
```
720
```

## Credits

Thanks to Yutaka Hara for inventing Starry and providing reference sourcecode for the original [Ruby implementation](https://github.com/yhara/esolang-book-sources/tree/master/starry)
