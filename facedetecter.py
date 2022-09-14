import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#smiles_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
plates_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

def search_objects(file_path):
    img = cv2.imread(file_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.2, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face_gray = gray[y:y+h, x:x+w]
        face_color = img[y:y+h, x:x+w]

        eyes = eyes_cascade.detectMultiScale(face_gray, 1.2, 4)
        for (x, y, w, h) in eyes:
            cv2.rectangle(face_color, (x, y), (x + w, y + h), (0, 255, 0), 2)


    plates = plates_cascade.detectMultiScale(gray, 1.2, 4)
    for (x, y, w, h) in plates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imwrite(file_path, img)

    return open(file_path, "rb")