from standard_equipment import standard_breakers

class DistributionBoard():
    
    
    def __init__(self, name, input_cable):
        self.name = name
        self.input_cable = input_cable
        self.inputs_with = [] # Will be read from the excels (defined structure in the excels)
        self.outputs_with_loads = [] # Will be read from the excels (defined structure in the excels)
         
        
    def calculate_breaker(self): # Should be rated between the max cable capacity and load requirement current -- allow for min 20% breathing space
        pass