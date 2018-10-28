import pyglet # import pyglet module

# Define our window
window = pyglet.window.Window(width=400, height=400, caption="Display Text")

# Create a lable 'object' that contains our parameters
label = pyglet.text.Label('Hello, world',
	font_name='Times New Roman', font_size=36,
	x=window.width//2, y=window.height//2,
	anchor_x='center', anchor_y='center'
)


@window.event
def on_draw(): # Make our on_draw() function
    label.draw() # Draw the text

pyglet.app.run() # ALWAYS!!!! This tells pyglet to run
