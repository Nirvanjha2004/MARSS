from PIL import Image

def calculate_brightness(pixel):
    return (0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2]) / 3

def process_image(image_path, threshold, brightness_level):
    img = Image.open(image_path)
    width, height = img.size
    typeA_count = 0
    typeB_count = 0

    # Create a new image for black and white
    bw_img = Image.new("RGB", (width, height))

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))

           
            if pixel[0] > threshold[0] and pixel[1] > threshold[1] and pixel[2] > threshold[2]:
                typeA_count += 1
            else:
                typeB_count += 1

           
            brightness = calculate_brightness(pixel)
            if brightness > brightness_level:
                bw_img.putpixel((x, y), (0, 0, 0))  # black
            else:
                bw_img.putpixel((x, y), (255, 255, 255))  # white

   
    total_pixels = width * height
    percentage_typeA = (typeA_count / total_pixels) * 100
    percentage_typeB = (typeB_count / total_pixels) * 100

   
    bw_img.show()

   
    print(f"Percentage of typeA pixels: {percentage_typeA:.2f}%")
    print(f"Percentage of typeB pixels: {percentage_typeB:.2f}%")


image_path = r"C:\Users\nirva\OneDrive\Desktop\your_image.jpg"
threshold = (160, 160, 160)
brightness_level = 137 
process_image(image_path, threshold, brightness_level)