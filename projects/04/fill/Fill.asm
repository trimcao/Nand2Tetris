// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.


(OUTERLOOP)
// initialization
    @SCREEN
    D = A
    @addr
    M = D

    @i
    M = 0

// listen to keyboard
    @KBD
    D = M
    @WHITEN
    D; JEQ

(BLACKEN)
    @i
    D = M
    @8192
    D = D - A
    @OUTERLOOP
    D; JEQ

    // fill the screen
    @addr
    A = M       // load the address as the address stored in @addr
    M = -1
    // increment @addr
    @i
    M = M + 1
    @addr
    M = M + 1
    @BLACKEN
    0; JMP


(WHITEN)
    @i
    D = M
    @8192
    D = D - A
    @OUTERLOOP
    D; JEQ

    // fill the screen
    @addr
    A = M       // load the address as the address stored in @addr
    M = 0
    // increment @addr
    @i
    M = M + 1
    @addr
    M = M + 1
    @WHITEN
    0; JMP

//(END)
//    @END
//    0; JMP
