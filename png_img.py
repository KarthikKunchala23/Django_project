#changing image file into jpg file
from PIL import Image

# Open the image file
with Image.open('bobf_franchise_slider_efe95678_jpeg_region_0_0_1536_864') as im:
    # Convert the image to RGB if it is not already in RGB mode
    if im.mode != 'RGB':
        im = im.convert('RGB')
    # Save the image in JPEG format with 80% quality
    im.save('starwars.jpg', quality=80)
