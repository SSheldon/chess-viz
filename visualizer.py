import re
import chess
import pyglet
from pyglet.gl import *

class Visualizer:
	def __init__(self):
		self.window = pyglet.window.Window()
		self.window.set_handler('on_draw', self.onDraw)
		glClearColor(1, 1, 1, 1)

	def onDraw(self):
		glClear(GL_COLOR_BUFFER_BIT)

	def run(self):
		pyglet.app.run()

game = chess.Game()
for row in game.show():
	print row
for line in open('samples-pgn/simple.pgn'):
	for command in re.findall(r'[^\s\.]+(?!\S)', line):
		game.move(command)
		for row in game.show():
			print row
		game.advance()
