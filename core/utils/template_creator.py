template = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<template density="40" threshold="200" version="2.1">
    <crop bottom="0" left="0" right="0" top="0"/>
    <rotation angle="0.0"/>
    <corners type="ANGULAR">
        <corner position="TOP_RIGHT">
            <point x="$TR_X$" y="$TR_Y$"/>
        </corner>
        <corner position="TOP_LEFT">
            <point x="$TL_X$" y="$TL_Y$"/>
        </corner>
        <corner position="BOTTOM_LEFT">
            <point x="$BL_X$" y="$BL_Y$"/>
        </corner>
        <corner position="BOTTOM_RIGHT">
            <point x="$BR_X$" y="$BR_Y$"/>
        </corner>
    </corners>
    <fields groups="true" shape="CIRCLE" size="$SZ$">
$GROUPS$
    </fields>
</template>
"""


value ="""                    <value response="$RESP$">
                       <point x="$X$" y="$Y$"/>
                    </value>"""

group =""" <group name="$ID$">
            <question multiple="false" question="sources" rejectMultiple="false" type="RESPONSES_BY_GRID">
                <values>
                  $VALS$
                </values>
            </question>
        </group>"""
        

def create_resp(resp, x, y):
    return value.replace("$RESP$", resp).replace("$X$", str(x)).replace("$Y$", str(y))

def create_group(id, resps):
    val = ""
    for resp in resps:
        val+=resp
        val+="\n"
    return group.replace("$ID$", id).replace("$VALS$", val)

def create_template(groups):
    grps = ""
    for g in groups:
        grps+=g
        grps+="\n"
    return template.replace("$GROUPS$", grps)

r1 = create_resp("Yes", 100, 200)
r2 = create_resp("N0", 200, 200)
g1 = create_group("ROBUS_TEAM1", (r1,r2))
print(create_template((g1,g1)))