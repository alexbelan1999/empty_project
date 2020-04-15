import face_recognition

bill_image = face_recognition.load_image_file("person/Bill_Gates.jpg")
unknown_image = face_recognition.load_image_file("testphoto/Bill_Gates01.jpg")

try:
    bill_face_encoding = face_recognition.face_encodings(bill_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("IndexError")
    quit()

known_faces = [
    bill_face_encoding
]

results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Это Bill Gates? {}".format(results[0]))
