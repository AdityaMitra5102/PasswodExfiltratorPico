import usb_hid
import os

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time
# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)
time.sleep(3)
kbd.send(Keycode.LEFT_GUI, Keycode.R)
kbd.send(Keycode.ENTER)
time.sleep(1)
kbd.send(Keycode.C)
kbd.send(Keycode.M)
kbd.send(Keycode.D)
kbd.send(Keycode.ENTER)
time.sleep(1)
kbd.send(Keycode.P)
kbd.send(Keycode.Y)
kbd.send(Keycode.T)
kbd.send(Keycode.H)
kbd.send(Keycode.O)
kbd.send(Keycode.N)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.MINUS)
kbd.send(Keycode.C)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.SHIFT, Keycode.QUOTE)
kbd.send(Keycode.I)
kbd.send(Keycode.M)
kbd.send(Keycode.P)
kbd.send(Keycode.O)
kbd.send(Keycode.R)
kbd.send(Keycode.T)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.O)
kbd.send(Keycode.S)
kbd.send(Keycode.COMMA)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.S)
kbd.send(Keycode.U)
kbd.send(Keycode.B)
kbd.send(Keycode.P)
kbd.send(Keycode.R)
kbd.send(Keycode.O)
kbd.send(Keycode.C)
kbd.send(Keycode.E)
kbd.send(Keycode.S)
kbd.send(Keycode.S)
kbd.send(Keycode.COMMA)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.J)
kbd.send(Keycode.S)
kbd.send(Keycode.O)
kbd.send(Keycode.N)
kbd.send(Keycode.COMMA)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.T)
kbd.send(Keycode.E)
kbd.send(Keycode.R)
kbd.send(Keycode.T)
kbd.send(Keycode.O)
kbd.send(Keycode.O)
kbd.send(Keycode.L)
kbd.send(Keycode.S)
kbd.send(Keycode.COMMA)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.U)
kbd.send(Keycode.R)
kbd.send(Keycode.L)
kbd.send(Keycode.L)
kbd.send(Keycode.I)
kbd.send(Keycode.B)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.P)
kbd.send(Keycode.A)
kbd.send(Keycode.R)
kbd.send(Keycode.S)
kbd.send(Keycode.E)
kbd.send(Keycode.SEMICOLON)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.O)
kbd.send(Keycode.S)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.S)
kbd.send(Keycode.Y)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.E)
kbd.send(Keycode.M)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.P)
kbd.send(Keycode.Y)
kbd.send(Keycode.T)
kbd.send(Keycode.H)
kbd.send(Keycode.O)
kbd.send(Keycode.N)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.MINUS)
kbd.send(Keycode.M)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.P)
kbd.send(Keycode.I)
kbd.send(Keycode.P)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.N)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.A)
kbd.send(Keycode.L)
kbd.send(Keycode.L)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.R)
kbd.send(Keycode.E)
kbd.send(Keycode.Q)
kbd.send(Keycode.U)
kbd.send(Keycode.E)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.S)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SEMICOLON)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.M)
kbd.send(Keycode.P)
kbd.send(Keycode.O)
kbd.send(Keycode.R)
kbd.send(Keycode.T)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.R)
kbd.send(Keycode.E)
kbd.send(Keycode.Q)
kbd.send(Keycode.U)
kbd.send(Keycode.E)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.S)
kbd.send(Keycode.SEMICOLON)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.R)
kbd.send(Keycode.E)
kbd.send(Keycode.Q)
kbd.send(Keycode.U)
kbd.send(Keycode.E)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.S)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.G)
kbd.send(Keycode.E)
kbd.send(Keycode.T)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.H)
kbd.send(Keycode.T)
kbd.send(Keycode.T)
kbd.send(Keycode.P)
kbd.send(Keycode.S)
kbd.send(Keycode.SHIFT, Keycode.SEMICOLON)
kbd.send(Keycode.FORWARD_SLASH)
kbd.send(Keycode.FORWARD_SLASH)
kbd.send(Keycode.A)
kbd.send(Keycode.P)
kbd.send(Keycode.I)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.T)
kbd.send(Keycode.E)
kbd.send(Keycode.L)
kbd.send(Keycode.E)
kbd.send(Keycode.G)
kbd.send(Keycode.R)
kbd.send(Keycode.A)
kbd.send(Keycode.M)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.O)
kbd.send(Keycode.R)
kbd.send(Keycode.G)
kbd.send(Keycode.FORWARD_SLASH)
kbd.send(Keycode.B)
kbd.send(Keycode.O)
kbd.send(Keycode.T)
kbd.send(Keycode.SIX)
kbd.send(Keycode.ZERO)
kbd.send(Keycode.FIVE)
kbd.send(Keycode.FOUR)
kbd.send(Keycode.TWO)
kbd.send(Keycode.ONE)
kbd.send(Keycode.FOUR)
kbd.send(Keycode.THREE)
kbd.send(Keycode.EIGHT)
kbd.send(Keycode.EIGHT)
kbd.send(Keycode.SHIFT, Keycode.SEMICOLON)
kbd.send(Keycode.SHIFT, Keycode.A)
kbd.send(Keycode.SHIFT, Keycode.A)
kbd.send(Keycode.SHIFT, Keycode.G)
kbd.send(Keycode.SHIFT, Keycode.H)
kbd.send(Keycode.T)
kbd.send(Keycode.SHIFT, Keycode.E)
kbd.send(Keycode.Z)
kbd.send(Keycode.U)
kbd.send(Keycode.G)
kbd.send(Keycode.T)
kbd.send(Keycode.SEVEN)
kbd.send(Keycode.SHIFT, Keycode.E)
kbd.send(Keycode.SHIFT, Keycode.P)
kbd.send(Keycode.V)
kbd.send(Keycode.J)
kbd.send(Keycode.SHIFT, Keycode.P)
kbd.send(Keycode.SHIFT, Keycode.I)
kbd.send(Keycode.SHIFT, Keycode.A)
kbd.send(Keycode.TWO)
kbd.send(Keycode.D)
kbd.send(Keycode.SHIFT, Keycode.B)
kbd.send(Keycode.ZERO)
kbd.send(Keycode.SHIFT, Keycode.E)
kbd.send(Keycode.SHIFT, Keycode.Y)
kbd.send(Keycode.SHIFT, Keycode.Z)
kbd.send(Keycode.SHIFT, Keycode.C)
kbd.send(Keycode.L)
kbd.send(Keycode.SHIFT, Keycode.D)
kbd.send(Keycode.S)
kbd.send(Keycode.C)
kbd.send(Keycode.SHIFT, Keycode.R)
kbd.send(Keycode.SHIFT, Keycode.N)
kbd.send(Keycode.SHIFT, Keycode.Y)
kbd.send(Keycode.NINE)
kbd.send(Keycode.K)
kbd.send(Keycode.FORWARD_SLASH)
kbd.send(Keycode.S)
kbd.send(Keycode.E)
kbd.send(Keycode.N)
kbd.send(Keycode.D)
kbd.send(Keycode.SHIFT, Keycode.M)
kbd.send(Keycode.E)
kbd.send(Keycode.S)
kbd.send(Keycode.S)
kbd.send(Keycode.A)
kbd.send(Keycode.G)
kbd.send(Keycode.E)
kbd.send(Keycode.SHIFT, Keycode.FORWARD_SLASH)
kbd.send(Keycode.C)
kbd.send(Keycode.H)
kbd.send(Keycode.A)
kbd.send(Keycode.T)
kbd.send(Keycode.SHIFT,Keycode.MINUS)
kbd.send(Keycode.I)
kbd.send(Keycode.D)
kbd.send(Keycode.EQUALS)
kbd.send(Keycode.SIX)
kbd.send(Keycode.THREE)
kbd.send(Keycode.FOUR)
kbd.send(Keycode.EIGHT)
kbd.send(Keycode.FOUR)
kbd.send(Keycode.ONE)
kbd.send(Keycode.THREE)
kbd.send(Keycode.TWO)
kbd.send(Keycode.EIGHT)
kbd.send(Keycode.SHIFT, Keycode.SEVEN)
kbd.send(Keycode.T)
kbd.send(Keycode.E)
kbd.send(Keycode.X)
kbd.send(Keycode.T)
kbd.send(Keycode.EQUALS)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT,Keycode.EQUALS)
kbd.send(Keycode.U)
kbd.send(Keycode.R)
kbd.send(Keycode.L)
kbd.send(Keycode.L)
kbd.send(Keycode.I)
kbd.send(Keycode.B)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.P)
kbd.send(Keycode.A)
kbd.send(Keycode.R)
kbd.send(Keycode.S)
kbd.send(Keycode.E)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.Q)
kbd.send(Keycode.U)
kbd.send(Keycode.O)
kbd.send(Keycode.T)
kbd.send(Keycode.E)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.R)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.LEFT_BRACKET)
kbd.send(Keycode.B)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.S)
kbd.send(Keycode.P)
kbd.send(Keycode.L)
kbd.send(Keycode.I)
kbd.send(Keycode.T)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT, Keycode.SEMICOLON)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.LEFT_BRACKET)
kbd.send(Keycode.ONE)
kbd.send(Keycode.RIGHT_BRACKET)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.R)
kbd.send(Keycode.I)
kbd.send(Keycode.P)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.F)
kbd.send(Keycode.O)
kbd.send(Keycode.R)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.B)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.N)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.L)
kbd.send(Keycode.I)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.I)
kbd.send(Keycode.T)
kbd.send(Keycode.E)
kbd.send(Keycode.R)
kbd.send(Keycode.T)
kbd.send(Keycode.O)
kbd.send(Keycode.O)
kbd.send(Keycode.L)
kbd.send(Keycode.S)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.C)
kbd.send(Keycode.H)
kbd.send(Keycode.A)
kbd.send(Keycode.I)
kbd.send(Keycode.N)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.F)
kbd.send(Keycode.R)
kbd.send(Keycode.O)
kbd.send(Keycode.M)
kbd.send(Keycode.SHIFT,Keycode.MINUS)
kbd.send(Keycode.I)
kbd.send(Keycode.T)
kbd.send(Keycode.E)
kbd.send(Keycode.R)
kbd.send(Keycode.A)
kbd.send(Keycode.B)
kbd.send(Keycode.L)
kbd.send(Keycode.E)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.LEFT_BRACKET)
kbd.send(Keycode.O)
kbd.send(Keycode.U)
kbd.send(Keycode.T)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.S)
kbd.send(Keycode.P)
kbd.send(Keycode.L)
kbd.send(Keycode.I)
kbd.send(Keycode.T)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.BACKSLASH)
kbd.send(Keycode.BACKSLASH)
kbd.send(Keycode.R)
kbd.send(Keycode.BACKSLASH)
kbd.send(Keycode.BACKSLASH)
kbd.send(Keycode.N)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.F)
kbd.send(Keycode.O)
kbd.send(Keycode.R)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.O)
kbd.send(Keycode.U)
kbd.send(Keycode.T)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.N)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.LEFT_BRACKET)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.R)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.O)
kbd.send(Keycode.U)
kbd.send(Keycode.T)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.F)
kbd.send(Keycode.O)
kbd.send(Keycode.R)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.O)
kbd.send(Keycode.U)
kbd.send(Keycode.T)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.N)
kbd.send(Keycode.LEFT_BRACKET)
kbd.send(Keycode.P)
kbd.send(Keycode.R)
kbd.send(Keycode.O)
kbd.send(Keycode.C)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.C)
kbd.send(Keycode.O)
kbd.send(Keycode.M)
kbd.send(Keycode.M)
kbd.send(Keycode.U)
kbd.send(Keycode.N)
kbd.send(Keycode.I)
kbd.send(Keycode.C)
kbd.send(Keycode.A)
kbd.send(Keycode.T)
kbd.send(Keycode.E)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.F)
kbd.send(Keycode.O)
kbd.send(Keycode.R)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.P)
kbd.send(Keycode.R)
kbd.send(Keycode.O)
kbd.send(Keycode.C)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.N)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.LEFT_BRACKET)
kbd.send(Keycode.S)
kbd.send(Keycode.U)
kbd.send(Keycode.B)
kbd.send(Keycode.P)
kbd.send(Keycode.R)
kbd.send(Keycode.O)
kbd.send(Keycode.C)
kbd.send(Keycode.E)
kbd.send(Keycode.S)
kbd.send(Keycode.S)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.SHIFT, Keycode.P)
kbd.send(Keycode.O)
kbd.send(Keycode.P)
kbd.send(Keycode.E)
kbd.send(Keycode.N)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.N)
kbd.send(Keycode.E)
kbd.send(Keycode.T)
kbd.send(Keycode.S)
kbd.send(Keycode.H)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.W)
kbd.send(Keycode.L)
kbd.send(Keycode.A)
kbd.send(Keycode.N)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.S)
kbd.send(Keycode.H)
kbd.send(Keycode.O)
kbd.send(Keycode.W)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.P)
kbd.send(Keycode.R)
kbd.send(Keycode.O)
kbd.send(Keycode.F)
kbd.send(Keycode.I)
kbd.send(Keycode.L)
kbd.send(Keycode.E)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT,Keycode.EQUALS)
kbd.send(Keycode.S)
kbd.send(Keycode.S)
kbd.send(Keycode.I)
kbd.send(Keycode.D)
kbd.send(Keycode.SHIFT,Keycode.EQUALS)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.K)
kbd.send(Keycode.E)
kbd.send(Keycode.Y)
kbd.send(Keycode.EQUALS)
kbd.send(Keycode.C)
kbd.send(Keycode.L)
kbd.send(Keycode.E)
kbd.send(Keycode.A)
kbd.send(Keycode.R)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.S)
kbd.send(Keycode.P)
kbd.send(Keycode.L)
kbd.send(Keycode.I)
kbd.send(Keycode.T)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.COMMA)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.D)
kbd.send(Keycode.O)
kbd.send(Keycode.U)
kbd.send(Keycode.T)
kbd.send(Keycode.EQUALS)
kbd.send(Keycode.S)
kbd.send(Keycode.U)
kbd.send(Keycode.B)
kbd.send(Keycode.P)
kbd.send(Keycode.R)
kbd.send(Keycode.O)
kbd.send(Keycode.C)
kbd.send(Keycode.E)
kbd.send(Keycode.S)
kbd.send(Keycode.S)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.SHIFT, Keycode.P)
kbd.send(Keycode.SHIFT, Keycode.I)
kbd.send(Keycode.SHIFT, Keycode.P)
kbd.send(Keycode.SHIFT, Keycode.E)
kbd.send(Keycode.COMMA)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.S)
kbd.send(Keycode.H)
kbd.send(Keycode.E)
kbd.send(Keycode.L)
kbd.send(Keycode.L)
kbd.send(Keycode.EQUALS)
kbd.send(Keycode.SHIFT, Keycode.T)
kbd.send(Keycode.R)
kbd.send(Keycode.U)
kbd.send(Keycode.E)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.F)
kbd.send(Keycode.O)
kbd.send(Keycode.R)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.S)
kbd.send(Keycode.S)
kbd.send(Keycode.I)
kbd.send(Keycode.D)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.N)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.LEFT_BRACKET)
kbd.send(Keycode.C)
kbd.send(Keycode.LEFT_BRACKET)
kbd.send(Keycode.ZERO)
kbd.send(Keycode.RIGHT_BRACKET)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.R)
kbd.send(Keycode.I)
kbd.send(Keycode.P)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.F)
kbd.send(Keycode.O)
kbd.send(Keycode.R)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.C)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.N)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.LEFT_BRACKET)
kbd.send(Keycode.B)
kbd.send(Keycode.LEFT_BRACKET)
kbd.send(Keycode.ONE)
kbd.send(Keycode.RIGHT_BRACKET)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.S)
kbd.send(Keycode.P)
kbd.send(Keycode.L)
kbd.send(Keycode.I)
kbd.send(Keycode.T)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.BACKSLASH)
kbd.send(Keycode.BACKSLASH)
kbd.send(Keycode.R)
kbd.send(Keycode.BACKSLASH)
kbd.send(Keycode.BACKSLASH)
kbd.send(Keycode.N)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.F)
kbd.send(Keycode.O)
kbd.send(Keycode.R)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.B)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.N)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.LEFT_BRACKET)
kbd.send(Keycode.A)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.S)
kbd.send(Keycode.P)
kbd.send(Keycode.L)
kbd.send(Keycode.I)
kbd.send(Keycode.T)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT, Keycode.SEMICOLON)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.F)
kbd.send(Keycode.O)
kbd.send(Keycode.R)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.A)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.N)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.R)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.S)
kbd.send(Keycode.U)
kbd.send(Keycode.B)
kbd.send(Keycode.P)
kbd.send(Keycode.R)
kbd.send(Keycode.O)
kbd.send(Keycode.C)
kbd.send(Keycode.E)
kbd.send(Keycode.S)
kbd.send(Keycode.S)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.SHIFT, Keycode.P)
kbd.send(Keycode.O)
kbd.send(Keycode.P)
kbd.send(Keycode.E)
kbd.send(Keycode.N)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.N)
kbd.send(Keycode.E)
kbd.send(Keycode.T)
kbd.send(Keycode.S)
kbd.send(Keycode.H)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.W)
kbd.send(Keycode.L)
kbd.send(Keycode.A)
kbd.send(Keycode.N)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.S)
kbd.send(Keycode.H)
kbd.send(Keycode.O)
kbd.send(Keycode.W)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.P)
kbd.send(Keycode.R)
kbd.send(Keycode.O)
kbd.send(Keycode.F)
kbd.send(Keycode.I)
kbd.send(Keycode.L)
kbd.send(Keycode.E)
kbd.send(Keycode.S)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.S)
kbd.send(Keycode.P)
kbd.send(Keycode.L)
kbd.send(Keycode.I)
kbd.send(Keycode.T)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.COMMA)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.S)
kbd.send(Keycode.T)
kbd.send(Keycode.D)
kbd.send(Keycode.O)
kbd.send(Keycode.U)
kbd.send(Keycode.T)
kbd.send(Keycode.EQUALS)
kbd.send(Keycode.S)
kbd.send(Keycode.U)
kbd.send(Keycode.B)
kbd.send(Keycode.P)
kbd.send(Keycode.R)
kbd.send(Keycode.O)
kbd.send(Keycode.C)
kbd.send(Keycode.E)
kbd.send(Keycode.S)
kbd.send(Keycode.S)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.SHIFT, Keycode.P)
kbd.send(Keycode.SHIFT, Keycode.I)
kbd.send(Keycode.SHIFT, Keycode.P)
kbd.send(Keycode.SHIFT, Keycode.E)
kbd.send(Keycode.COMMA)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.S)
kbd.send(Keycode.H)
kbd.send(Keycode.E)
kbd.send(Keycode.L)
kbd.send(Keycode.L)
kbd.send(Keycode.EQUALS)
kbd.send(Keycode.SHIFT, Keycode.T)
kbd.send(Keycode.R)
kbd.send(Keycode.U)
kbd.send(Keycode.E)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.C)
kbd.send(Keycode.O)
kbd.send(Keycode.M)
kbd.send(Keycode.M)
kbd.send(Keycode.U)
kbd.send(Keycode.N)
kbd.send(Keycode.I)
kbd.send(Keycode.C)
kbd.send(Keycode.A)
kbd.send(Keycode.T)
kbd.send(Keycode.E)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.PERIOD)
kbd.send(Keycode.S)
kbd.send(Keycode.P)
kbd.send(Keycode.L)
kbd.send(Keycode.I)
kbd.send(Keycode.T)
kbd.send(Keycode.SHIFT, Keycode.NINE)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT, Keycode.A)
kbd.send(Keycode.L)
kbd.send(Keycode.L)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.SHIFT, Keycode.U)
kbd.send(Keycode.S)
kbd.send(Keycode.E)
kbd.send(Keycode.R)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.SHIFT, Keycode.P)
kbd.send(Keycode.R)
kbd.send(Keycode.O)
kbd.send(Keycode.F)
kbd.send(Keycode.I)
kbd.send(Keycode.L)
kbd.send(Keycode.E)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.LEFT_BRACKET)
kbd.send(Keycode.ONE)
kbd.send(Keycode.SHIFT, Keycode.SEMICOLON)
kbd.send(Keycode.RIGHT_BRACKET)
kbd.send(Keycode.RIGHT_BRACKET)
kbd.send(Keycode.RIGHT_BRACKET)
kbd.send(Keycode.RIGHT_BRACKET)
kbd.send(Keycode.RIGHT_BRACKET)
kbd.send(Keycode.RIGHT_BRACKET)
kbd.send(Keycode.RIGHT_BRACKET)
kbd.send(Keycode.RIGHT_BRACKET)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.F)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SHIFT, Keycode.K)
kbd.send(Keycode.E)
kbd.send(Keycode.Y)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.SHIFT, Keycode.C)
kbd.send(Keycode.O)
kbd.send(Keycode.N)
kbd.send(Keycode.T)
kbd.send(Keycode.E)
kbd.send(Keycode.N)
kbd.send(Keycode.T)
kbd.send(Keycode.QUOTE)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.I)
kbd.send(Keycode.N)
kbd.send(Keycode.SPACE)
kbd.send(Keycode.B)
kbd.send(Keycode.RIGHT_BRACKET)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SHIFT, Keycode.ZERO)
kbd.send(Keycode.SHIFT, Keycode.QUOTE)
kbd.send(Keycode.ENTER)
kbd.send(Keycode.E)
kbd.send(Keycode.X)
kbd.send(Keycode.I)
kbd.send(Keycode.T)
kbd.send(Keycode.ENTER)
