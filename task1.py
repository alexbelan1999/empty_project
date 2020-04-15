import face_recognition

image = face_recognition.load_image_file("testphoto/bill_elon_steve1.jpg")
face_locations = face_recognition.face_locations(image)
print("Лиц на фото: {}.".format(len(face_locations)))
