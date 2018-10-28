import pyglet # import pyglet module

# Define our window
window = pyglet.window.Window(width=400, height=400)

# Displayed rectangle position and dimension variables:
x = 100
y = 100
width = 100
height = 100

# Red, green, and blue values for rectangle:
red = 1
green = 0
blue = 1

# Define a tuple named 'color' with our values:
color = (red, green, blue) * 4

# Our draw function:
@window.event
def on_draw():
    window.clear()
    # Makes a polygon with 4 sides:
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
    	('v2i', (x,y , x+width,y , x+width,y+height , x,y+height)),
    	('c3f', color)
    )

pressed_keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(pressed_keys)

speed = 400 # Define speed variable
def update(dt,ex_dt):
	global x
	global y

	if pressed_keys[pyglet.window.key.W]: # IF W is pressed
		y += int(speed * dt) # Increase y position
	if pressed_keys[pyglet.window.key.S]:
		y -= int(speed * dt) # Decrease y position
	if pressed_keys[pyglet.window.key.A]:
		x -= int(speed * dt) # Decrease x position
	if pressed_keys[pyglet.window.key.D]:
		x += int(speed * dt) # Increase x position

pyglet.clock.schedule(update, 1/60.0)

pyglet.app.run()
