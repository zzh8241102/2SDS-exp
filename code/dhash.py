from PIL import Image

def caculateHashValue(image):
    resize_width = 9
    resize_height = 8
    smaller_img = image.resize((resize_width, resize_height),Image.ANTIALIAS)
    grayscale_image = smaller_img.convert('L')
    pixels = list(grayscale_image.getdata())
    difference = []
    for row in range(resize_height):
        row_s_idx = row * resize_width
        for col in range(resize_width - 1):
            left_pixel_idx = row_s_idx + col
            difference.append(pixels[left_pixel_idx] > pixels[left_pixel_idx + 1])
    decimal_value = 0
    hash_base16 = ""
    for index, value in enumerate(difference):    
        if value:         
                decimal_value += value * (2 ** (index % 8))   
        if index % 8 == 7:  
                hash_base16 += str(hex(decimal_value)[2:].rjust(2, "0")) 
                decimal_value = 0
    return hash_base16

def caculateHammingDistance(dhash1,dhash2):
    difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
    return bin(difference).count("1")
