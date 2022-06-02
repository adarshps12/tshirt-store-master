# import time
#
# import cv2
# import numpy as np
# import face_recognition
# import os
#
# # import serial
# # arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
# # def write_read(x):
# #     arduino.write(bytes(x, 'utf-8'))
# #     time.sleep(0.05)
# #     data = arduino.readline()
# #     return data
# from django.shortcuts import redirect, render
#
#
# def face_detect(source):
#     path = '../Training images'
#     images = []
#     classNames = []
#     myList = os.listdir(path)
#     print(myList)
#     for cl in myList:
#         curImg = cv2.imread(f'{path}/{cl}')
#         images.append(curImg)
#         classNames.append(os.path.splitext(cl)[0])
#     print(classNames)
#     print(type(classNames))
#
#     def findEncodings(images):
#         encodeList = []
#
#         for img in images:
#             img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#             encode = face_recognition.face_encodings(img)[0]
#             encodeList.append(encode)
#         return encodeList
#
#     encodeListKnown = findEncodings(images)
#     print('Encoding Complete')
#
#     cap = cv2.VideoCapture(0)
#
#     while True:
#         success, img = cap.read()
#         # img = captureScreen()
#         imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#         imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
#
#         facesCurFrame = face_recognition.face_locations(imgS)
#         encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
#
#         for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
#             matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#             faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#             print(faceDis)
#             matchIndex = np.argmin(faceDis)
#             print(matchIndex)
#
#             if matches[matchIndex]:
#                 name = classNames[matchIndex].upper()
#                 # print(name)
#                 y1, x2, y2, x1 = faceLoc
#                 y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#                 cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                 cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#                 cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#                 # if (label == 0):
#                 #     num = 'MY'
#                 #     value = write_read(num)
#                 #     break
#                 # elif (label == 1):
#                 #     num = 'NM'
#                 #     value = write_read(num)
#                 #     break
#
#         cv2.imshow('Webcam', img)
#         if cv2.waitKey(1) == ord("q"):
#             break
#         return redirect('orders')
#
#
# def details(request):
#     return render(request, 'cam_open.html')
