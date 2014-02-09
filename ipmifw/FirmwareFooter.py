import struct

class FirmwareFooter:
	def __init__(self):
		# these together get you the firmware version: rev1.rev2
		self.rev1 = 0
		self.rev2 = 0
		self.checksum = 0
		# fwtag appears to be some way of recogizing that this is indeed a footer
		# should be 0x71
		self.fwtag1 = 0
		# should be 0x17
		self.fwtag2 = 0

	def loadFromString(self, footer):
		(self.rev1, self.rev2, self.fwtag1, self.checksum, self.fwtag2) = struct.unpack("<bbbIb", footer)

	def __str__(self):
		return "Firmware footer version %i.%i checksum: 0x%x tag: 0x%x%x" % (self.rev1, self.rev2, self.checksum, self.fwtag1, self.fwtag2)
