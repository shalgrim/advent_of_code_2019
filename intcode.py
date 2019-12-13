from copy import copy


class Intcode(object):
    def __init__(self, instructions):
        self.memory = copy(instructions)
        self.instruction_pointer = 0
        self.output_bus = []

    @staticmethod
    def parse_instruction(instruction_int):
        instruction_s = str(instruction_int)
        opcode = int(instruction_s[-2:])
        param_modes = [0, 0, 0]

        for i, digit in enumerate(instruction_s[:-2][::-1]):
            param_modes[i] = int(digit)

        return opcode, param_modes

    def get_params(self, opcode, param_modes):
        params = []
        if opcode in (1, 2, 5, 6, 7, 8):  # two input params, one output param
            for i in range(2):
                if param_modes[i] == 0:  # position
                    params.append(
                        self.memory[self.memory[self.instruction_pointer + i + 1]]
                    )
                elif param_modes[i] == 1:  # immediate
                    params.append(self.memory[self.instruction_pointer + i + 1])

            params.append(self.memory[self.instruction_pointer + 3])
        elif opcode in (3, 4):
            params.append(self.memory[self.instruction_pointer + 1])

        return params

    def process_instruction(self, opcode, params):
        if opcode == 1:
            self.memory[params[2]] = params[0] + params[1]
            self.instruction_pointer += 4
        elif opcode == 2:
            self.memory[params[2]] = params[0] * params[1]
            self.instruction_pointer += 4
        elif opcode == 3:
            in_param = input('need some input please: ')
            self.memory[params[0]] = int(in_param)
            self.instruction_pointer += 2
        elif opcode == 4:
            print(self.memory[params[0]])
            self.output_bus.append(self.memory[params[0]])
            self.instruction_pointer += 2
        elif opcode == 5:
            if params[0] != 0:
                self.instruction_pointer = params[1]
            else:
                self.instruction_pointer += 3
        elif opcode == 6:
            if params[0] == 0:
                self.instruction_pointer = params[1]
            else:
                self.instruction_pointer += 3
        elif opcode == 7:
            self.memory[params[2]] = 1 if params[0] < params[1] else 0
            self.instruction_pointer += 4
        elif opcode == 8:
            self.memory[params[2]] = 1 if params[0] == params[1] else 0
            self.instruction_pointer += 4

    def run(self):
        while self.memory[self.instruction_pointer] != 99:
            instruction = self.memory[self.instruction_pointer]
            opcode, param_modes = Intcode.parse_instruction(instruction)
            params = self.get_params(opcode, param_modes)
            self.process_instruction(opcode, params)
