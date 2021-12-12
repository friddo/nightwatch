#!/usr/bin/env python3
import sys
class starry():
    def run(parsed):
        p,s,pc = parsed, [], 0
        while pc < len(p):
            i,a = p[pc] #separate parsed commands into op-code and arguments
            if not isinstance(a, int) and a is not None: raise ValueError(f'lol') #if argument is not empty or an int
            if   i == "push": s.append(a) #append argument to stack
            elif i == "dup" : s.append(s[-1]) #duplicate top element of stack
            elif i == "swap": s[-2:] = reversed(s[-2:]) #swap 2 last elements of array
            elif i == "rot" : s[-3:] = s[-1:]+s[-3:-1] #rotate last 3 elements of array (1,2,3,4) -> (1,4,2,3)
            elif i == "pop" : s.pop() #pop an element from stack
            elif i == "+"   : s[-2:] = [sum(s[-2:])] #merge 2 last elements with addition
            elif i == "-"   : s[-2:] = [s[-2]-s[-1]] #merge 2 last elements with subtraction
            elif i == "*"   : s[-2:] = [s[-2]*s[-1]] #merge 2 last elements with multiplication
            elif i == "/"   : s[-2:] = [s[-2]//s[-1]] #merge 2 last elements with division
            elif i == "%"   : s[-2:] = [s[-2]%s[-1]] #merge 2 last elements with modulus
            elif i == "in"  : s.append(int(input()) if a % 2 == 0 else ord(input())) #read input and convert to ASCII if needed
            elif i == "out" : print(int(s.pop()) if a % 2 == 0 else chr(s.pop()),end="") #write to output and convert to ASCII if needed
            elif i == "jump": pc = p.index(('label',a)) if s.pop() else pc #pop and jump if not 0
            else: raise ValueError(f'Unknown parsed operator: {i}, with arguments {a}')
            pc += 1
        print("\n\nExecution finished.")
    def parse(src):
        OP_STACK, OP_CALC = ["nop","dup","swap","rot","pop"], "+-*/%" #index for stack operations, and math operations
        i, spaces = [], 0
        for c in src:
            if c in "+*.,`'": #valid code chars
                if c == "+": i.append((OP_STACK[spaces % 5],None) if spaces < 5 else ("push",spaces - 5))
                if c == "*": i.append((OP_CALC[spaces % 5],None))
                if c == ".": i.append(("out",spaces))
                if c == ",": i.append(("in",spaces))
                if c == "`": i.append(("label",spaces))
                if c == "'": i.append(("jump",spaces))
                spaces = 0
            elif c == " ":
                spaces += 1
        return i
        
def main():
  if len(sys.argv) == 2:
      with open(sys.argv[1]) as file:
          parsed = starry.parse(file.read())
          #for c in parsed: print(c)
          starry.run(parsed)
  else:
      print(f'Usage: {sys.argv[0]} filename')
if __name__ == "__main__": main()