"""TPRG2131 Winter 202x RC class starter with simplistic test code."""

class ResistorCapacitor (object):
    """Model a resistor-capacitor network"""
    def __init__(self, resistance, capacitance, initial=0.0):
        """Initialize with resistance (ohms), capacitance (farads), and initial voltage (volts)."""
        self.resistance = resistance
        self.capacitance = capacitance
        self.initial_voltage = initial
        self.voltage_value = initial
        return

    #
    # Mutator methods
    #
    def set_voltage(self, voltage):
        """Set the voltage."""
        self.voltage_value = voltage
        
    #
    # Accessor methods
    #
    def voltage(self, time):
        """Calculate the voltage at a given time using the RC discharge formula."""
        return self.voltage_value * math.exp(-time / (self.resistance * self.capacitance))    
        


## Test code (place at bottom of the file)
if __name__ == "__main__":
    print("Self testing...")
    rc1 = ResistorCapacitor(1000.0, 1.0e-6)
    rc1.set_voltage(5.0)
    rc2 = ResistorCapacitor(10.0e3, 22.0e-6, 12.0)
    print("rc1:")
    print(rc1.resistance, rc1.capacitance, rc1.initial_voltage)
    for vtime in range(0, 6):
        stime = vtime * 0.5e-3
        print(stime, rc1.voltage(stime))
    print("rc2:")
    print(rc2.resistance, rc2.capacitance, rc2.initial_voltage)
    for vtime in range(0, 6):
        stime = vtime * 150.0e-3
        print(stime, rc2.voltage(stime))
# done
