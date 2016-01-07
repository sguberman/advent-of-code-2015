class Machine(object):

    def __init__(self, instructions_file):
        self.registers = {'a': 1,
                          'b': 0,
                          }
        self.position = 0
        instructions = []
        with open(instructions_file, 'r') as f:
            for line in f:
                instructions.append(line.strip())
        self.instructions = instructions

    def hlf(self, r):
        self.registers[r] /= 2
        self.position += 1

    def tpl(self, r):
        self.registers[r] *= 3
        self.position += 1

    def inc(self, r):
        self.registers[r] += 1
        self.position += 1

    def jmp(self, offset):
        self.position += int(offset)

    def jie(self, r, offset):
        r = r.strip(',')
        if self.registers[r] % 2 == 0:
            self.jmp(offset)
        else:
            self.position += 1

    def jio(self, r, offset):
        r = r.strip(',')
        if self.registers[r] == 1:
            self.jmp(offset)
        else:
            self.position += 1

    def run(self):
        while self.position < len(self.instructions):
            self.execute()

    def execute(self):
        instr = self.instructions[self.position].split()
        args = instr[1:]
        fun = getattr(self, instr[0])
        fun(*args)

if __name__ == '__main__':
    turing = Machine('day23.input')
    turing.run()
    print(turing.registers['b'])
