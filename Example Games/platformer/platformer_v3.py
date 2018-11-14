import pyglet

class Player(pyglet.sprite.Sprite):
	grounded = True
	velocity = 0
	jump = 200
	speed = 400

	def __init__(self, world, image):
		super().__init__(image, batch=world.batch, group=world.foreground)

		self.world = world

	def update(self, dt):
		if self.world.pressed_keys[pyglet.window.key.A]:
			self.x -= int(self.speed * dt)
		if self.world.pressed_keys[pyglet.window.key.D]:
			self.x += int(self.speed * dt)

		if self.world.pressed_keys[pyglet.window.key.W] and self.grounded:
			self.velocity += self.jump
			self.grounded = False

		self.y += self.velocity * dt

		if self.y < self.world.ground:
			self.y = self.world.ground
			self.velocity = 0
			self.grounded = True
		else:
			self.velocity -= self.world.gravity * dt

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

		image = pyglet.resource.image('kitten.png')
		self.player = Player(self, image)

		Block(self, 0, 0, width, 50)

		pyglet.clock.schedule(self.update, 1/60.0)

	def on_draw(self):
		self.clear()

		self.batch.draw()

	def update(self, dt, ex_dt):
		self.player.update(dt)
		

if __name__ == "__main__":
	game = World(500,500)
	pyglet.app.run()