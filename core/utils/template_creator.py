from xml.sax.saxutils import escape

template = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<template density="30" threshold="200" version="2.1">
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
    <fields groups="true" shape="SQUARE" size="$SZ$">
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

qrcode = """        <group name="$ID$">
            <area name="id" type="BARCODE"> 
                <corners>
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
            </area>
        </group>"""        

def create_resp(resp, x, y):
    return value.replace("$RESP$", resp).replace("$X$", str(x)).replace("$Y$", str(y))

def create_group(id, resps):
    val = ""
    for resp in resps:
        val+=resp
        val+="\n"
    return group.replace("$ID$", escape(id)).replace("$VALS$", escape(val))

def create_template(tl,tr,bl,br,groups, field_sz):
    grps = ""
    for g in groups:
        grps+=escape(g)
        grps+="\n"
    return template.replace("$GROUPS$", grps).\
            replace("$TR_X$", str(tr[0])).\
            replace("$TR_Y$", str(tr[1])).\
            replace("$TL_X$", str(tl[0])).\
            replace("$TL_Y$", str(tl[1])).\
            replace("$BR_X$", str(br[0])).\
            replace("$BR_Y$", str(br[1])).\
            replace("$BL_X$", str(bl[0])).\
            replace("$BL_Y$", str(bl[1])).\
            replace("$SZ$", str(field_sz))


def create_qr(id, tl,tr,bl,br):
    return qrcode.replace("$ID$", id).\
            replace("$TR_X$", str(tr[0])).\
            replace("$TR_Y$", str(tr[1])).\
            replace("$TL_X$", str(tl[0])).\
            replace("$TL_Y$", str(tl[1])).\
            replace("$BR_X$", str(br[0])).\
            replace("$BR_Y$", str(br[1])).\
            replace("$BL_X$", str(bl[0])).\
            replace("$BL_Y$", str(bl[1]))

#r1 = create_resp("Yes", 100, 200)
#r2 = create_resp("N0", 200, 200)
#g1 = create_group("ROBUS_TEAM1", (r1,r2))
#print(create_template((g1,g1)))