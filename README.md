# EC602_hw3
Open CV Assignment

4.1 EXERCISE 1

    The Matrices are stored in Row Major order. This means that we can access the element using the row and the column index. For an image with x and y coordinates, mat.at(row,col) = mat.at(y,x).

5.1 EXERCISE 2

    The output of ColorImage.cpp shows the conversion to different colorspaces starting from an original image that is in the RGB format.
The image is first split with only Red, Green and Blue parts and those are displayed. Then the image is converted to Ycrcb image and it is again split into Y, Cr and Cb components and displayed as three different images. Then it is converted to HSV colorspace and is then split into the Hue, Saturation and Value and printed as three different images.

9.1 EXERCISE 5

    Detecting an object in each frame would be like doing the exact same task again and again in each frame and hence repeating the work. But object tracking is better because it is like reusing the work done to detect the object and to track only the changes from the previous frame.
  
