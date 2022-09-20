# me - this DAT
# 
# comp - the List Component that holds this panel
# row - the row number of the cell being updated
# col - the column number of the cell being updated
#
# attribs contains the following members:
#
# text				   str            cell contents
# help                 str       	  help text
#
# textColor            r g b a        font color
# textOffsetX		   n			  horizontal text offset
# textOffsetY		   n			  vertical text offset
# textJustify		   m			  m is one of:  JustifyType.TOPLEFT, JustifyType.TOPCENTER,
#													JustifyType.TOPRIGHT, JustifyType.CENTERLEFT,
#													JustifyType.CENTER, JustifyType.CENTERRIGHT,
#													JustifyType.BOTTOMLEFT, JustifyType.BOTTOMCENTER,
#													JustifyType.BOTTOMRIGHT
#
# bgColor              r g b a        background color
#
# leftBorderInColor	   r g b a		  inside left border color
# rightBorderInColor   r g b a		  inside right border color
# bottomBorderInColor  r g b a		  inside bottom border color
# topBorderInColor	   r g b a		  inside top border color
#
# leftBorderOutColor   r g b a		  outside left border color
# rightBorderOutColor  r g b a		  outside right border color
# bottomBorderOutColor r g b a		  outside bottom border color
# topBorderOutColor	   r g b a		  outside top border color
#
# colWidth             w              sets column width
# colStetch            True/False     sets column stretchiness (width is min width)
# rowHeight            h              sets row height
# rowStetch            True/False     sets row stretchiness (height is min height)
# rowIndent            w              offsets entire row by this amount
#
# editable			   int			  number of clicks to activate editing the cell.
# draggable             True/False     allows cell to be drag/dropped elsewhere
# fontBold             True/False     render font bolded
# fontItalic           True/False     render font italicized
# fontSizeX            float		  font X size in pixels
# fontSizeY            float		  font Y size in pixels, if not specified, uses X size
# sizeInPoints         True/False	  If true specify font size in points, rather than pixels.
# fontFace             str			  font face, example 'Verdana'
# fontFile             str			  font file, when specified on disk or embedded in VFS.
# wordWrap             True/False     word wrap
#
# top                  TOP			  background TOP operator
#
# select   true when the cell/row/col is currently being selected by the mouse
# rollover true when the mouse is currently over the cell/row/col
# radio    true when the cell/row/col was last selected
# focus    true when the cell/row/col is being edited
#
#

# called when Reset parameter is pulsed, or on load
tab = op('num_vars')
print(tab)
num = tab.numRows


## add content to the cells of the list
def onInitCell(comp, row, col, attribs):
	for i in range(0,num):
		if row == i and col == 0:
			attribs.text = tab[i,0].val
		if row == i and col == 1:
			attribs.text = tab[i,1].val
	for i in range(0,op('selected_vars').numRows):
		if row == i and col == 2:
			try:
				attribs.text = op('selected_vars')[i,0].val
			except:
				pass
	return


## color of list
def onInitRow(comp, row, attribs):
	if row == 0:
		bgColor =  [0.4,0.2,0.2,1]
	else:
		bgColor = [0.2,0.2,0.2,1]

	attribs.bgColor = bgColor
	return


## size of list
def onInitCol(comp, col, attribs):
	# specify each columns width in a list
	colWidth = [150,150,250,90,90]

	# specify which column is stretchable in a list
	stretch = [1]

	# assign the width and stretch to the column attributes
	attribs.colWidth = colWidth[0]
	attribs.colStretch = stretch[0]

	return


## further features
def onInitTable(comp, attribs):
	# set every cells justify to be center left
	attribs.textJustify = JustifyType.CENTERLEFT

	# set every cells bottom border to a slight blue
	attribs.bottomBorderOutColor = [0.2,0.2,0.6,1]

	return

# called during specific events
#
# coords - a named tuple containing the following members:
#   x
#   y
#   u
#   v

def onRollover(comp, row, col, coords, prevRow, prevCol, prevCoords):
	# make sure to only change the layout if row and prevRow are different
	if row != prevRow:

		# we don't want to change the header row so test for row being larger then 0
		# this also takes care of when rolling out of the List where row would return -1
		if row > 0 and col==0:
			rowAttribs = comp.rowAttribs[row]
			rowAttribs.bgColor = [0.2,0.4,0.2,1]

		if row > 0 and col==1:
			rowAttribs = comp.rowAttribs[row]
			rowAttribs.bgColor = [0.5,0.2,0.2,1]

		# same as before, we check that prevRow is not the header row and
		# we are not entering the List from the outside
		if prevRow > 0:
			rowAttribs = comp.rowAttribs[prevRow]
			rowAttribs.bgColor = [0.2,0.2,0.2,1]

	return


kmeans_vars = []

def onSelect(comp, startRow, startCol, startCoords, endRow, endCol, endCoords, start, end):
	info = tab[startRow,0]
	parent(1).par.reset.pulse()

	# ADDA VARIABLES ON KMEANS
	if start and startRow > 0 and startCol == 0:
		# get the row attributes for the clicked on row and change the bgColor
		rowAttribs = comp.rowAttribs[startRow]
		rowAttribs.bgColor = [0.2,0.6,0.4,1]

		# save the startRow in storage so we can revert the layout changes on mouse up
		comp.store('prevSelect', startRow)

		# run a script and pass row and column as an argument
		op('script1').run(startRow, startCol)

		# save the variables selected in a table
		if info not in kmeans_vars:
			kmeans_vars.append(info)
		op('choosen').store('info', kmeans_vars)

	# DELETE VARIABLES
	elif start and startRow > 0 and startCol == 1:
		# get the row attributes for the clicked on row and change the bgColor
		rowAttribs = comp.rowAttribs[startRow]
		rowAttribs.bgColor = [0.6,0.2,0.2,1]

		# save the startRow in storage so we can revert the layout changes on mouse up
		comp.store('prevSelect', startRow)

		# run a script and pass row and column as an argument
		op('script1').run(startRow, startCol)

		# save the variables selected in a table
		info = tab[startRow,0]
		if info in kmeans_vars:
			kmeans_vars.remove(info)
		op('text4').par.text = info

	elif (startCol == 0) and end:
		# get the previous selected row from storage
		prevSelRow = comp.fetch('prevSelect',None)

		# if there is a previously selected row change the layout back to default
		if prevSelRow:
			rowAttribs = comp.rowAttribs[prevSelRow]

			# if my mouse is still over the previously selected row, change it's layout to the rollover bg
			# else change it to the default look
			if startRow == endRow:
				bgColor = [0.2,0.4,0.2,1]
			else:
				bgColor = [0.2,0.2,0.2,1]

			# assign the color to the rows bgColor attribute
			rowAttribs.bgColor = bgColor

		# remove the previously selected row from storage
		comp.unstore('prevSelect')
	



	return

def onRadio(comp, row, col, prevRow, prevCol):
	return

def onFocus(comp, row, col, prevRow, prevCol):
	return

def onEdit(comp, row, col, val):
	return

# return True if interested in this drop event, False otherwise
def onHoverGetAccept(comp, row, col, coords, prevRow, prevCol, prevCoords, dragItems):
	return False
def onDropGetAccept(comp, row, col, coords, prevRow, prevCol, prevCoords, dragItems):
	return False

	