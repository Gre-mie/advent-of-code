class Arcade:
    def __init__(self, file):
        self.file = file

    def process_file(self):
        arr_of_machines = []
        machine = {}
        for line in self.file:
            if not line:
                arr_of_machines.append(machine)
                machine = {}
            else: 
                line_type, values = line.split(':')
                x, y = values.split(',')

                if 'A' in line_type or 'B' in line_type:
                    line_type = line_type[-1]
                    x = int(x[3:])
                    y = int(y[3:])
                else:
                    x = int(x[3:])
                    y = int(y[3:])        
                machine[line_type] = (x, y)
        arr_of_machines.append(machine) # last machine to add
        return arr_of_machines
            

            
            