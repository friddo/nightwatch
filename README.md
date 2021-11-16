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

### Running code

Run the script with:
```
$ ./starry.py [filename]
```

Script will throw generic Python errors, if file contains invalid code.

### Compiler

A future compiler will allow for compilation of a custom assembly code format, to .sta files

#### About whitespace 
Since Starry programs utilize whitespace for instruction parsing, extra caution is needed when copying or modifying code.  
Ensure that your editor doesnt erase trailing spaces.

## Examples

Small examples to demonstrate

#### Hello World
Codegolf-ed solution to the `Hello, World!` problem made by [Sp3000](https://codegolf.stackexchange.com/a/55526)

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
Made by [Not a tree](https://codegolf.stackexchange.com/a/135269) 

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
## To Do

* Command line arguments
  * verbose
  * delay
  * initial stack setup
* Support for an interactive debugger
  * program view, stack view
## Credits

Thanks to Yutaka Hara for inventing Starry and providing reference sourcecode for the original [Ruby implementation](https://github.com/yhara/esolang-book-sources/tree/master/starry)
