#!/usr/bin/env python3
import sys
class starry():
    def run(parsed):
        p,s,pc = parsed, [], 0
        while pc < len(p):
            i,a = p[pc] if isinstance(p[pc], tuple) else (p[pc],None)
            if i == "push": s.append(a)
            if i == "dup" : s.append(s[-1])
            if i == "swap": s = s[:-2]+s[-1:]+s[-2:-1]
            if i == "rot" : s = s[:-3]+s[-1:]+s[-3:-1]
            if i == "pop" : s.pop()
            if i == "+"   : s = s[:-2] + [s[-2]+s[-1]]
            if i == "-"   : s = s[:-2] + [s[-2]-s[-1]]
            if i == "*"   : s = s[:-2] + [s[-2]*s[-1]]
            if i == "/"   : s = s[:-2] + [int(s[-2]/s[-1])]
            if i == "%"   : s = s[:-2] + [s[-2]%s[-1]]
            if i == "in"  : s.append(int(input()) if a % 2 == 0 else ord(input()))
            if i == "out" : print(int(s.pop()) if a % 2 == 0 else chr(s.pop()),end="")
            if i == "jump": pc = p.index(("label",a))
            pc += 1
        print("\n\nExecution finished.")
    def parse(src):
        OP_STACK, OP_CALC = ["nop", "dup", "swap", "rot", "pop"], ["+", "-", "*", "/", "%"]
        i, spaces = [], 0
        for c in src:
            if c != " ":
                if c == "+": i.append(starry.select(OP_STACK, spaces) if spaces < len(OP_STACK) else ("push",spaces - len(OP_STACK)))
                if c == "*": i.append((starry.select(OP_CALC, spaces)))
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