import libtcodpy as libtcod
import random
import sys

Game_Screen_Width = 100#100#128
Game_Screen_Height = 100#75#96

Message_Screen_Width = Game_Screen_Width - 2
Message_Screen_Height = Game_Screen_Height / 4
Message_V_Pos = Game_Screen_Height - Message_Screen_Height - 1

Stat_Screen_Width = Game_Screen_Width / 4
Stat_Screen_Height = Game_Screen_Height - Message_Screen_Height - 2
Stat_H_Pos = Game_Screen_Width - Stat_Screen_Width - 1

Game_Console_Width = Game_Screen_Width - Stat_Screen_Width
Game_Console_Height = Game_Screen_Height - Message_Screen_Height -2

Inventory_Width = Game_Screen_Width - Stat_Screen_Width  -2
Inventory_Height = Game_Screen_Height - Message_Screen_Height -2

##Cavern Generator based on Cellular Automata
##Needs boundry checking for checking the edge cells
class GenCave:
    def __init__(self,size=100):
        self.FLOOR = " "
        self.WALL  = "#"
        self.size = size
        self.map_arr = [["#" for col in range(self.size)] for row in range(self.size)]
        self.temp_map = [["#" for col in range(self.size)] for row in range(self.size)]
        self.setup()
        ##Run the whole generator aside from the setup 5 times to get natural looking caves
        for i in range(5):
            self.automate()
            self.map_arr = self.temp_map
    def setup(self):
        ##Fill the map with ground at the specified percentage
        ##Lower numbers make more open caves, while higher numbers result in more closed in, but more un connected 'rooms'
        ##40% is a decent percentage
        for x in range(0,self.size-0):
            for y in range(0,self.size-0):
                r = random.randrange(0,100)
                if r > 40:
                    self.map_arr[x][y] = self.FLOOR
                else:
                    self.map_arr[x][y] = self.WALL

    def automate(self):
        ##Go through each cell to see if it needs to be transformed
        for x in range(2,self.size-2):
            for y in range(2,self.size-2):
                cell = self.checkCell(x,y)
                #self.map_arr[x][y] = cell
                self.temp_map[x][y] = cell

    def checkCell(self,x,y):
        z = 0
        ##Check in a 3x3 area around the chosen cell
        for xx in range(0,3):
            for yy in range(0,3):
                if self.map_arr[x+xx-1][y+yy-1] is self.WALL: z+=1 ##Has an offset to get closer to the wall
        ##If there are 5 or more wall segments next to a piece of floor
        ##Turn it into a wall
        if self.map_arr[x][y] == self.FLOOR:
            if z >= 5:
                return self.WALL
            else:
                return self.FLOOR
        ##If there are 4 or more wall segments next to another wall
        ##Keep it a wall, otherwise turn it into floor
        if self.map_arr[x][y] == self.WALL:
            if z >= 4:
                return self.WALL
            else:
                return self.FLOOR


    def getMap(self):
        return self.map_arr

