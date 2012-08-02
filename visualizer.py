import re
import chess

game = chess.Game()
for row in game.show():
	print row
for line in open('samples-pgn/simple.pgn'):
	for command in re.findall(r'[^\s\.]+(?!\S)', line):
		game.move(command)
		for row in game.show():
			print row
		game.advance()
