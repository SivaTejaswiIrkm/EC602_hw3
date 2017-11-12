import cv2
import numpy as np
import sys

def gaussian_Noise(baboon, mean, sigma):

    noisyPic=baboon.copy()
    cv2.randn(noisyPic,mean,sigma)
    cv2.add(baboon, noisyPic, noisyPic)

    return noisyPic

def salt_pepper_Noise(baboon, pa, pb):
    amount1 = int(baboon.shape[0]*baboon.shape[1]*pa)
    amount2 = int(baboon.shape[0]*baboon.shape[1]*pb)

    pa1 = [0.01, 0.03, 0.05, 0.4]
    pb1 = [0.01, 0.03, 0.05, 0.4]

    for i in range(len(pa1)):
        print("noise for pa=",pa1[i]," and pb=",pb1[i]," is = " ,int(baboon.shape[0]*baboon.shape[1]*pa1[i]),",",int(baboon.shape[0]*baboon.shape[1]*pb1[i]))

    picCopy=baboon.copy()

    for i in range(amount1):
        picCopy[np.random.randint(0,baboon.shape[0]-1), np.random.randint(0,baboon.shape[1]-1)]=0

    for i in range(amount2):
        picCopy[np.random.randint(0,baboon.shape[0]-1), np.random.randint(0,baboon.shape[1]-1)]=255

    return picCopy

def main():
    mean = 0
    sigma = 100
    pa = 0.01
    pb = 0.01

    input_img = "baboon.jpg"
    baboon = cv2.imread(input_img)
    gray_img = cv2.cvtColor(baboon,cv2.COLOR_BGR2GRAY)
    cv2.imshow("./baboonGray.jpg",gray_img)

    gaussianImg = gaussian_Noise(gray_img,mean,sigma)
    cv2.imshow("./gaussianNoise.png",gaussianImg)
    boxFilterImg = cv2.boxFilter(gaussianImg, -1, (3, 3))
    cv2.imshow("./gaussianBoxfilter.png",boxFilterImg)
    gaussFilterImg=cv2.GaussianBlur(gaussianImg, (3,3), 1.5, 3)
    cv2.imshow("./gaussianGaussfilter.png",gaussFilterImg)
    medianFilterImg=cv2.medianBlur(gaussianImg,5)
    cv2.imshow("./gaussianMedianfilter.png",medianFilterImg)

    pepperSaltImg=salt_pepper_Noise(gray_img,pa,pb)
    cv2.imshow("./peppersaltnoise.png",pepperSaltImg)
    boxFilterImg = cv2.boxFilter(pepperSaltImg, -1, (3, 3))
    cv2.imshow("./peppersaltBoxfilter.png",boxFilterImg)
    gaussFilterImg=cv2.GaussianBlur(pepperSaltImg, (3,3), 1.5, 3)
    cv2.imshow("./peppersaltGaussfilter.png",gaussFilterImg)
    medianFilterImg=cv2.medianBlur(pepperSaltImg,5)
    cv2.imshow("./peppersaltMedianfilter.png",medianFilterImg)

    noisyPic_forprint = baboon.copy()
    print(cv2.randn(noisyPic_forprint,0,0))
    print(cv2.randn(noisyPic_forprint,5,20))
    print(cv2.randn(noisyPic_forprint,10,50))
    print(cv2.randn(noisyPic_forprint,20,100))

    cv2.waitKey(0)

if __name__ == "__main__":
    main()