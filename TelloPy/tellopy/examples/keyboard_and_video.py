"""
tellopy sample using keyboard and video player

Requires mplayer to record/save video.


Controls:
- tab to lift off
- WASD to move the drone
- space/shift to ascend/descent slowly
- Q/E to yaw slowly
- arrow keys to ascend, descend, or yaw quickly
- backspace to land, or P to palm-land
- enter to take a picture
- R to start recording video, R again to stop recording
  (video and photos will be saved to a timestamped file in ~/Pictures/)
- Z to toggle camera zoom state
  (zoomed-in widescreen or high FOV 4:3)
"""

import time
import sys
import tellopy
import pygame
import pygame.display
import pygame.key
import pygame.locals
import pygame.font
import os
import datetime
from subprocess import Popen, PIPE
# from tellopy import logger

# log = tellopy.logger.Logger('TelloUI')

def back_left_down(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(speed/ 1.414*1.207)
    getattr(drone, 'left')(speed/ 1.414*1.102)
    getattr(drone, 'right')(0)
    drone.up(0)
    drone.down(speed*2)


def back_left(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(speed/ 1.414*1.207)
    getattr(drone, 'left')(speed/ 1.414*1.102)
    getattr(drone, 'right')(0)
    drone.up(0)
    drone.down(0)

def back_left_up(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(speed/ 1.414*1.207)
    getattr(drone, 'left')(speed/ 1.414*1.102)
    getattr(drone, 'right')(0)
    drone.up(speed*2)
    drone.down(0)


def back_down(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(speed*1.207)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(0)
    drone.up(0)
    drone.down(speed*2)


def back(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(speed*1.207)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(0)
    drone.up(0)
    drone.down(0)


def back_up(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(speed*1.207)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(0)
    drone.up(speed*2)
    drone.down(0)


def back_right_down(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(speed/ 1.414*1.207)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(speed/ 1.414*1.102)
    drone.up(0)
    drone.down(speed*2)


def back_right(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(speed/ 1.414*1.207)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(speed/ 1.414*1.102)
    drone.up(0)
    drone.down(0)


def back_right_up(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(speed/ 1.414*1.207)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(speed/ 1.414*1.102)
    drone.up(speed*2)
    drone.down(0)


def left_down(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(speed*1.102)
    getattr(drone, 'right')(0)
    drone.up(0)
    drone.down(speed*2)


def left(drone, speed):
    # getattr(drone, 'forward')(0)
    # getattr(drone, 'backward')(0)
    getattr(drone, 'left')(speed*1.102)
    # getattr(drone, 'right')(0)
    # drone.up(0)
    # drone.down(0)


def left_up(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(speed*1.102)
    getattr(drone, 'right')(0)
    drone.up(speed*2)
    drone.down(0)


def down(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(0)
    drone.up(0)
    drone.down(speed*2)


def stop(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(0)
    drone.up(0)
    drone.down(0)
    drone.land()


def up(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(0)
    drone.up(speed*2)
    drone.down(0)


def right_down(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(speed*1.102)
    drone.up(0)
    drone.down(speed*2)


def right(drone, speed):
    # getattr(drone, 'forward')(0)
    # getattr(drone, 'backward')(0)
    # getattr(drone, 'left')(0)
    getattr(drone, 'right')(speed*1.102)
    # drone.up(0)
    # drone.down(0)


def right_up(drone, speed):
    getattr(drone, 'forward')(0)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(speed*1.102)
    drone.up(speed*2)
    drone.down(0)


def fw_left_down(drone, speed):
    getattr(drone, 'forward')(speed/ 1.414*1.207)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(speed/ 1.414*1.102)
    getattr(drone, 'right')(0)
    drone.up(0)
    drone.down(speed*2)


def fw_left(drone, speed):
    getattr(drone, 'forward')(speed/ 1.414*1.207)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(speed/ 1.414*1.102)
    getattr(drone, 'right')(0)
    drone.up(0)
    drone.down(0)


def fw_left_up(drone, speed):
    getattr(drone, 'forward')(speed/ 1.414*1.207)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(speed/ 1.414*1.102)
    getattr(drone, 'right')(0)
    drone.up(speed*2)
    drone.down(0)


def fw_down(drone, speed):
    getattr(drone, 'forward')(speed*1.207)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(0)
    drone.up(0)
    drone.down(speed*2)


def fw(drone, speed):
    getattr(drone, 'forward')(speed*1.207)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(0)
    drone.up(0)
    drone.down(0)


def fw_up(drone, speed):
    getattr(drone, 'forward')(speed*1.207)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(0)
    drone.up(speed*2)
    drone.down(0)


def fw_right_down(drone, speed):
    getattr(drone, 'forward')(speed/ 1.414*1.207)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(speed/ 1.414*1.102)
    drone.up(0)
    drone.down(speed*2)


def fw_right(drone, speed):
    getattr(drone, 'forward')(speed/ 1.414*1.207)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(speed/ 1.414*1.102)
    drone.up(0)
    drone.down(0)


def fw_right_up(drone, speed):
    getattr(drone, 'forward')(speed/ 1.414*1.207)
    getattr(drone, 'backward')(0)
    getattr(drone, 'left')(0)
    getattr(drone, 'right')(speed/ 1.414*1.102)
    drone.up(speed*2)
    drone.down(0)


command_list = [[[back_left_down,  back_left,  back_left_up],
                 [back_down,       back,       back_up],
                 [back_right_down, back_right, back_right_up]],
                [[left_down,       left,       left_up],
                 [down,            stop,       up],
                 [right_down,      right,      right_up]],
                [[fw_left_down,    fw_left,    fw_left_up],
                 [fw_down,         fw,         fw_up],
                 [fw_right_down,   fw_right,   fw_right_up]]]

direc = [(1, 2, 1), (1, 0, 1), (1, 2, 1)]

prev_flight_data = None
video_player = None
video_recorder = None
font = None
wid = None
date_fmt = '%Y-%m-%d_%H%M%S'

def toggle_recording(drone, speed):
    global video_recorder
    global date_fmt
    if speed == 0:
        return

    if video_recorder:
        # already recording, so stop
        video_recorder.stdin.close()
        status_print('Video saved to %s' % video_recorder.video_filename)
        video_recorder = None
        return

    # start a new recording
    filename = '%s/Pictures/tello-%s.mp4' % (os.getenv('HOME'),
                                             datetime.datetime.now().strftime(date_fmt))
    video_recorder = Popen([
        'mencoder', '-', '-vc', 'x264', '-fps', '30', '-ovc', 'copy',
        '-of', 'lavf', '-lavfopts', 'format=mp4',
        # '-ffourcc', 'avc1',
        # '-really-quiet',
        '-o', filename,
    ], stdin=PIPE)
    video_recorder.video_filename = filename
    status_print('Recording video to %s' % filename)

def take_picture(drone, speed):
    if speed == 0:
        return
    drone.take_picture()

def palm_land(drone, speed):
    if speed == 0:
        return
    drone.palm_land()

def toggle_zoom(drone, speed):
    # In "video" mode the drone sends 1280x720 frames.
    # In "photo" mode it sends 2592x1936 (952x720) frames.
    # The video will always be centered in the window.
    # In photo mode, if we keep the window at 1280x720 that gives us ~160px on
    # each side for status information, which is ample.
    # Video mode is harder because then we need to abandon the 16:9 display size
    # if we want to put the HUD next to the video.
    if speed == 0:
        return
    drone.set_video_mode(not drone.zoom)
    pygame.display.get_surface().fill((0,0,0))
    pygame.display.flip()

controls = {
    'w': 'forward',
    's': 'backward',
    'a': 'left',
    'd': 'right',
    'space': 'up',
    'left shift': 'down',
    'right shift': 'down',
    'q': 'counter_clockwise',
    'e': 'clockwise',
    # arrow keys for fast turns and altitude adjustments
    'left': lambda drone, speed: drone.counter_clockwise(speed*2),
    'right': lambda drone, speed: drone.clockwise(speed*2),
    'up': lambda drone, speed: drone.up(speed*2),
    'down': lambda drone, speed: drone.down(speed*2),
    'tab': lambda drone, speed: drone.takeoff(),
    'backspace': lambda drone, speed: drone.land(),
    'p': palm_land,
    'r': toggle_recording,
    'z': toggle_zoom,
    'enter': take_picture,
    'return': take_picture,
}

class FlightDataDisplay(object):
    # previous flight data value and surface to overlay
    _value = None
    _surface = None
    # function (drone, data) => new value
    # default is lambda drone,data: getattr(data, self._key)
    _update = None
    def __init__(self, key, format, colour=(255,255,255), update=None):
        self._key = key
        self._format = format
        self._colour = colour

        if update:
            self._update = update
        else:
            self._update = lambda drone,data: getattr(data, self._key)

    def update(self, drone, data):
        new_value = self._update(drone, data)
        if self._value != new_value:
            self._value = new_value
            self._surface = font.render(self._format % (new_value,), True, self._colour)
        return self._surface

def flight_data_mode(drone, *args):
    return (drone.zoom and "VID" or "PIC")

def flight_data_recording(*args):
    return (video_recorder and "REC 00:00" or "")  # TODO: duration of recording

def update_hud(hud, drone, flight_data):
    (w,h) = (158,0) # width available on side of screen in 4:3 mode
    blits = []
    for element in hud:
        surface = element.update(drone, flight_data)
        if surface is None:
            continue
        blits += [(surface, (0, h))]
        # w = max(w, surface.get_width())
        h += surface.get_height()
    h += 64  # add some padding
    overlay = pygame.Surface((w, h), pygame.SRCALPHA)
    overlay.fill((0,0,0)) # remove for mplayer overlay mode
    for blit in blits:
        overlay.blit(*blit)
    pygame.display.get_surface().blit(overlay, (0,0))
    pygame.display.update(overlay.get_rect())

def status_print(text):
    pygame.display.set_caption(text)

hud = [
    FlightDataDisplay('height', 'ALT %3d'),
    FlightDataDisplay('ground_speed', 'SPD %3d'),
    FlightDataDisplay('battery_percentage', 'BAT %3d%%'),
    FlightDataDisplay('wifi_strength', 'NET %3d%%'),
    FlightDataDisplay(None, 'CAM %s', update=flight_data_mode),
    FlightDataDisplay(None, '%s', colour=(255, 0, 0), update=flight_data_recording),
]

def flightDataHandler(event, sender, data):
    global prev_flight_data
    text = str(data)
    if prev_flight_data != text:
        update_hud(hud, sender, data)
        prev_flight_data = text

def videoFrameHandler(event, sender, data):
    global video_player
    global video_recorder
    if video_player is None:
        cmd = [ 'mplayer', '-fps', '35', '-really-quiet' ]
        if wid is not None:
            cmd = cmd + [ '-wid', str(wid) ]
        video_player = Popen(cmd + ['-'], stdin=PIPE)

    try:
        video_player.stdin.write(data)
    except IOError as err:
        status_print(str(err))
        video_player = None

    try:
        if video_recorder:
            video_recorder.stdin.write(data)
    except IOError as err:
        status_print(str(err))
        video_recorder = None

def handleFileReceived(event, sender, data):
    global date_fmt
    # Create a file in ~/Pictures/ to receive image data from the drone.
    path = '%s/Pictures/tello-%s.jpeg' % (
        os.getenv('HOME'),
        datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S'))
    with open(path, 'wb') as fd:
        fd.write(data)
    status_print('Saved photo to %s' % path)

def main():
    pygame.init()
    pygame.display.init()
    pygame.display.set_mode((1280, 720))
    pygame.font.init()

    global font
    font = pygame.font.SysFont("dejavusansmono", 32)

    global wid
    if 'window' in pygame.display.get_wm_info():
        wid = pygame.display.get_wm_info()['window']
    print("Tello video WID:", wid)

    drone = tellopy.Tello()
    drone.connect()
    drone.start_video()
    drone.subscribe(drone.EVENT_FLIGHT_DATA, flightDataHandler)
    drone.subscribe(drone.EVENT_VIDEO_FRAME, videoFrameHandler)
    drone.subscribe(drone.EVENT_FILE_RECEIVED, handleFileReceived)
    speed = 30

    drone.takeoff()
    time.sleep(0.5)
    print('hello?')
    try:
        # for i in range(1):  # loop with pygame.event.get() is too mush tight w/o some sleep
        for x, y, z in direc:
            print(x, y, z)
            command = command_list[x][y][z]
            for i in range(1):
                # WASD for movement
                # print('+' + command)
                # keyname = command
                # if keyname == 'escape':
                #     drone.quit()
                #     exit(0)
                # if keyname in controls:
                #     key_handler = controls[keyname]
                #     if type(key_handler) == str:
                #         getattr(drone, key_handler)(speed)
                #     else:
                #         key_handler(drone, speed)
                command(drone, 10)
                time.sleep(1)
        drone.land()
    except Exception as e:
        print(e)
        drone.land()
    finally:
        print('Shutting down connection to drone...')
        if video_recorder:
            toggle_recording(drone, 1)
        drone.quit()
        exit(1)

if __name__ == '__main__':
    main()
