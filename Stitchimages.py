import cv2
import numpy as np

def stitch_images(image_paths):
    # Load images and resize for better stitching results
    images = []
    for image_path in image_paths:
        img = cv2.imread(image_path)
        if img is None:
            print(f"Error loading image: {image_path}")
            return None
        # Resize images to a smaller size to speed up processing (optional)
        img = cv2.resize(img, (800, int(img.shape[0] * 800 / img.shape[1])))  # Resize maintaining aspect ratio
        images.append(img)
    
    # Create a stitcher and stitch images
    stitcher = cv2.Stitcher.create()
    status, stitched_image = stitcher.stitch(images)
    
    if status != cv2.Stitcher_OK:
        print("Error during stitching: ", status)
        return None
    
    return stitched_image

image_paths = ['camera1.png', 'camera2.png', 'camera3.png', 'camera4.png']
stitched_image = stitch_images(image_paths)

if stitched_image is not None:
    cv2.imwrite('stitched_image.png', stitched_image)
    cv2.imshow('Stitched Image', stitched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
