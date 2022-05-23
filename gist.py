import numpy as np
import cv2 as cv2
import sys
import mediapipe as mp

class matchbox():
    def __init__(self,matches=4,nopes=2):
        self.matches=matches
        self.mopes=nopes

    def homie(self, img, coord, radii):
        newimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        black = np.zeros(img.shape,dtype=np.uint8)
        if newimg[coord[0]][coord[1]] <= 20:
            return black
        elif newimg[coord[0]][coord[1]] >= 230:
            cv2.circle(black,(coord[1],coord[0]),radii, (255, 255, 255), thickness=cv2.FILLED)
            black=cv2.cvtColor(black, cv2.COLOR_BGR2GRAY)
            return cv2.cvtColor(cv2.bitwise_and(newimg, black),cv2.COLOR_GRAY2BGR)


def main():
    img = cv2.imread('maze.png')
    helper_func = matchbox()
    coord=[195,395]#manipulate coords and radii to check
    img1 = helper_func.homie(img,coord,100)
    cv2.imshow('Window', img1)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
