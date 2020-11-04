import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
y = 0
total_list = []
corr = []
img = cv2.imread("C:\Sid\Projects\Segmentation\img2.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.convertScaleAbs(img, alpha=1.5, beta=0)
#cong = r'--oem 3 --psm 6 outputbase digitsC:\Sid\Projects\Segmentation\overlay.jpg'
hImg, wImg, channels = img.shape
boxes = pytesseract.image_to_data(img)

for x,b in enumerate(boxes.splitlines()):
    if x!= 0:
        b = b.split()
        if len(b) == 12:
            total_list.append(b)


num = 0
for i in total_list:
    if i[11].isdigit() and len(i[11]) == 4:
        if total_list[num+1][11].isdigit() and len(total_list[num+1][11]) == 4:
            if total_list[num+2][11].isdigit() and len(total_list[num+1][11]) == 4:
                for j in range(num, num+2):
                    b = total_list[j]
                    x,y,w,h = int(b[6]), int(b[7]),int(b[8]),int(b[9])
                    cv2.rectangle(img, (x,y), (w+x, h+y), (255,0,0), -1)
                    num2 = num

    num += 1

print("Your AADHAR number is " + total_list[num2][11] + total_list[num2+1][11] + total_list[num2+2][11])
#blurred_img = cv2.GaussianBlur(img, (21,21), 0)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imshow("result", img)
cv2.waitKey(0)
