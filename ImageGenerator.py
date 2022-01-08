from PIL import Image

# Enlarge scale factor
SCALE_FACTOR = 4

# Open template image
img_template = Image.open(r"D:\01_Dev\ImageGenerator\Tamplate.jpg")

# Open overlay image
img_overlay = Image.open(r"D:\01_Dev\ImageGenerator\header.jpg")

# Enlarge header to 400%
img_overlay_resize = img_overlay.resize((img_overlay.width * SCALE_FACTOR, img_overlay.height * SCALE_FACTOR))

# Paste header image at the center of template image
img_template.paste(img_overlay_resize, (img_template.width // 2 - img_overlay_resize.width // 2, img_template.height // 2 - img_overlay_resize.height // 2))

# Save image
img_template.save(r"D:\01_Dev\ImageGenerator\item_img.jpg")

# Displaying the image
img_template.show()