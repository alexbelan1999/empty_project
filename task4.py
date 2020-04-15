import face_recognition
from PIL import Image, ImageDraw

file = "testphoto/bill_elon_steve1.jpg"
image = face_recognition.load_image_file(file)
face_landmarks_list = face_recognition.face_landmarks(image)
print("Лиц на фото: {}.".format(len(face_landmarks_list)))

pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:

    for facial_feature in face_landmarks.keys():
        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    for facial_feature in face_landmarks.keys():
        d.line(face_landmarks[facial_feature], width=5)

#pil_image.save("test.jpg")
pil_image.show()
