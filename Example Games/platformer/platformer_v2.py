import pyglet

class Player(pyglet.sprite.Sprite):
	grounded = True
	velocity = 0
	jump = 200
	speed = 400

	def __init__(self, world, image):
		super().__init__(image)

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

class World(pyglet.window.Window):
	gravity = 98
	ground = 0

	def __init__(self, width, height):
		super().__init__(width, height)

		image = pyglet.resource.image('kitten.png')
		self.player = Player(self, image)

		self.pressed_keys = pyglet.window.key.KeyStateHandler()
		self.push_handlers(self.pressed_keys)

		pyglet.clock.schedule(self.update, 1/60.0)

	def on_draw(self):
		self.clear()

		self.player.draw()

	def update(self, dt, ex_dt):
		self.player.update(dt)
		

if __name__ == "__main__":
	game = World(500,500)
	pyglet.app.run()