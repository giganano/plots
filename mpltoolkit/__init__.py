""" 
Matplotlib Tools 
================ 
Matplotlib plotting tools. 

Modules 
======= 
presets 
""" 

from __future__ import absolute_import 

# __all__ = ["load_mpl_presets"]
__all__ = ["load_style_sheet"]

from .presets import load_style_sheet
from . import env 
import matplotlib as mpl 
from .core import * 
__all__.extend(core.__all__) 


# def load_mpl_presets(): 
# 	""" 
# 	Load matplotlib presets. 
# 	Preset source file at ~/Work/Research/plots/matplotlib_/presets.py 
# 	""" 
# 	from . import presets as __presets 	# don't add to the public namespace 









