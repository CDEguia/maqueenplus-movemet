radio.onReceivedString(function on_received_string(receivedString: string) {
    if (receivedString == "oneForward") {
        display_direction("forward")
        MoveForward(fullmove)
    } else if (receivedString == "oneBackward") {
        display_direction("backward")
        MoveBackward(fullmove)
    } else if (receivedString == "oneLeft") {
        display_direction("left")
        turn_signal("left", 4)
        TurnLeft(quarterTurn)
    } else if (receivedString == "oneRight") {
        display_direction("right")
        turn_signal("right", 4)
        TurnRight(quarterTurn)
    } else if (receivedString == "littleForward") {
        display_direction("forward")
        MoveForward(smallmove)
    } else if (receivedString == "littleBackward") {
        display_direction("backward")
        MoveBackward(smallmove)
    } else if (receivedString == "littleLeft") {
        display_direction("left")
        turn_signal("left", 2)
        TurnLeft(smallmove)
    } else if (receivedString == "littleRight") {
        display_direction("right")
        turn_signal("right", 2)
        TurnRight(smallmove)
    } else {
        
    }
    
    DFRobotMaqueenPlus.mototStop(Motors.ALL)
    basic.showLeds(`
        # . . . #
        . # # # .
        . # # . .
        . # . . .
        . . . . .
    `)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.WHITH)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.WHITH)
})
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    if (name == "forward") {
        DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, Math.map(value, 550, 1023, 10, 255))
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.GREEN)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.GREEN)
        display_direction("forward")
    } else if (name == "backward") {
        DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CCW, Math.map(value, 1, 540, 255, 10))
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.BLUE)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.BLUE)
        display_direction("backward")
    } else if (name == "left") {
        DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, Math.map(value, 1, 450, 255, 40))
        DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, 20)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.GREEN)
        display_direction("left")
    } else if (name == "right") {
        DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, Math.map(value, 550, 1023, 40, 255))
        DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, 20)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.GREEN)
        display_direction("right")
    }
    
})
function TurnLeft(num: number) {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, turnSpeed)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, turnSpeed)
    while (Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M2))) < num || Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M1))) < num) {
        
    }
}

function TurnRight(num2: number) {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, turnSpeed)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, turnSpeed)
    while (Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M2))) < num2 || Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M1))) < num2) {
        
    }
}

function MoveBackward(num3: number) {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, basespeed)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, basespeed)
    while (Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M2))) < num3 || Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M1))) < num3) {
        
    }
}

function MoveForward(num4: number) {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, basespeed)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, basespeed)
    while (Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M2))) < num4 || Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M1))) < num4) {
        
    }
}

function turn_signal(direction: string, blink: number) {
    let lightToBlink = 2
    if (direction == "left") {
        lightToBlink = 1
    }
    
    for (let i = 0; i < blink; i++) {
        DFRobotMaqueenPlus.setRGBLight(lightToBlink, Color.YELLOW)
        basic.pause(250)
        DFRobotMaqueenPlus.setRGBLight(lightToBlink, Color.WHITH)
        basic.pause(250)
    }
}

function display_direction(direction: string) {
    if (direction == "forward") {
        basic.showLeds(`
            . . # . .
            . # . # .
            # . # . #
            . . # . .
            . . # . .
        `)
    } else if (direction == "backward") {
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # . # .
            . . # . .
        `)
    } else if (direction == "left") {
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
        `)
    } else {
        basic.showLeds(`
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
        `)
    }
    
}

let basespeed = 0
let quarterTurn = 0
let turnSpeed = 0
let fullmove = 0
let smallmove = 0
radio.setGroup(1)
basespeed = 50
turnSpeed = 50
quarterTurn = 0.35
fullmove = 0.75
smallmove = 0.01
basic.forever(function on_forever() {
    
})
