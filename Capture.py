import numpy as np
import cv2

def create_composite_map(image_paths):
    # Initialize a blank composite map
    composite_map = np.zeros((512, 512), dtype=np.uint8)
    
    for path in image_paths:
        # Load the image in grayscale
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        
        if img is None:
            print(f"Error loading image: {path}")
            continue
        
        # Resize the image to 512x512
        resized_img = cv2.resize(img, (512, 512))
        
        # Accumulate the resized image into the composite map
        composite_map += resized_img // 4  # Adjusting brightness
        
    # Save the composite map as a PGM file
    cv2.imwrite('composite_map.pgm', composite_map)

# List of image paths
image_paths = ['camera1.png', 'camera2.png', 'camera3.png', 'camera4.png']
create_composite_map(image_paths)
