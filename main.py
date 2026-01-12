class VirtualMachine:
    MOVE = 0
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    PUSH = 5
    POP = 6
    RETURN = 7
    CALL = 8
    SYSTEM_CALL = 9
    COMPARE = 10
    JUMP = 11
    JUMP_NOT_LESS = 12
    JUMP_LESS = 13
    JUMP_NOT_EQUAL = 14
    JUMP_EQUAL = 15
    JUMP_NOT_MORE = 16
    JUMP_MORE = 17
    EXIT = 18
    # Register addresses
    RSP = 0
    RBP = 1
    RAX = 2
    RBX = 3
    RCX = 4
    RDX = 5
 
    def __init__(self, memoryCapacity):
        self.instructPtr = 0
        self.memoryCapacity = memoryCapacity
        # First 6 positions are reserved for registers
        self.memory = [0] * memoryCapacity

    def execute_command(self, cmd, arg1, arg2):
        if cmd == VirtualMachine.MOVE:
            self.memory[arg1] = arg2
        elif cmd == VirtualMachine.ADD:
            self.memory[arg1] += arg2

    def reset(self):
        self.instructPtr = 0
        self.memory = [0] * self.memoryCapacity

    def debug(self):
        print("rsp:", self.rsp)
        print("rsp:", self.rbp)
        print("rsp:", self.rax)
        print("rsp:", self.rbx)
        print("rsp:", self.rcx)
        print("rsp:", self.rdx)

 # Advance position in a game
if __name__ == "__main__":
    print("Hello, World!")