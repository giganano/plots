""" 
Core routines for manipulating matplotlib figures. 
""" 

from __future__ import absolute_import 

__all__ = ["append_axes", "named_colors", "fancy_legend", "mpl_loc",
	"markers", "align_subplots", "zoom_box", "draw_box", 
	"dummy_background_axes"]   

from . import env 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes as zia 
from mpl_toolkits.axes_grid1 import make_axes_locatable 


def append_axes(ax, loc = "right", size = "5%", pad = 0, **kwargs): 
	""" 
	Append axes to an existing set of axes and return the object. 

	Parameters 
	========== 
	ax :: axes 
		The matplotlib axis object to append to 
	loc :: str [default :: "right"] 
		Where to append the axes on the existing axes 
	size :: str [default :: "5%"] 
		A string denoting the size ratio 
	pad :: float 
		The space between the axes 
	""" 
	divider = make_axes_locatable(ax) 
	return divider.append_axes(loc, size = size, pad = pad, **kwargs)  


def named_colors(): 
	""" 
	Returns 
	======= 
	colors :: dict 
		A dictionary of color named to matplotlib colors 
		This is simply matplotlib.colors.get_named_colors_mapping() 
	""" 
	return mpl.colors.get_named_colors_mapping() 


def fancy_legend(leg, colors):
	r"""
	Make legend handles invisible and set text colors to the color of the
	label.

	Parameters
	----------
	leg : ``matplotlib.artist.Artist``
		The legend object to modify
	colors : ``list``
		A list of strings containing the names of the colors to switch the
		text labels to.
	"""
	if len(leg.legendHandles) != len(colors):
		raise ValueError("""\
Number of legend entries does not match length of colors list: (%d, %d)""" % (
			len(leg.legendHandles), len(colors)))
	else:
		for i in range(len(colors)):
			leg.get_texts()[i].set_color(colors[i])
			leg.legendHandles[i].set_visible(False)


def mpl_loc(label):
	"""
	Parameters 
	========== 
	label :: str [case-insensitive] 
		A descriptive location of a point in a box. 
		Recognized inputs 
		----------------- 
			"best"
			"upper right"
			"upper left"
			"lower left"
			"lower right"
			"right"
			"center left"
			"center right"
			"lower center"
			"upper center"
			"center"

	Returns 
	======= 
	index :: int 
		The matplotlib integer denoting the location within the box 

	Example 
	======= 
	>>> subplot.legend(loc = mpl_loc("upper right")) 
	"""
	indeces = {
		"best": 0,
		"upper right": 1,
		"upper left": 2,
		"lower left": 3,
		"lower right": 4,
		"right": 5,
		"center left": 6,
		"center right": 7,
		"lower center": 8,
		"upper center": 9,
		"center": 10
	} 

	if label.lower() in indeces.keys(): 
		return indeces[label.lower()] 
	else: 
		raise ValueError("Unrecognized location string: %s" % (label)) 

def markers():
	"""
	Returns a dictionary of terms to matplotlib marker characters.

	Recognized markers:
	---------------
	point
	pixel
	circle
	triangle_down
	triangle_up
	triangle_left
	triangle_right
	tri_down
	tri_up
	tri_left
	tri_right
	octagon
	square
	pentagon
	plus_filled
	star
	hexagon1
	hexagon2
	plus
	x
	x_filled
	diamond
	thin_diamond
	vline
	hline
	tickleft
	tickright
	tickup
	tickdown
	caretright
	caretleft
	caretup
	caretdown
	caretrightbase
	caretleftbase
	caretupbase

	Example:
	This line of code will produce the scatter plot in red stars:
	plt.plot(range(10), range(10, 20), '%c%c' % (
		graphics.colors()['red'], 
		graphics.markers()['star']
	))
	"""
	return {
		"point":			".",
 		"pixel":			",", 
		"circle":			"o",
		"triangle_down":	"v",
		"triangle_up":		"^", 
		"triangle_left":	"<", 
		"triangle_right":	">",
		"tri_down":			"1",
		"tri_up":			"2", 
		"tri_left":			"3", 
		"tri_right":		"4", 
		"octagon":			"8", 
		"square": 			"s", 
		"pentagon":			"p", 
		"plus_filled":		"P", 
		"star":				"*",
		"hexagon1":			"h", 
		"hexagon2":			"H", 
		"plus":				"+",
		"x":				"x", 
		"x_filled":			"X", 
		"diamond":			"D", 
		"thin_diamond":		"d", 
		"vline":			"|", 
		"hline":			"_", 
		"tickleft":			"TICKLEFT",
		"tickright":		"TICKRIGHT",
		"tickup":			"TICKUP",
		"tickdown":			"TICKDOWN", 
		"caretright":		"CARETRIGHT", 
		"caretleft":		"CARETLEFT", 
		"caretup":			"CARETUP",
		"caretdown":		"CARETDOWN",
		"caretrightbase":	"CARETRIGHTBASE", 
		"caretleftbase":	"CARETLEFTBASE",
		"caretupbase":		"CARETUPBASE"
	}


def align_subplots(ax1, ax2, leftright = True): 
	""" 
	Align the edges of two subplots left-to-right or top-to-bottom such that 
	their edges are flush while maintaining the same aspect ratio on each 
	set of axes. 

	ax1 :: matplotlib subplot 
		The left [top] subplot 
	ax2 :: matplotlib subplot 
		The right [bottom] subplot 
	leftright :: bool [default :: True] 
		If True, the subplots will be aligned left-to-right. Else they'll be 
		aligned top-to-bottom. 

	Raises 
	====== 
	TypeError :: 
		::	Either subplot isn't a matplotlib subplot object 
	""" 
	if (isinstance(ax1, mpl.axes._subplots.AxesSubplot) and 
		isinstance(ax2, mpl.axes._subplots.AxesSubplot)): 
		# Both positional arguments must be matplotlib subplot objects 
		pos1 = ax1.get_position() 
		pos2 = ax1.get_position() 
		""" 
		By simply moving one subplot, they necessarily stay the same size and 
		the aspect ratio is maintained. 
		""" 
		if leftright: 
			pos1.x0 += pos2.x0 - pos1.x1 
			pos1.x1 = pos2.x0 
		else: 
			pos2.y0 += pos1.y0 - pos2.y1 
			pos2.y1 = pos1.y1 
	else: 
		raise TypeError("""Both positional arguments must be a matplotlib \
subplot object. Got: (%s, %s)""" % (type(ax1), type(ax2))) 


def log_scale_ticklabel_formatter(subplot, x = True): 
	""" 
	Format a log-scaled axis such that all ticks less [greater] than +10,000 
	[-10,000] print as a plain number, and all larger numbers print in 
	scientific notation, i.e.: 1, 10, 100, 1000, 10^4, 10^5, etc. 

	Parameters 
	========== 
	subplot :: a matplotlib subplot 
		The subplot to format the ticks for 
	x :: bool [default :: True] 
		If True, formats the x-axis tick labels. Else formats the y-axis tick 
		labels. 

	Raises 
	====== 
	TypeError :: 
		:: 	subplot is not a matplotlib subplot object 
	""" 
	pass 

def _log_scale_xticklabel_formatter(subplot): 
	""" 
	Formats the x-axis ticklabels according to log_scale_ticklabel_formatter. 
	""" 
	subplot.figure.canvas.draw() 
	xaxis = subplot.xaxis 


def zoom_box(subplot, xlim, ylim, zoom = 2, loc = "upper left", 
	borderpad = 0.5):
	"""
	Args:
	---------------
	subplot:		A matplotlib subplot object
	xlim:			The x limits of the inset
	ylim:			The y limits of the inset

	Kwargs:
	---------------
	zoom:			The zoom scale of the inset
						Default: 2
	loc:			The location string denoting where to place the inset
						Default: "upper left"
	borderpad:		Number quantifying how much space to leave between 
					the zoom box and the frame of the subplot
						Default: 0.5
	"""
	axins = zia(subplot, zoom, loc = mpl_loc(loc), borderpad = borderpad)
	axins.set_xlim(xlim)
	axins.set_ylim(ylim)
	return axins

def draw_box(subplot, xlim, ylim):
	"""
	Args:
	---------------
	subplot:		A matplotlib subplot object
	xlim:			The desired x-limits (length-2 list)
	ylim:			The desired y-limits (length-2 list)

	Draws a box defined by the x- and y-limits in black on the 
	subplot
	"""
	if not isinstance(xlim, list):
		message = "xlim must be a list of length 2"
		raise TypeError(message)
	elif len(xlim) != 2:
		message = "xlim must be a list of length 2"
		raise ValueError(message)
	elif not isinstance(ylim, list):
		message = "ylim must be a list of length 2"
		raise TypeError(message)
	elif len(ylim) != 2:
		message = "ylim must be a list of length 2"
		raise ValueError(message)
	else:
		subplot.plot(xlim, 2 * [ylim[0]], c = named_colors()["black"])
		subplot.plot(xlim, 2 * [ylim[1]], c = named_colors()["black"])
		subplot.plot(2 * [xlim[0]], ylim, c = named_colors()["black"])
		subplot.plot(2 * [xlim[1]], ylim, c = named_colors()["black"])


def dummy_background_axes(axes):
	r"""
	Constructs a subplot in the background of a set of subplots with the
	corners aligned, but invisible tick labels.

	Parameters
	----------
	axes : 2-d list
		A 2-d list of subplots. First axis must be the row number of the
		subplot, with the zero'th element at the top of the figure. Second
		axis must be the column number of the subplot, with the zero'th
		element at the left of the figure.

	Returns
	-------
	dummy : subplot
		A matplotlib subplot whose corners are aligned with the grid of
		subplots passed, and will be drawn behind them.

	Raises
	------
	No exceptions are explicitly raised by this routine.
	"""
	dummy = plt.gcf().add_subplot(111, facecolor = "white", zorder = -100)
	posd = dummy.get_position()
	posd.x0 = axes[-1][0].get_position().x0
	posd.x1 = axes[-1][-1].get_position().x1
	posd.y0 = axes[-1][0].get_position().y0
	posd.y1 = axes[0][0].get_position().y1
	dummy.set_position(posd)
	plt.setp(dummy.get_xticklabels(), visible = False)
	plt.setp(dummy.get_yticklabels(), visible = False)
	return dummy

