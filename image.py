import cv2
import numpy as np
import matplotlib.pyplot as plt

# read IR image
image_path1 = ".\\source\\p1-assets\\1_2.PNG" #input 1 change here
image_path2 = ".\\source\\p1-assets\\1_1.PNG" #input 2 change here
image_path3 = ".\\II.png" #input 3 change here
def process_images(image_path1, image_path2,image_path3):
    original_image = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    original_image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    # read new image and resize it to match the original images
    new_image = cv2.imread(image_path3, cv2.IMREAD_GRAYSCALE)
    new_image = cv2.resize(new_image, (original_image.shape[1], original_image.shape[0]))

    # Define the trapezoid coordinates
    height, width = original_image.shape
    trapezoid_top = int(height * 0.3)
    trapezoid_bottom = height
    trapezoid_left = int(width * 0.3)
    trapezoid_right = int(width * 0.7)

    # Crop the original image to the trapezoid region
    cropped_image = original_image[trapezoid_top:trapezoid_bottom, trapezoid_left:trapezoid_right]

    # avg grey intensity of the IR image
    avg_grey = np.mean(original_image)

    hist = cv2.calcHist([original_image], [0], None, [256], [0, 256])

    # find most common pixel value
    most_common_pixel_value = np.argmax(hist)

    # use GaussianBlurry to denoise
    blurred_image = cv2.GaussianBlur(original_image, (5, 5), 0)

    # use Canny Algorithm to detect the edge
    lower_threshold = 50
    upper_threshold = 150
    edges = cv2.Canny(blurred_image, lower_threshold, upper_threshold)

    # binary setting as thd is most common piexl value
    ret, binary_image = cv2.threshold(edges, most_common_pixel_value, 255, cv2.THRESH_BINARY)

    # find contours
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # set area_threshold of a contour, if the area is low than that, the contour will be abandoned
    area_threshold = 10

    # find centers
    # find centers
    centers = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > area_threshold:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                
                # Check if the center is within the trapezoid
                if trapezoid_top <= cY <= trapezoid_bottom and trapezoid_left <= cX <= trapezoid_right:
                    centers.append((cX, cY))


    # mark center in IR picture and Visible light picture
    marked_image1 = original_image.copy()
    for center in centers:
        cv2.circle(marked_image1, center, 5, (255, 0, 0), -1)

    marked_image2 = original_image2.copy()
    for center in centers:
        cv2.circle(marked_image2, center, 5, (255, 0, 0), -1)
    # print(marked_image2.shape)
    # print(new_image.shape)

    # overlay the new image on the marked images
    overlay_alpha = 0.5  # define the transparency level
    marked_image1 = cv2.addWeighted(marked_image1, 1 - overlay_alpha, new_image, overlay_alpha, 0)
    marked_image2 = cv2.addWeighted(marked_image2, 1 - overlay_alpha, new_image, overlay_alpha, 0)

    return centers,marked_image1,marked_image2,original_image,edges

centers, marked_image1,marked_image2,original_image,edges= process_images(image_path1,image_path2,image_path3)
# output
plt.subplot(1, 3, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(edges, cmap='gray')
plt.title('Edge Detection')

plt.subplot(1, 3, 3)
plt.imshow(marked_image1, cmap='gray')
plt.title('Centers Marked')

# plt.subplot(1, 4, 4)
# plt.imshow(marked_image2,cmap='plasma')
# plt.title('Centers Marked')
cv2.imwrite('marked_image1.png', marked_image1)

plt.show()
