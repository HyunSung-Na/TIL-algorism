import sys

N = int(sys.stdin.readline())
S = 0

for _ in range(N):
    opcodeStr = sys.stdin.readline()

    opcode = opcodeStr.split()[0]
    if opcode == "add":
        S |= 1 << int(opcodeStr.split()[1])
    elif opcode == "remove":
        S &= ~(1 << int(opcodeStr.split()[1]))
    elif opcode == "check":
        if S & (1 << int(opcodeStr.split()[1])):
            print(1)
        else:
            print(0)
    elif opcode == "toggle":
        S ^= (1 << int(opcodeStr.split()[1]))
    elif opcode == "all":
        S = (1 << 21) - 1
    elif opcode == "empty":
        S = 0
