import pyglet # import pyglet module
import math
from pyglet.window import mouse

# Define our window
window = pyglet.window.Window(width=600, height=600)

# Define the image we want to display
iochar_image = pyglet.resource.image('resources/iochar.png')
io_title_image = pyglet.resource.image('resources/title.png')
bullet_image = pyglet.resource.image('resources/bullet.png')

# Create a sprite 'object' that contains the image, and can be drawn
io_character = pyglet.sprite.Sprite(iochar_image, x=100, y=100)
io_character.scale_x = 0.4 # set images x scale (make it 0.5 times smaller)
io_character.scale_y = 0.4 # set images y scale (make it 0.5 times smaller)
io_character.image.anchor_x = io_character.image.width/2 # set images x scale (make it 0.5 times smaller)
io_character.image.anchor_y = io_character.image.height/2  # set images y scale (make it 0.5 times smaller)


title = pyglet.sprite.Sprite(io_title_image)
title.scale_x = 0.4 # set images x scale (make it 0.5 times smaller)
title.scale_y = 0.4 # set images y scale (make it 0.5 times smaller)
title.x = (window.width/2) - (title.width/2)
title.y = (window.height/2) - (title.height/2)

global allBullets # Global variable that is used all over
allBullets = []
bullet_speed = 25
bulletBatch = pyglet.graphics.Batch()

background_color = (128/255,175/255,73/255) * 4

# Our draw function:
@window.event
def on_draw():
    window.clear()
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
    	('v2i', (0,0 , 600,0 , 600,600 , 0,600)),
    	('c3f', background_color)
    )
    bulletBatch.draw()
    io_character.draw()
    title.draw()


def createBullet(velX,velY): # Makes a bullet
    bullet = pyglet.sprite.Sprite(bullet_image, batch= bulletBatch)
    bullet.rotation = io_character.rotation - 90
    bullet.x = io_character.x
    bullet.y = io_character.y
    bullet.scale = 0.4
    bullet.opacity = 150

    allBullets.append( { # Adds it to a list of bullets (helpful later)
        'sprite': bullet,
        'velX': velX,
        'velY': velY
    } )


def rotateCharacter(x,y):
    xDistanceFromChar = x - io_character.x # x distance from player
    yDistanceFromChar = y - io_character.y # y distance from player

    if xDistanceFromChar != 0: # if the x distance doesn't equal to zero
        ratio = (yDistanceFromChar)/ (xDistanceFromChar)
        angle = math.degrees(math.atan(ratio))
        if xDistanceFromChar < 0:
            angle = angle + 180
        io_character.rotation = -angle # Negative for counter clockwise

def shoot(x,y):
    xDistanceFromChar = x - io_character.x # x distance from player
    yDistanceFromChar = y - io_character.y # y distance from player

    if xDistanceFromChar != 0: # if the x distance doesn't equal to zero
        ratio = (yDistanceFromChar)/ (xDistanceFromChar)
        angle = abs(math.degrees(math.atan(ratio)))
        dx = math.cos( (angle * 0.01745 ) ) * bullet_speed # Makes x velocity
        dy = math.sin( (angle * 0.01745 ) ) * bullet_speed # Makes y velocity

        createBullet( # Create the bullet
        abs(dx) * (xDistanceFromChar / abs(xDistanceFromChar)),
        abs(dy) * (yDistanceFromChar / abs(yDistanceFromChar))
        )


@window.event
def on_mouse_motion(x, y, dx, dy):  # When the mouse moves on screen
    rotateCharacter(x,y)


@window.event
def on_mouse_press(x, y, button, modifiers):  # When the mouse is pressed
    rotateCharacter(x,y)
    shoot(x,y)


pressed_keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(pressed_keys)

speed = 200 # Define speed variable
def update(dt,ex_dt):

    for index,bullet in enumerate(allBullets):  # Moves the bullet
        bullet['sprite'].x += bullet['velX']
        bullet['sprite'].y += bullet['velY']

        if  bullet['sprite'].x  > 600 or bullet['sprite'].x < 0: # CLEANUP
            bullet['sprite'].delete()
            del allBullets[index]

    if pressed_keys[pyglet.window.key.W]: # IF W is pressed
    	io_character.y += int(speed * dt) # Increase y position
    if pressed_keys[pyglet.window.key.S]:
    	io_character.y -= int(speed * dt) # Decrease y position
    if pressed_keys[pyglet.window.key.A]:
    	io_character.x -= int(speed * dt) # Decrease x position
    if pressed_keys[pyglet.window.key.D]:
    	io_character.x += int(speed * dt) # Increase x position


pyglet.clock.schedule(update, 1/60.0)

pyglet.app.run()
