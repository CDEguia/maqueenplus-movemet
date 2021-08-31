radio.onReceivedString(function (receivedString) {
    if (receivedString == "FA") {
        for (let index = 0; index < 2; index++) {
            DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, 25)
            basic.pause(500)
            DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.GREEN)
            DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.GREEN)
            basic.showLeds(`
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
                `)
        }
    } else if (receivedString == "BA") {
        for (let index = 0; index < 2; index++) {
            DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CCW, 100)
            DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.YELLOW)
            DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.YELLOW)
            basic.showLeds(`
                . . # . .
                . . # . .
                # . # . #
                . # # # .
                . . # . .
                `)
        }
    } else if (receivedString == "LA") {
        DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, 20)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.GREEN)
        basic.showLeds(`
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
            `)
    } else if (receivedString == "RA") {
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.GREEN)
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
            `)
        TurnRight()
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
function TurnRight () {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, 65)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, 65)
    while (DFRobotMaqueenPlus.readeDistance(Motors1.M1) == 0 && DFRobotMaqueenPlus.readeDistance(Motors1.M1) == 0) {
    	
    }
}
radio.setGroup(1)
basic.forever(function () {
	
})
