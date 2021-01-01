from pyboy import PyBoy
pyboy = PyBoy('ROMs/gamerom.gb')
while not pyboy.tick():
	pass
