from PIL import Image

def pad_image_to_square(image_path, output_path):
    img = Image.open(image_path)
    width, height = img.size
    new_size = max(width, height)
    
    # Create a new square image with a transparent background
    new_img = Image.new('RGBA', (new_size, new_size), (255, 255, 255, 0))
    
    # Calculate the position to paste the original image so it's centered
    paste_x = (new_size - width) // 2
    paste_y = (new_size - height) // 2
    
    # Paste the original image
    new_img.paste(img, (paste_x, paste_y))
    
    # Save the new image
    new_img.save(output_path)

pad_image_to_square('favicon.png', 'favicon_square.png')
print("Saved square favicon to favicon_square.png")
