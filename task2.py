import face_recognition

image = face_recognition.load_image_file("testphoto/bill_elon_steve1.jpg")
face_locations = face_recognition.face_locations(image)
print("Лиц на фото: {}.".format(len(face_locations)))

for face_location in face_locations:
    top, right, bottom, left = face_location
    print("Расположение лица на фото: Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
