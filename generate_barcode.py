import barcode
from barcode.writer import ImageWriter

# Your name
name = "Jack"

# Generate a Code 128 barcode
code = barcode.Code128(name, writer=ImageWriter())

# Save the barcode as an image file
code.save('jack_barcode')
