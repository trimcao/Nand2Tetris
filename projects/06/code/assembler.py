"""
Project 6 - Nand2Tetris
Hack Assembler
Name: Tri Minh Cao
Email: trimcao@gmail.com
Date: March 2016
"""

class Parser:
    """
    Idea: The parser class will contain the file object. We will not need methods
    like hasNext() and advance(), just use existing methods of file object.
    But other processing methods can be used to parse the command (because the
    methods take input as string or list of chars)
    """
    def __init__(self, filename):
        # do some processing here
        self.asm = open(filename, 'r')

    # processing idea: get a command, then iterate each character
    # look for '=', ";"
    # ignore white space by using replace()
    # ignore blank line by checking length of the line
    # usual syntax: dest = comp ; jump
    # dest = comp
    # comp ; jump
    # dest() and comp() methods may return -1 to notice that the command does
    #   not have the requested part

    # also check comment

    def commandType(self, command):
        for idx in range(len(command)):
            if (idx == len(command) - 1):
                return None
            elif (command[idx] == '@'):
                return 'A_COMMAND'
            elif (command[idx] == ';' or command[idx] == '='):
                return 'C_COMMAND'
            elif (command[idx] == '('):
                return 'L_COMMAND'

    def dest(self, command):
        # find symbol '='
        signIdx = -1
        for idx in range(len(command)):
            if (command[idx] == '='):
                signIdx = idx
                break
        if (signIdx == -1):
            return None
        else:
            return command[0:signIdx]

    def jump(self, command):
        # find symbol ';'
        signIdx = -1
        for idx in range(len(command)):
            if (command[idx] == ';'):
                signIdx = idx
                break
        if (signIdx == -1):
            return None
        else:
            return command[signIdx + 1:-1]

    def comp(self, command):
        # find symbol ';' or '='
        signIdx = -1
        sign = None
        for idx in range(len(command)):
            if (command[idx] == ';' or command[idx] == '='):
                signIdx = idx
                sign = command[idx]
                break

        if (signIdx == -1):
            return None
        else:
            if (sign == ';'):
                return command[:signIdx]
            else: # sign == '='
                s = ''
                for idx in range(signIdx + 1, len(command) - 1):
                    if (command[idx]  != ';'):
                        s += command[idx]
                    else:
                        break
                return s

    def symbol(self, command):
        cmdType = self.commandType(command)
        if (cmdType == 'A_COMMAND'):
            return command[1:-1]
        elif (cmdType == 'L_COMMAND'):
            return command[1:-1]
        else:
            return None

    def destBin(self, string):
        if (string == None):
            return '000'
        elif (string == 'M'):
            return '001'
        elif (string == 'D'):
            return '010'
        elif (string == 'MD'):
            return '011'
        elif (string == 'A'):
            return '100'
        elif (string == 'AM'):
            return '101'
        elif (string == 'AD'):
            return '110'
        elif (string == 'AMD'):
            return '111'

    def compBin(self, string):
        if (string == '0'):
            return '0101010'
        elif (string == '1'):
            return '0111111'
        elif (string == '-1'):
            return '0111010'
        elif (string == 'D'):
            return '0001100'
        elif (string == 'A'):
            return '0110000'
        elif (string == '!D'):
            return '0001101'
        elif (string == '!A'):
            return '0110001'
        elif (string == '-D'):
            return '0001111'
        elif (string == '-A'):
            return '0110011'
        elif (string == 'D+1'):
            return '0011111'
        elif (string == 'A+1'):
            return '0110111'
        elif (string == 'D-1'):
            return '0001110'
        elif (string == 'A-1'):
            return '0110010'
        elif (string == 'D+A'):
            return '0000010'
        elif (string == 'D-A'):
            return '0010011'
        elif (string == 'A-D'):
            return '0000111'
        elif (string == 'D&A'):
            return '0000000'
        elif (string == 'D|A'):
            return '0010101'
        elif (string == 'M-1'):
            return '1110010'
        elif (string == 'D+M'):
            return '1000010'
        elif (string == 'D-M'):
            return '1010011'
        elif (string == 'M-D'):
            return '1000111'
        elif (string == 'D&M'):
            return '1000000'
        elif (string == 'D|M'):
            return '1010101'
        elif (string == 'M'):
            return '1110000'
        elif (string == '!M'):
            return '1110001'
        elif (string == '-M'):
            return '1110011'
        elif (string == 'M+1'):
            return '1110111'

    def jumpBin(self, string):
        if (string == None):
            return '000'
        elif (string == 'JGT'):
            return '001'
        elif (string == 'JEQ'):
            return '010'
        elif (string == 'JGE'):
            return '011'
        elif (string == 'JLT'):
            return '100'
        elif (string == 'JNE'):
            return '101'
        elif (string == 'JLE'):
            return '110'
        elif (string == 'JMP'):
            return '111'

    def toBin(self, string):
        number = int(string)
        binary = bin(number)[2:]
        if (len(binary) < 15):
            for i in range(15 - len(binary)):
                binary = '0' + binary
        return binary


class SymbolTable:

    def __init__(self):
        self.st = dict()
        # initialization
        self.st['R0'] = 0
        self.st['R1'] = 1
        self.st['R2'] = 2
        self.st['R3'] = 3
        self.st['R4'] = 4
        self.st['R5'] = 5
        self.st['R6'] = 6
        self.st['R7'] = 7
        self.st['R8'] = 8
        self.st['R9'] = 9
        self.st['R10'] = 10
        self.st['R11'] = 11
        self.st['R12'] = 12
        self.st['R13'] = 13
        self.st['R14'] = 14
        self.st['R15'] = 15
        self.st['SP'] = 0
        self.st['LCL'] = 1
        self.st['ARG'] = 2
        self.st['THIS'] = 3
        self.st['THAT'] = 4
        self.st['SCREEN'] = 16384
        self.st['KBD'] = 24576

    def contains(self, symbol):
        return (symbol in self.st)

    def addEntry(self, symbol, address):
        self.st[symbol] = address

    def getAddress(self, symbol):
        if (symbol in self.st):
            return self.st[symbol]
        else:
            return None


def isNumber(string):
    """
    check if a string is a number or not
    """
    for char in string:
        charNum = ord(char)
        if (charNum < 48 or charNum > 57):
            return False
    return True


add = 'Add'
maxfile = 'Max'
rectfile = 'Rect'
pong = 'Pong'
target = add
parser = Parser(target + '.asm')
out = open(target + '.hack', 'w')

lineNum = 0
freeRAM = 16
table = SymbolTable()

# first pass, find L instruction
for l in parser.asm:
    line = l.strip()
    line = line.replace(' ', '')
    newLine = ''
    for char in line:
        if (char != '/'):
            newLine += char
        else:
            break
    #print newLine
    #print lineNum
    if (len(newLine) > 0):
        cmdType = parser.commandType(newLine)
        if (cmdType == 'L_COMMAND'):
            symbol = parser.symbol(newLine)
            table.addEntry(symbol, lineNum)
        else:
            lineNum += 1

#print table.st

# second pass
parser = Parser(target + '.asm')
for l in parser.asm:
    line = l[:-1].replace(' ', '')
    newLine = ''
    for char in line:
        if (char != '/'):
            newLine += char
        else:
            break

    if (len(newLine) > 0):
        #print newLine
        #print test.comp(newLine)
        #print
        # now newLine is the command without comment and spaces
        # we should use methods from Parser class with each newLine

        cmdType = parser.commandType(newLine)
        output = ''
        if (cmdType == 'A_COMMAND'):
            output += '0'
            sym = parser.symbol(newLine)
            isNum = isNumber(sym)
            #print "Symbol: ", list(sym)
            if (isNum):
                output += parser.toBin(parser.symbol(newLine))
            else:
                #print table.contains(sym)
                if (table.contains(sym)):
                    #print table.getAddress(sym)
                    output += parser.toBin(table.getAddress(sym))
                else:
                    table.addEntry(sym, freeRAM)
                    freeRAM += 1
                    output += parser.toBin(table.getAddress(sym))

        elif (cmdType == 'C_COMMAND'):
            output += '111'
            comp = parser.compBin(parser.comp(newLine))
            jump = parser.jumpBin(parser.jump(newLine))
            dest = parser.destBin(parser.dest(newLine))
            #print list(parser.comp(newLine))
            #print comp
            #print parser.jump(newLine)
            #print jump
            #print dest
            output += comp + dest + jump

        if (len(output) > 0):
            #print output
            #print
            out.write(output + '\n')

out.close()
