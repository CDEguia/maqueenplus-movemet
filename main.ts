function TurnLeft (num: number) {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, 55)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, 55)
    while (Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M2))) < num || Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M1))) < num) {
    	
    }
}
radio.onReceivedString(function (receivedString) {
    if (receivedString == "FA") {
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.GREEN)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.GREEN)
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
        MoveForward(1)
    } else if (receivedString == "BA") {
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.YELLOW)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.YELLOW)
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
        MoveBackward(1)
    } else if (receivedString == "LA") {
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.GREEN)
        basic.showLeds(`
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
            `)
        TurnLeft(_90degrees)
    } else if (receivedString == "RA") {
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.GREEN)
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
            `)
        TurnRight(1)
    } else if (receivedString == "slowForward") {
        MoveForward(0.05)
    } else if (receivedString == "slowBackward") {
        MoveBackward(0.05)
    } else if (receivedString == "oneDegreeLeft") {
        TurnLeft(0.02)
    } else if (receivedString == "oneDegreeRight") {
        TurnRight(0.02)
    } else {
    	
    }
    DFRobotMaqueenPlus.mototStop(Motors.ALL)
    basic.showIcon(IconNames.No)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.RED)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.RED)
})
radio.onReceivedValue(function (name, value) {
    if (name == "F") {
        DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, Math.map(value, 550, 1023, 10, 255))
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.GREEN)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.GREEN)
        basic.showLeds(`
            . . # . .
            . # . # .
            # . # . #
            . . # . .
            . . # . .
            `)
    } else if (name == "B") {
        DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CCW, Math.map(value, 1, 540, 255, 10))
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.BLUE)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.BLUE)
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # . # .
            . . # . .
            `)
    } else if (name == "L") {
        DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, Math.map(value, 1, 450, 255, 40))
        DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, 20)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.GREEN)
        basic.showLeds(`
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
            `)
    } else if (name == "R") {
        DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, Math.map(value, 550, 1023, 40, 255))
        DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, 20)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.GREEN)
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
            `)
    }
})
function TurnRight (num: number) {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, 55)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, 55)
    while (Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M2))) < num || Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M1))) < num) {
    	
    }
}
function MoveBackward (num: number) {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, basespeed)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, basespeed)
    while (Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M2))) < num || Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M1))) < num) {
    	
    }
}
function MoveForward (num: number) {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, basespeed)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, basespeed)
    while (Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M2))) < num || Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M1))) < num) {
    	
    }
}
let basespeed = 0
let _90degrees = 0
radio.setGroup(1)
_90degrees = 0.35
let trim = 0
basespeed = 55
basic.forever(function () {
	
})
