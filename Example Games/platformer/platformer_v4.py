import pyglet

class Player(pyglet.sprite.Sprite):
	grounded = True
	velocity = 0
	jump = 500
	speed = 400

	def __init__(self, world, image):
		super().__init__(image, batch=world.batch, group=world.foreground)

		self.world = world
		self.y = 250
		self.x = 0

	def update(self, dt):
		if self.world.pressed_keys[pyglet.window.key.A]:
			self.moveX(-self.speed * dt)
		if self.world.pressed_keys[pyglet.window.key.D]:
			self.moveX(self.speed * dt)

		if self.world.pressed_keys[pyglet.window.key.W] and self.grounded:
			self.velocity += self.jump
			self.grounded = False

		self.moveY(self.velocity * dt)
		self.velocity -= self.world.gravity * dt

	def moveX(self, x):
		self.x += int(x)

		for obj in self.world.objects:
			if obj == self:
				continue
			if obj.x + obj.width > self.x and obj.x < self.x + self.width and obj.y + obj.height > self.y and obj.y < self.y + self.height:
				if x > 0:
					self.x = obj.x - self.width
				if x < 0:
					self.x = obj.x + obj.width
					self.grounded = True

	def moveY(self, y):
		self.y += int(y)

		for obj in self.world.objects:
			if obj == self:
				continue
			if obj.x + obj.width > self.x and obj.x < self.x + self.width and obj.y + obj.height > self.y and obj.y < self.y + self.height:
				if y > 0:
					self.y = obj.y - self.height
				if y < 0:
					self.y = obj.y + obj.height
					self.grounded = True



class Block():
	def __init__(self, world, x, y, width, height, color=(255,255,255)):
		self.world = world

		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.color = color

		self.world.batch.add(4, pyglet.gl.GL_QUADS, self.world.foreground,
			('v2i', (self.x,self.y , self.x + self.width,self.y , self.x + self.width,self.y + self.height , self.x,self.y + self.height)),
			('c3B', self.color * 4)
		)

	def update(self, dt):
		pass

class World(pyglet.window.Window):
	gravity = 98
	ground = 20

	def __init__(self, width, height):
		super().__init__(width, height)

		self.pressed_keys = pyglet.window.key.KeyStateHandler()
		self.push_handlers(self.pressed_keys)

		self.batch = pyglet.graphics.Batch()
		self.background = pyglet.graphics.OrderedGroup(0)
		self.foreground = pyglet.graphics.OrderedGroup(1)
		self.objects = []

		image = pyglet.resource.image('kitten.png')
		self.objects.append(Player(self, image))

		self.objects.append(Block(self, 0, 0, width, 50))

		self.objects.append(Block(self, 300, 250, 50, 50))

		pyglet.clock.schedule(self.update, 1/60.0)

	def on_draw(self):
		self.clear()
		self.batch.draw()

	def update(self, dt, ex_dt):
		for obj in self.objects:
			obj.update(dt)

if __name__ == "__main__":
	game = World(500,500)
	pyglet.app.run()