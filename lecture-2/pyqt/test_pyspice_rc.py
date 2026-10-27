# pip install pyspice
# C:\Users\{user}\AppData\Local\Python\pythoncore-3.14-64\Scripts/pyspice-post-installation.exe --install-ngspice-dll

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import matplotlib.pyplot as plt

from pathlib import Path
from PySpice.Spice.Parser import SpiceParser

# Define the path to your netlist file
file_path = Path('rc.cir')

# Parse the netlist file
parser = SpiceParser(path=str(file_path))

# Build the circuit object from the parser
circuit = parser.build_circuit()

# Create a simulator instance to run analysis
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
simulator.initial_condition(output = 0)  # Set initial condition for the capacitor voltage

# Run the simulation
analysis = simulator.transient(step_time=1e-6, end_time=50e-3)


v_out=analysis['output']  # Access the voltage across the capacitor
v_in=analysis['input']  # Access the input voltage


plt.figure()
plt.plot(analysis.time.as_ndarray(), v_out.as_ndarray())
plt.plot(analysis.time.as_ndarray(), v_in.as_ndarray())
plt.title('Voltage across Capacitor')
plt.xlabel('Time [s]')
plt.ylabel('Voltage [V]')
plt.grid()
plt.show()