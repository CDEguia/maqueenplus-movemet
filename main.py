LEFT = 0
RIGHT = 1
FORWARD = 2
BACKWARD = 3
DAMAGE = 4

convertedString = []

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
baseMove = 0.01
moveAmount = 0

def calculate_turn(receivedValue: number, type: number):
    
    moveAmount = (receivedValue*35)*baseMove

def calculate_squars(receicedValue: number):
    mo


def convert_received_string(received: str):
    for i in 2:
        convertedString.append(int(received[i]))

def on_received_string(receivedString):
    convert_received_string(receivedString)

    display_direction(convertedString[0])
    
    if convertedString[0] >= RIGHT :
        calculate_turn(convertedString[1])
    elif convertedString[1] >= BACKWARD :
        cal
    if convertedString[0] >= BACKWARD :
        MoveBackward(convertedString[1])
    elif convertedString[0] == FORWARD:
        MoveForward(convertedString[1])
    elif convertedString[0] == LEFT:
        turn_signal("left", 4)
        TurnLeft(convertedString[1])
    elif convertedString[0] == RIGHT:
        turn_signal("right", 4)
        TurnRight(convertedString[1])
#    elif receivedString == "littleForward":
#        MoveForward(smallmove)
#    elif receivedString == "littleBackward":
#        MoveBackward(smallmove)
#    elif receivedString == "littleLeft":
#        turn_signal("left", 2)
#        TurnLeft(smallmove)
#    elif receivedString == "littleRight":
#        turn_signal("right", 2)
#        TurnRight(smallmove)
    else:
        pass
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)

    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.WHITH)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.WHITH)
radio.on_received_string(on_received_string)

def on_received_value(name, value):
    if name == "forward":
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, Math.map(value, 550, 1023, 10, 255))
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.GREEN)
        display_direction("forward")
    elif name == "backward":
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CCW, Math.map(value, 1, 540, 255, 10))
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.BLUE)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.BLUE)
        display_direction("backward")
    elif name == "left":
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, Math.map(value, 1, 450, 255, 40))
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, 20)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)
        display_direction("left")
    elif name == "right":
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, Math.map(value, 550, 1023, 40, 255))
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, 20)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.GREEN)
        display_direction("right")
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

def turn_signal(direction: str, blink: number):
    lightToBlink = 2
    if direction == "left":
        lightToBlink = 1
    
    for i in range(blink):
        DFRobotMaqueenPlus.set_rgb_light(lightToBlink, Color.YELLOW)
        basic.pause(250)
        DFRobotMaqueenPlus.set_rgb_light(lightToBlink, Color.WHITH)
        basic.pause(250)



def display_direction(direction: str):
    if (direction == "oneForward") or (direction == "littleForward"):
        basic.show_leds("""
            . . # . .
            . # . # .
            # . # . #
            . . # . .
            . . # . .
        """)
    elif (direction == "oneBackward") or (direction == "littleBackward"):
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # . # .
            . . # . .
        """)
    elif (direction == "oneLeft") or (direction == "littleLeft"):
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
        """)
    elif (direction == "oneLeft") or (direction == "littleRight"):
        basic.show_leds("""
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
        """)
    else:
        basic.show_leds("""
            # . . . #
            . # # # .
            . # # . .
            . # . . .
            . . . . .
        """)

def on_forever():
    pass

basic.forever(on_forever)
