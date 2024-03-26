
import matplotlib.pyplot as plt
import os

def load_style_sheet(name):
	path = os.path.dirname(os.path.abspath(__file__))
	plt.style.use("%s/stylesheets/%s.mplstyle" % (path, name))


# import matplotlib as mpl 

# # Text parameters
# mpl.rcParams["font.family"] = "serif"
# mpl.rcParams["text.usetex"] = True
# mpl.rcParams["mathtext.fontset"] = "custom"
# mpl.rcParams["text.latex.preamble"] = r"\usepackage{amsmath}"
# mpl.rcParams["figure.titlesize"] = 18
# mpl.rcParams["axes.titlesize"] = 18
# mpl.rcParams["axes.labelsize"] = 20
# mpl.rcParams["xtick.labelsize"] = 18
# mpl.rcParams["ytick.labelsize"] = 18
# mpl.rcParams["legend.fontsize"] = 18

# # Figure formatting
# mpl.rcParams["figure.figsize"] = (5, 5)
# mpl.rcParams["figure.facecolor"] = "white"

# # Error bars and legend formatting
# mpl.rcParams["errorbar.capsize"] = 5
# mpl.rcParams["legend.numpoints"] = 1
# mpl.rcParams["legend.frameon"] = False
# mpl.rcParams["legend.handletextpad"] = 0.3

# # Axes and tick formatting
# mpl.rcParams["axes.linewidth"] = 0.75
# mpl.rcParams["xtick.direction"] = "in"
# mpl.rcParams["ytick.direction"] = "in"
# mpl.rcParams["ytick.right"] = True
# mpl.rcParams["xtick.top"] = True
# mpl.rcParams["xtick.minor.visible"] = True
# mpl.rcParams["ytick.minor.visible"] = True
# mpl.rcParams["xtick.major.size"] = 10
# mpl.rcParams["ytick.major.size"] = 10
# mpl.rcParams["xtick.minor.size"] = 5
# mpl.rcParams["ytick.minor.size"] = 5
# mpl.rcParams["xtick.major.width"] = 0.5
# mpl.rcParams["ytick.major.width"] = 0.5
# mpl.rcParams["xtick.minor.width"] = 0.5
# mpl.rcParams["ytick.minor.width"] = 0.5
