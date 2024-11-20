        .org            $0200

        lda             #$aa
        sta             $4000
Delay1:
        ldx             #$ff
Delay2:
        ldy             #$ff
Delay3:
        dey
        bne Delay3
        dex
        bne Delay2
        lda             #$55
        sta             $4000
Delay1b:
        ldx             #$ff
Delay2b:
        ldy             #$ff
Delay3b:
        dey
        bne Delay3b
        dex
        bne Delay2b

        jmp             $0200
        nop
        nop
        nop
