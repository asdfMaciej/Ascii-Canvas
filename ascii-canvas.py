import math

class Canvas:
	def __init__(self, width=10, height=10, filler=' '):
		self.painting = []
		for i in range(height):
			x = []
			for z in range(width):
				x.append(str(filler))
			self.painting.append(x)

	def __str__(self):
		res = ''
		for line in self.painting:
			for char in line:
				res += char
			res += '\n'
		return res

	def __eq__(self, other):
		if isinstance(other, Canvas):
			return other.painting == self.painting
		else:
			return False

	def __ne__(self, other):
		if isinstance(other, Canvas):
			return other.painting != self.painting
		else:
			return False

	def __len__(self):
		return len(self.painting) * len(self.painting[0])

	def __setitem__(self, key, value):
		self.painting[key] = value

	def __getitem__(self, key):
		return self.painting[key]
		
	def set_point(self, coords, filler):
		try:
			self.painting[coords[1]][coords[0]] = str(filler)
		except IndexError:
			raise IndexError("[!] Point out of bounds of the array.")

	def get_point(self, coords):
		try:
			return self.painting[cooords[1]][coords[0]]
		except IndexError:
			raise IndexError("[!] Point out of bounds of the array.")

	def draw_point_intensitity(self, coords, intense):
		""" Intense is on scale of 0 to 255"""
		character = ' `.,:;irsXA253hGSBH9E@M#'[int(math.floor(intense/11))]
		self.set_point(coords, character)

	def draw_text(self, coords, text):
		bc = len(self.painting) * len(self.painting[0])
		if bc - (coords[0] + coords[1]*len(self.painting[0])) < len(text):
			raise IndexError("[!] Fail due to text too long.")

		for a in range(len(text)):
			b = a+1
			b = b-1
			a += coords[0] + coords[1]*len(self.painting[0])
			y = (a - (a % len(self.painting[0]))) / len(self.painting[0])
			x = a % len(self.painting[0])
			self.set_point((x, y), text[b])

	def draw_fill(self, coords1, coords2, symbol):
		x1, y1 = coords1
		x2, y2 = coords2
		difx, dify = abs(x1-x2)+1, abs(y1-y2)+1
		for a in range(dify):
			for b in range(difx):
				self.set_point((min(x1, x2)+b, min(y1, y2)+a), symbol)
	def draw_line(self, coords1, coords2, symbol):
		x1, y1 = coords1
		x2, y2 = coords2
		points = []
		issteep = abs(y2-y1) > abs(x2-x1)
		if issteep:
			x1, y1 = y1, x1
			x2, y2 = y2, x2
		rev = False
		if x1 > x2:
			x1, x2 = x2, x1
			y1, y2 = y2, y1
			rev = True
		deltax = x2 - x1
		deltay = abs(y2-y1)
		error = int(deltax / 2)
		y = y1
		ystep = None
		if y1 < y2:
			ystep = 1
		else:
			ystep = -1
		for x in range(x1, x2 + 1):
			if issteep:
				points.append((y, x))
			else:
				points.append((x, y))
			error -= deltay
			if error < 0:
				y += ystep
				error += deltax

		if rev:
			points.reverse()
		for p in points:
			self.set_point(p, symbol)

if __name__ == '__main__':
	canvas = Canvas(20, 20, ' ')

	canvas.draw_text((5, 5), "bozek"*30)
	canvas.draw_fill((10, 7), (16, 17), '$')
	canvas.draw_line((0, 0), (19, 19), '#')
	print canvas
