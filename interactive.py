# The function below is called when any passed values have changed.
# Be sure to turn on the related parameter in the DAT to retrieve these values.
#
# me - this DAT
# renderPickDat - the connected Render Pick DAT
#
# events - a list of named tuples with the fields listed below.
# eventsPrev - a list of events holding the eventsPrev values.
#
#	u				- The selection u coordinate.			(float)
#	v				- The selection v coordinate.			(float)
#	select			- True when a selection is ongoing.		(bool)
#	selectStart		- True at the start of a selection.		(bool)
#	selectEnd		- True at the end of a selection.		(bool)
#	selectedOp		- First picked operator.				(OP)
#	selectedTexture	- Texture coordinate of selectedOp.		(Position)
#	pickOp			- Currently picked operator.			(OP)
#	pos				- 3D position of picked point.			(Position)
#	texture			- Texture coordinate of picked point.	(Position)
#	color			- Color of picked point.				(4-tuple)
#	normal			- Geometry normal of picked point.		(Vector)
#	depth			- Post projection space depth.			(float)
#	instanceId		- Instance ID of the object.			(int)
#	row				- The row associated with this event	(float)
#	inValues		- Dictionary of input DAT strings for the given row, where keys are column headers. (dict)
#	custom	 		- Dictionary of selected custom attributes

GENERATOR = op('../blueprint')
def onEvents(renderPickDat, events, eventsPrev):

	for event, eventPrev in zip(events, eventsPrev):
		print(event.u, event.pickOp, event.instanceId)
		name = op('df_ready')[event.instanceId+1, f"{GENERATOR.par.Details1}"]
		
		if event.pickOp == "/scatter/blueprint/plot/out1":
			op('display_details1').par.text = name
			op('label_pos').par.tx = (op('pos_xy')['x_pos'][event.instanceId])
			op('label_pos').par.ty = (op('pos_xy')['y_pos'][event.instanceId]) +.05
			op('label').par.fillalpha, op('label').par.borderalpha = 1, 1

		if event.pickOp == "/scatter/blueprint/backgroud/out1":
			op('display_details1').par.text = ""
			op('label').par.fillalpha, op('label').par.borderalpha = 0, 0

	pass
'''
		if event.pickOp:
			name = (op('final_data')[event.instanceId+1, "Name"])
			if name != "Name":
				op('details').unstore('*')
				op('details').store('name', name)
				op('label_pos').par.tx = (op('position')['x_pos'][event.instanceId])/op('scale_canvas').par.value0 
				op('label_pos').par.ty = (op('position')['y_pos'][event.instanceId])/op('scale_canvas').par.value0 +.1
				op('display_details1').par.text = name


	for event, eventPrev in zip(events, eventsPrev):
		if event.select and event.pickOp: 
			if '/2wayArea/geo_minT/' in event.pickOp.path or '/2wayArea/geo_maxT/' in event.pickOp.path:
				mouse_x = event.texture.x
				op('constant_u').par.value0 = mouse_x
				op('constant_select').par.value0 = 1

				if '/2wayArea/geo_min' in event.pickOp.path: 
					op('constant_geo').par.value0 = 0 
				if '/2wayArea/geo_max' in event.pickOp.path: 
					op('constant_geo').par.value0 = 1 

		if event.selectEnd:		
			op('constant_select').par.value0 = 0 

		pass
		'''