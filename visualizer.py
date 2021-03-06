from exceptions import StopIteration
import re
import chess
import pyglet
from pyglet.gl import *

class Visualizer:
	def __init__(self, commands):
		self.commands = commands
		self.game = chess.Game()
		self.window = pyglet.window.Window()
		self.window.set_handler('on_draw', self.onDraw)
		pyglet.clock.schedule_interval(self.update, 1)
		glClearColor(1, 1, 1, 1)

	def onDraw(self):
		glClear(GL_COLOR_BUFFER_BIT)
		for row in self.game.show():
			print row

	def update(self, dt=0):
		command = self.getCommand()
		if command:
			self.game.move(command)
			self.game.advance()

	def getCommand(self):
		try:
			return self.commands.next()
		except StopIteration:
			return None

	def run(self):
		pyglet.app.run()

commands = (command for line in open('samples-pgn/simple.pgn')
	for command in re.findall(r'[^\s\.]+(?!\S)', line))
viz = Visualizer(commands)
viz.run()
