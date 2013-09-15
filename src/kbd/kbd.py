#!/usr/bin/python2

# KBD - A simple keyboard backlight daemon to control keyboard backlight with a web service
# Copyright (C) 2013  Claus Matzinger
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from SocketServer import BaseRequestHandler, TCPServer
import argparse
import sys

BACKLIGHT_FILE = 0
PORT = 1
OFF = 2
MAX = 3

DEFAULT_PORT = 19999
DEFAULT_BACKLIGHT_FILE = "/sys/class/leds/smc::kbd_backlight/brightness"

DEFAULT_OFF_VALUE = 0
DEFAULT_MAX_VALUE = 99

OPTIONS = None

parser = argparse.ArgumentParser(description='Simple keyboard backlight daemon - control your keyboard backlight with a web service.')
parser.add_argument('-f', '--backlight_file', 
                   dest='control_file', 
                   default=DEFAULT_BACKLIGHT_FILE,
                   help='The file interface controlling the current backlight value.')
                   

parser.add_argument('-p', '--port', 
                   dest='port', 
                   type=int,
                   default=DEFAULT_PORT,
                   help='The port to listen to. (default: %d)' % DEFAULT_PORT)
                   

parser.add_argument('-m', '--max', 
                   dest='max', 
                   type=int,
                   default=DEFAULT_MAX_VALUE,
                   help='The maximum value to set the backlight to. (default: %d)' % DEFAULT_MAX_VALUE)
           


def set_keyboard_backlight(value):
  """ Writes the passed value to the file """
  
  try:
    with open(OPTIONS[BACKLIGHT_FILE], "w+") as backlight:
      backlight.write(str(value))
  except IOError as ioe:
    print >> sys.stderr, ioe  

class BacklightHandler(BaseRequestHandler):
  """ Handles incoming values (max. 4 bytes) """

  def handle(self):
    try:
      value = int(self.request.recv(2))
    except:
      value = OPTIONS[OFF]
    finally:
      self.request.close()

    if value < OPTIONS[OFF]:
      value = OPTIONS[OFF]
    elif value > OPTIONS[MAX]:
      value = OPTIONS[MAX]
      
    set_keyboard_backlight(value) 

def run(arguments):
  global OPTIONS
  
  args = parser.parse_args(arguments)
  OPTIONS = (args.control_file, args.port, DEFAULT_OFF_VALUE, args.max)
  server = None
  try: 
    server = TCPServer(('localhost', OPTIONS[PORT]), BacklightHandler )
    server.serve_forever()
  except Exception as ex: 
    print >> sys.stderr, ex
  finally:
    print "Shutting down ..."
    if server: server.shutdown()

