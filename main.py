
def on_received_string(receivedString):
    if receivedString == "FA":
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.GREEN)
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
        """)
        MoveForward(fullmove)
    elif receivedString == "BA":
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.YELLOW)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.YELLOW)
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
        """)
        MoveBackward(fullmove)
    elif receivedString == "LA":
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)
        basic.show_leds("""
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
        """)
        TurnLeft(quarterTurn)
    elif receivedString == "RA":
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.GREEN)
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
        """)
        TurnRight(quarterTurn)
    elif receivedString == "slowForward":
        MoveForward(smallmove)
    elif receivedString == "slowBackward":
        MoveBackward(smallmove)
    elif receivedString == "oneDegreeLeft":
        TurnLeft(smallmove)
    elif receivedString == "oneDegreeRight":
        TurnRight(smallmove)
    else:
        pass
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    basic.show_leds("""
        # . . . #
        . # # # .
        . # # . .
        . # . . .
        . . . . .
    """)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.RED)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.RED)
radio.on_received_string(on_received_string)

def on_received_value(name, value):
    if name == "F":
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, Math.map(value, 550, 1023, 10, 255))
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.GREEN)
        basic.show_leds("""
            . . # . .
            . # . # .
            # . # . #
            . . # . .
            . . # . .
        """)
    elif name == "B":
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CCW, Math.map(value, 1, 540, 255, 10))
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.BLUE)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.BLUE)
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # . # .
            . . # . .
        """)
    elif name == "L":
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, Math.map(value, 1, 450, 255, 40))
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, 20)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)
        basic.show_leds("""
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
        """)
    elif name == "R":
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, Math.map(value, 550, 1023, 40, 255))
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, 20)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.GREEN)
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
        """)
radio.on_received_value(on_received_value)

def TurnLeft(num: number):
    DFRobotMaqueenPlus.clear_distance(Motors.ALL)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, turnSpeed)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, turnSpeed)
    while abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M2))) < num or abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M1))) < num:
        pass

def TurnRight(num2: number):
    DFRobotMaqueenPlus.clear_distance(Motors.ALL)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, turnSpeed)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, turnSpeed)
    while abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M2))) < num2 or abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M1))) < num2:
        pass

def MoveBackward(num3: number):
    DFRobotMaqueenPlus.clear_distance(Motors.ALL)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, basespeed)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, basespeed)
    while abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M2))) < num3 or abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M1))) < num3:
        pass

def MoveForward(num4: number):
    DFRobotMaqueenPlus.clear_distance(Motors.ALL)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, basespeed)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, basespeed)
    while abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M2))) < num4 or abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M1))) < num4:
        pass

basespeed = 0
quarterTurn = 0
turnSpeed = 0
fullmove = 0
smallmove = 0
radio.set_group(1)

basespeed = 50
turnSpeed = 50

quarterTurn = 0.35
fullmove = 0.75
smallmove = 0.01

def on_forever():
    pass

basic.forever(on_forever)
