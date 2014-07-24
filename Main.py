# -*- coding: utf-8 -*-
import Object
import MapObject
import Player
# import Client
# import pickle as pick

from sys import path as syspath
syspath.append('.//libtcod-1.5.1')
import libtcodpy as libtcod

#FOV information
FOV_ALGO = 0  # default FOV algorithm
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 8

#Complete Window size
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
Limit_Fps = 30

#Map window in console window
Map_Width = 80
Map_Height = 45

Map = MapObject.Map(80, 45, 'smalldungeon')

#Update FOV Map with lightable tiles
fov_map = libtcod.map_new(Map_Width, Map_Height)
for y in range(Map_Height):
    for x in range(Map_Width):
        libtcod.map_set_properties(fov_map, x, y,
        not Map.mappedArea[x][y].block_sight, not Map.mappedArea[x][y].blocked)

#dungeon colors
color_dungeon_dark_wall = libtcod.Color(10, 0, 110)
color_dungeon_dark_floor = libtcod.Color(110, 110, 110)
color_dungeon_light_wall = libtcod.Color(20, 0, 150)
color_dungeon_light_floor = libtcod.Color(150, 150, 150)

#cave colors
color_cave_dark_wall = libtcod.Color(100, 80, 80)
color_cave_dark_floor = libtcod.Color(110, 110, 110)
color_cave_light_wall = libtcod.Color(140, 90, 80)
color_cave_light_floor = libtcod.Color(150, 150, 150)
color_cave_dark_water = libtcod.Color(10, 110, 170)
color_cave_light_water = libtcod.Color(20, 140, 200)


libtcod.console_set_custom_font('dejavu16x16.png', libtcod.FONT_TYPE_GREYSCALE
| libtcod.FONT_LAYOUT_TCOD)

# Initialize the window
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Arrfia 2.0', False)

mapCon = libtcod.console_new(Map_Width, Map_Height)

libtcod.sys_set_fps(Limit_Fps)

(new_x, new_y) = Map.starting_point
player = Object.Object(new_x, new_y, '@', libtcod.white, True)
#npc = Object.Object(SCREEN_WIDTH / 2 - 5, SCREEN_HEIGHT / 2, '@', libtcod.yellow, mapCon, True)

objects = Map.entities
objects.append(player)

libtcod.map_compute_fov(fov_map, player.x, player.y, TORCH_RADIUS, FOV_LIGHT_WALLS, FOV_ALGO)

def player_input():
    x = 0
    y = 0

    key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)
    #movement keys
    if key.vk == libtcod.KEY_CHAR:
        fov_recompute = False
        if key.c == ord('w'):
            y -= 1
            fov_recompute = True
        elif key.c == ord('s'):
            y += 1
            fov_recompute = True
        elif key.c == ord('a'):
            x -= 1
            fov_recompute = True
        elif key.c == ord('d'):
            x += 1
            fov_recompute = True
        global mapCon
        player.clear(mapCon)
        global Map, objects
        player.move(x, y, Map, objects)
        # global client
        # try:
            # client.send(str(player.x))
        # except:
            # print("")
        if fov_recompute:
            #recompute FOV if needed (the player moved or something)
            fov_recompute = False
            libtcod.map_compute_fov(fov_map, player.x, player.y, TORCH_RADIUS, FOV_LIGHT_WALLS, FOV_ALGO)

    if key.vk == libtcod.KEY_CHAR:
        if key.c == ord('c'):
            global Map
            for y in range(Map_Height):
                for x in range(Map_Width):
                    Map.mappedArea[x][y].explored = False
            Map = MapObject.Map(80, 45, 'smalldungeon')
            (new_x, new_y) = Map.rooms[0].center()
            player.put(new_x, new_y)
            global fov_map
            fov_map = libtcod.map_new(Map_Width, Map_Height)
            for y in range(Map_Height):
                for x in range(Map_Width):
                    libtcod.map_set_properties(fov_map, x, y,
                    not Map.mappedArea[x][y].block_sight, not Map.mappedArea[x][y].blocked)
            libtcod.map_compute_fov(fov_map, player.x, player.y, TORCH_RADIUS, FOV_LIGHT_WALLS, FOV_ALGO)
    elif key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  # exit game


def HandleObjects():
    global fov_map, mapCon
    for object in objects:
        object.clear(mapCon)
        #object.
    for object in objects:
        object.draw(fov_map, mapCon)


def RenderMap():
    #go through all tiles, and set their background color according to the FOV
    for y in range(Map_Height):
        for x in range(Map_Width):
            visible = libtcod.map_is_in_fov(fov_map, x, y)
            wall = Map.mappedArea[x][y].block_sight
            if "dungeon" in Map.mapType:
                if not visible:
                    #it's out of the player's FOV
                    if Map.mappedArea[x][y].explored:
                        if wall:
                            libtcod.console_set_char_background(mapCon, x, y, color_dungeon_dark_wall, libtcod.BKGND_SET )
                        else:
                            libtcod.console_set_char_background(mapCon, x, y, color_dungeon_dark_floor, libtcod.BKGND_SET )
                else:
                    #it's visible
                    if wall:
                        libtcod.console_set_char_background(mapCon, x, y, color_dungeon_light_wall, libtcod.BKGND_SET )
                    else:
                        libtcod.console_set_char_background(mapCon, x, y, color_dungeon_light_floor, libtcod.BKGND_SET )
                    Map.mappedArea[x][y].explored = True
            if "cave" in Map.mapType:
                if not visible:
                    tile = Map.mappedArea[x][y]
                    #USE THIS TO SEE WHOLE MAP
                    #tile.explored = True
                    #it's out of the player's FOV
                    if tile.explored:
                        if wall:
                            libtcod.console_set_char_background(mapCon, x, y, color_cave_dark_wall, libtcod.BKGND_SET )
                        else:
                            if not tile.tileType is None:
                                if tile.tileType == "water":
                                    libtcod.console_set_char_background(mapCon, x, y, color_cave_dark_water, libtcod.BKGND_SET )
                            else:
                                libtcod.console_set_char_background(mapCon, x, y, color_cave_dark_floor, libtcod.BKGND_SET )
                else:
                    tile = Map.mappedArea[x][y]
                    #it's visible
                    if wall:
                        libtcod.console_set_char_background(mapCon, x, y, color_cave_light_wall, libtcod.BKGND_SET )
                    else:
                        if not tile.tileType is None:
                            if tile.tileType == "water":
                                libtcod.console_set_char_background(mapCon, x, y, color_cave_light_water, libtcod.BKGND_SET )
                        else:
                            libtcod.console_set_char_background(mapCon, x, y, color_cave_light_floor, libtcod.BKGND_SET )
                    tile.explored = True
def RenderAll():
    HandleObjects()
    RenderMap()
    libtcod.console_blit(mapCon, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

# client = Client.Client("localhost")


# Game Loop
while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(mapCon, libtcod.white)

    RenderAll()
    libtcod.console_flush()

    exit = player_input()
    if exit:
        break
