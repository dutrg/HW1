import cv2 
import matplotlib.pyplot as plt
import numpy as np

# Load an image from file as function
def load_image(image_path):
    """
    Load an image from file, using OpenCV
    """
    image = cv2.imread(image_path)
    return image

# Display an image as function
def display_image(image, title="Image"):
    """
    Display an image using matplotlib. Rembember to use plt.show() to display the image
    """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()


# grayscale an image as function
def grayscale_image(image):
    """
    Convert an image to grayscale. Convert the original image to a grayscale image. In a grayscale image, the pixel value of the
    3 channels will be the same for a particular X, Y coordinate. The equation for the pixel value
    [1] is given by:
        p = 0.299R + 0.587G + 0.114B
    Where the R, G, B are the values for each of the corresponding channels. We will do this by
    creating an array called img_gray with the same shape as img
    """
    # pass
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    
    return gray_image


# Save an image as function
def save_image(image, output_path):
    """
    Save an image to file using OpenCV
    """
    cv2.imwrite(output_path, image)


# flip an image as function 
def flip_image(image):
    """
    Flip an image horizontally using OpenCV
    """
    # pass
    return cv2.flip(image, 1)



# rotate an image as function
def rotate_image(image, angle):
    """
    Rotate an image using OpenCV. The angle is in degrees
    """
    # pass
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


if __name__ == "__main__":
    # Load an image from file
    img = load_image("hw1/uet.png")

    # Display the image
    display_image(img, "Original Image")

    # Convert the image to grayscale
    img_gray = grayscale_image(img)

    # Display the grayscale image
    display_image(img_gray, "Grayscale Image")

    # Save the grayscale image
    save_image(img_gray, "hw1/lena_gray.jpg")

    # Flip the grayscale image
    img_gray_flipped = flip_image(img_gray)

    # Display the flipped grayscale image
    display_image(img_gray_flipped, "Flipped Grayscale Image")

    # Rotate the grayscale image
    img_gray_rotated = rotate_image(img_gray, 45)

    # Display the rotated grayscale image
    display_image(img_gray_rotated, "Rotated Grayscale Image")

    # Save the rotated grayscale image
    save_image(img_gray_rotated, "hw1/lena_gray_rotated.jpg")

    #Additional function
    # flipped_image = flip_image(img)

    # save_image(flipped_image, "hw1/flipped_image.jpg")

    # rotated_image = rotate_image(img, 45)

    # save_image(rotated_image, "hw1/rotated_image.jpg")




    # Show the images
    plt.show() 
