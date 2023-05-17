from PIL import Image, ImageFont, ImageDraw

OUTPUT_DPI_X = 1200 # FIXME: keegs is 4800
OUTPUT_DPI_Y = 1200 # keegs' sticker printer

STICKER_WIDTH_INCHES = 4.055
STICKER_HEIGHT_INCHES = 0.787 # as per https://www.deviantart.com/borracho2x/art/Template-Sega-Master-System-805970013

GRID_SQUARES_X = 32
GRID_SQUARES_Y = 7

SEGA_LOGO_FONT = 'SEGA' # from https://www.dafont.com/sega.font
LABEL_FONT = 'himalaya' # from https://gettyfonts.net/font/himalaya/download

GRID_LINE_THICKNESS = 10 # in pixels

# Colours
SMS_LOGO_RED = (129, 11, 2)
SMS_LOGO_BLACK = (46, 9, 0)
SMS_LOGO_WHITE = (255, 255, 255)

# User parameters (TODO: fill from arguments)
label = 'Snail Maze'

# Create image
width_pixels = int(OUTPUT_DPI_X * STICKER_WIDTH_INCHES) # TODO: might need some tinkering to get this right on the printer
height_pixels = int(OUTPUT_DPI_Y * STICKER_HEIGHT_INCHES)
im = Image.new(mode = 'RGB', size = ( width_pixels, height_pixels ), color = SMS_LOGO_RED)
draw = ImageDraw.Draw(im)

# First render the grid
for x in range(1, GRID_SQUARES_X):
    grid_span_x = im.width / GRID_SQUARES_X
    draw.line((x * grid_span_x, 0, x * grid_span_x, im.height), fill=SMS_LOGO_BLACK, width=GRID_LINE_THICKNESS)

for y in range(1, GRID_SQUARES_Y):
    grid_span_y = im.height / GRID_SQUARES_Y
    draw.line((0, y * grid_span_y, im.width, y * grid_span_y), fill=SMS_LOGO_BLACK, width=GRID_LINE_THICKNESS)

# width is still a little off
sega_font = ImageFont.truetype(SEGA_LOGO_FONT, int(height_pixels * (1.85/GRID_SQUARES_Y)))
sega_font_y = height_pixels - (height_pixels * (2.8/GRID_SQUARES_Y))
sega_font_x = width_pixels - (width_pixels * (6.0/GRID_SQUARES_X))
draw.text((sega_font_x, sega_font_y), "SEGA", SMS_LOGO_WHITE, font=sega_font)

# label text
label_font = ImageFont.truetype(LABEL_FONT, int(height_pixels * (4.50/GRID_SQUARES_Y)))
label_font_x = int(width_pixels * (1.95/GRID_SQUARES_X))
label_font_y = int(height_pixels - (height_pixels * (4.50/GRID_SQUARES_Y)))
draw.text((label_font_x, label_font_y), label, SMS_LOGO_WHITE, font=label_font)

# Save the resulting image
im.save('output.png')
