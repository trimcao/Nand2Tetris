// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// initialization
    @i
    M = 0
    @R2     // result stored at R2
    M = 0

(LOOP)
    // compare i with R0, the loops stops if i == R0
    @i
    D = M
    @R0
    D = D - M // D = i - R0

    @END
    D; JEQ

    // increment i
    @i
    M = M + 1

    @R1
    D = M
    @R2
    M = M + D
    @LOOP
    0; JMP

(END)
    @END
    0; JMP
