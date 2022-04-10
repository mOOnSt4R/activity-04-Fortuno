import cv2
from tkinter import filedialog, Tk

root = Tk()
root.withdraw()
filepath = filedialog.askopenfilename()

print("Select image flag")
print("1. color")
print("2. grayscale")
print("3. unchange")

flagInput = int(input())

if flagInput == 1:
    flag = 1
elif  flagInput == 2:
    flag = 0
elif flagInput == 3: 
    flag = -1
else: 
    flag = 1

cv2.startWindowThread()
image = cv2.imread(filepath, flag)
cv2.imshow("Show Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()