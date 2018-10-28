import pyglet # import pyglet module

# Define our window
window = pyglet.window.Window(width=400, height=400, caption="Display Image")

# Define the image we want to display
flappy_image = pyglet.resource.image('Images/flappybird.png')


# Create a sprite 'object' that contains the image, and can be drawn
flappybird = pyglet.sprite.Sprite(flappy_image, x=100, y=100)
flappybird.scale_x = 0.2 # set images x scale (make it 0.5 times smaller)
flappybird.scale_y = 0.2 # set images y scale (make it 0.5 times smaller)


@window.event
def on_draw(): # Make our on_draw() function
    flappybird.draw() # Draw the image

pyglet.app.run() # ALWAYS!!!! This tells pyglet to run
