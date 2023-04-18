# add gizmo
toolbar = nuke.menu('Nodes')
menu = toolbar.addMenu('Westworld', icon='westworld.png')
menu.addCommand('ww_gizmo', "nuke.createNode('ww_gizmo')", "")
