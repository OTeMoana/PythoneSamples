import math
import os
import webbrowser

# кілька констант, формула, вивід синусів і косинусів, запис в файл
# ідея я можу описати програмно кут і силу натиску, просто ввівши дані, а далі корекція, на мене
# на мене працюватиме техніка, хоча рахувати так само потрібно, розганяти процеси, рухайся
# у рваному ритмі
# я можу розрахувати час падіння снарядуу, відповідно від цього можна буде утворювати свою систему часу


class tanki:

    def __init__(self, v , alfa, height):
        self.v = v
        self.alfa = alfa * 2 * math.pi / 360
        self.alfa1 = alfa
        self.height = height
        self.sin = math.sin(self.alfa)
        self.cos = math.cos(self.alfa)
        self.g = 9.82


    def fly_time(self):


        vH = self.sin * self.v
        t = vH / self.g # двійка добавляється пізніше, це питання часу
        l = self.cos * self.v * t
        self.t = t
        self.l = l




    def show_sin_cos(self):
        print(f"косинус: {self.cos:4.2f}")
        print(f"синус: {self.sin:4.2f}")


    def writing(self, path):
        #що мені потрібно, взаємозв'язок кута до дистанції, можна й в графік
        if not os.path.isfile(path):
            fileto = open(path, "w", encoding = "utf-8")
        else:
            fileto = open(path, "a", encoding = "utf-8")

        t = math.sin(self.alfa) * self.v / self.g

        compare = math.cos(self.alfa  - 2 * math.pi / 360) * self.v * t

        #fileto.write(f"v = {self.v}     vH sin = {self.sin}     v cos = {self.cos}      height = {self.height}")
        difference = compare - self.l
        if difference == 0:
            fileto.write(
                f"l = {self.l:4.2f}       df = no difference       \n")
        else:
            df_perc =  difference / compare * 100
            fileto.write(f"l = {self.l:4.2f}     previous = {compare:4.2f}       df = {difference:4.2f}       df_perc = {df_perc:4.2f}       "
                         f"t = {self.t:4.2f}        alpha = {self.alfa1:4.2f}        \n")


        fileto.close()


    # оцей метод зробити класовим або статичним
    def writing2(self, v, alfa):

        t = v * math.sin(alfa * 2 * math.pi / 360) / self.g
        l = v * math.cos * t


        return l, t, alfa


    def reading(self):
        return 0

fileto = open(r".\ballistics.txt", "w")
fileto.close()



for i in range(90):
    obj = tanki(87, i, 0)
    obj.fly_time()
    obj.writing(r".\ballistics.txt")

webbrowser.open(r".\ballistics.txt")
