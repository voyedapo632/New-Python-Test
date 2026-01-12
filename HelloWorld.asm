rsp
rbp
rax
rbx
rcx
rdx

mov
add
sub
mul
div
push
pop
ret
call
syscall
cmp
jmp
jnl
jl
jne
je
jnm
jm
exit

main:
    push 5
    mov %rax, $5
    mul %rax, [%rsp]
    exit