""" 
Environment Management 
====================== 
This file ensures that the python and matplotlib versions satisfy the minimum 
for this package. 
""" 

try: 
	ModuleNotFoundError 
except NameError: 
	ModuleNotFoundError = ImportError 
try: 
	import matplotlib as mpl 
except (ModuleNotFoundError, ImportError): 
	raise ModuleNotFoundError("Matplotlib not found.") 
if int(mpl.__version__[0]) < 2: 
	raise RuntimeError("Matplotlib version >= 2 required.") 
else: 
	pass 
import sys 
if sys.version_info[:2] <= (3, 5) and sys.version_info[:2] != (2, 7): 
	raise RuntimeError("Python version 2.7 or >= 3.5 required.") 
else: 
	pass 

