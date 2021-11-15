#!/usr/bin/env python3
import sys
class starry():
    def run(parsed):
        p,s,pc = parsed, [], 0
        while pc < len(p):
            i,a = p[pc]
            if i == "push": s.append(a)
            if i == "dup" : s.append(s[-1])
            if i == "swap": s[-2:] = reversed(s[-2:]) #swap 2 last elements of array
            if i == "rot" : s[-3:] = s[-1:]+s[-3:-1] #rotate last 3 elements of array (1,2,3,4) -> (1,4,2,3)
            if i == "pop" : s.pop()
            if i == "+"   : s[-2:] = [sum(s[-2:])] #merge 2 last elements with addition
            if i == "-"   : s[-2:] = [s[-2]-s[-1]] #merge 2 last elements with subtraction
            if i == "*"   : s[-2:] = [s[-2]*s[-1]] #merge 2 last elements with multiplication
            if i == "/"   : s[-2:] = [int(s[-2]/s[-1])] #merge 2 last elements with division
            if i == "%"   : s[-2:] = [s[-2]%s[-1]] #merge 2 last elements with modulus
            if i == "in"  : s.append(int(input()) if a % 2 == 0 else ord(input())) #read input and convert to ASCII if needed
            if i == "out" : print(int(s.pop()) if a % 2 == 0 else chr(s.pop()),end="") #write to output and convert to ASCII if needed
            if i == "jump": pc = p.index(("label",a)) if a.pop() else pc #pop and jump if not 0
            pc += 1
        print("\n\nExecution finished.")
    def parse(src):
        OP_STACK, OP_CALC = ["nop", "dup", "swap", "rot", "pop"], "+-*/%"
        i, spaces = [], 0
        for c in src:
            if c != " ":
                if c == "+": i.append((OP_STACK[spaces % 5],None) if spaces < 5 else ("push",spaces - 5))
                if c == "*": i.append((OP_CALC[spaces % 5],None))
                if c == ".": i.append(("out",spaces))
                if c == ",": i.append(("in",spaces))
                if c == "`": i.append(("label",spaces))
                if c == "'": i.append(("jump",spaces))
                spaces = 0
            else:
                spaces += 1
        return i
    def select(ops, n):
        return ops[n % len(ops)]

def main():
  if len(sys.argv) == 2:
      file = open(sys.argv[1])
      parsed = starry.parse(file.read())
      #print(parsed,"\n")
      starry.run(parsed)
  else:
      print("Usage:", sys.argv[0], "filename")
if __name__ == "__main__": main()