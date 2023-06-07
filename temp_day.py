from PyQt5.QtWidgets import QApplication
from day_design import DayDesign
from day_design import DayDesign
import Retriving_Data

location = "delhi"

data = Retriving_Data.retrive_data(location)

if __name__ == '__main__':
    app = QApplication([])

    night_design = DayDesign()

    deg = data[2][1]

    if deg >= 337.5 or deg < 22.5:
        direction = "North"
    elif 22.5 <= deg < 67.5:
        direction = "Northeast"
    elif 67.5 <= deg < 112.5:
        direction = "East"
    elif 112.5 <= deg < 157.5:
        direction = "Southeast"
    elif 157.5 <= deg < 202.5:
        direction = "South"
    elif 202.5 <= deg < 247.5:
        direction = "Southwest"
    elif 247.5 <= deg < 292.5:
        direction = "West"
    else:
        direction = "Northwest"

    wind =  "\nWind speed : " +str(data[2][0]) +"mph "+ " \n" + "Direction :" + direction

    temp = "\n"+ str(data[1][0]) + "°F"
    temp_max = "MAX: " + str(data[1][1]) + "°F"
    temp_min = "MIN: " + str(data[1][2]) + "°F" +"\n"

    date = "\n"+str(data[3][0]) + "\n" + "sunrise: " + str(data[4][0]) + "\n" + "sunset: " + str(data[5][0]) +"\n"

    name = str(data[6][0]) + "\n" + str(data[3][1])[0:5]

    weth = "\n"+ data[0][0] + "\n" + data[0][1]
    window = night_design.dayinvoke(temp, temp_max, temp_min, name, date,wind,weth)

    def resizeEvent(event):
        night_design.label_temp.resizeEvent(event)

    window.resizeEvent = resizeEvent

    window.show()

    app.exec_()
