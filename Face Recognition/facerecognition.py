import cv2, os

wajahdir = 'datawajah'

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640) # mengatur lebar 
cam.set(4, 480) # mengatur tinggi
faceDetector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeDetector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
faceId = input('Masukkan Face ID wajah ini : ')
print('Tatap mata saya, tunggu sampai proses selesai..')
ambildata = 1

while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5) #frame, scaleFaktor, minNeighbors
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)

        namafile = 'wajah.'+str(faceId)+'.'+str(ambildata)+'.jpg'
        cv2.imwrite(wajahdir + '/' + namafile, frame)
        ambildata += 1
        roiAbuAbu = abuAbu[y:y+h, x:x+w]
        roiWarna = frame[y:y+h, x:x+w]

        eyes = eyeDetector.detectMultiScale(roiAbuAbu)
        for (xe, ye, we, he) in eyes:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

    cv2.imshow('frame', frame)

    tombol = cv2.waitKey(1) & 0xFF
    if tombol == 27 or tombol == ord('q'):
        break
    elif ambildata > 30:
        break

print('Pengambilan data selesai')
cam.release()
cv2.destroyAllWindows()