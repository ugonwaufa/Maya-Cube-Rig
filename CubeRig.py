from maya import cmds

cube = cmds.polyCube()
print (cube)
cubeShape = cube[0]
print(cubeShape)
circle = cmds.circle()
print(circle)
circleShape = circle[0]

cmds.parent(cubeShape, circleShape)
cmds.setAttr(cubeShape+".translate", lock = True)
cmds.setAttr(cubeShape+".rotate", lock = True)
cmds.setAttr(cubeShape+".scale", lock = True)

cmds.select(circleShape)
