# # from flask import session
# # import keras
# # import cv2
# # import pickle
# # from tensorflow.keras.models import model_from_json
# # # from keras.preprocessing import img_to_array
# # from tensorflow.keras.utils import img_to_array
# # from keras.preprocessing.image import ImageDataGenerator
# # import numpy as np
# # import face_recognition
# # from datetime import datetime
# # from core import rec_face_image
# # from database import *
# # from keras import backend as K 


# # def camclick():
# #     K.clear_session()
# #     model = model_from_json(open(r"model\facial_expression_model_structure.json", "r").read())   
# #     model.load_weights(r'model\facial_expression_model_weights.h5') # load weights  
# #     face_cascade = cv2.CascadeClassifier(r'model\haarcascade_frontalface_default.xml')
# #     cap = cv2.VideoCapture(0)
# #     emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    
# #     while True:
# #         ret, img = cap.read()
# #         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #         faces = face_cascade.detectMultiScale(gray, 1.3, 5) #locations of detected faces
# #         emotion = None

# #         for (x, y, w, h) in faces:
# #             cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2) #draw rectangle to main image
# #             detected_face = img[int(y):int(y + h), int(x):int(x + w)] #crop detected face
# #             detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY) #transform to gray scale
# #             detected_face = cv2.resize(detected_face, (48, 48)) #resize to 48x48
# #             img_pixels = img_to_array(detected_face)
# #             img_pixels = np.expand_dims(img_pixels, axis=0)
# #             img_pixels /= 255 #pixels are in scale of [0, 255]. normalize all pixels in scale of [0, 1]
# #             predictions = model.predict(img_pixels) #store probabilities of 7 expressions
# #             #find max indexed array 0: angry, 1:disgust, 2:fear, 3:happy, 4:sad, 5:surprise, 6:neutral
# #             max_index = np.argmax(predictions[0])
# #             emotion = emotions[max_index]
# #             cv2.putText(img, emotion, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            
# #             # Save just the rectangle faces in SubRecFaces
# #             sub_face = img[y:y + h, x:x + w]
# #             FaceFileName = "static/test.jpg" #Saving the current image from the webcam for testing.
# #             print("FaceFileName : ", FaceFileName)
# #             cv2.imwrite(FaceFileName, sub_face)
# #             val = rec_face_image(FaceFileName)
# #             print("user", val)
# #             str1 = ""
# #             for ele in val:  
# #                 str1 = ele
# #                 print(str1)
# #                 val = str1.replace("'", "")
# #                 print("val : ", val)
# #             print(emotion)
        
# #         # Show the image and check for the 'q' key press to quit
# #         cv2.imshow('img', img)
# #         if cv2.waitKey(1) & 0xFF == ord('q'): 
# #             break

# #     cap.release()
# #     cv2.destroyAllWindows()
# #     K.clear_session()
# #     return emotion #write emotion text above rectangle


# # # recognize face image
# # def rec_face_image(imagepath):
# #     print("...........",imagepath)
# #     data = pickle.loads(open('faces.pickles', "rb").read())
# #     print("DATA : ",data)

# #     # load the input image and convert it from BGR to RGB
# #     image = cv2.imread(imagepath)
# #     print("image : ", image)
# #     h,w,ch=image.shape
# #     print("CH : ",ch)
# #     rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# #     print("RGB : ",rgb)

# #     # detect the (x, y)-coordinates of the bounding boxes corresponding
# #     # to each face in the input image, then compute the facial embeddings
# #     # for each face

# #     print("[INFO] recognizing faces...")
# #     boxes = face_recognition.face_locations(rgb,model='hog')
# #     encodings = face_recognition.face_encodings(rgb, boxes)
# #     print("encodings : ",encodings)

# #     # initialize the list of names for each face detected
# #     names = []

# #     # loop over the facial embeddings
# #     for encoding in encodings:
# #         # attempt to match each face in the input image to our known
# #         # encodings
# #         matches = face_recognition.compare_faces(data["encodings"],
# #             encoding,tolerance=0.4)
# #         print("matches : ",matches)
# #         name = "Unknown"

# #         # check to see if we have found a match
# #         if True in matches:
# #             # find the indexes of all matched faces then initialize a
# #             # dictionary to count the total number of times each face
# #             # was matched
# #             matchedIdxs = [i for (i, b) in enumerate(matches) if b]
# #             counts = {}

# #             # loop over the matched indexes and maintain a count for
# #             # each recognized face face
# #             for i in matchedIdxs:
# #                 name = data["names"][i]
# #                 counts[name] = counts.get(name, 0) + 1
# #             print(counts, " rount ")
# #             # determine the recognized face with the largest number of
# #             # votes (note: in the event of an unlikely tie Python will
# #             # select first entry in the dictionary)
# #             if len(counts) == 1:
# #                 name = max(counts, key=counts.get)
# #             else:
# #                 name = "-1"
# #         # update the list of names
# #         # if name not in names:
# #         if name != "Unknown":
# #             names.append(name)
# #     return names






# from flask import session
# import cv2
# import pickle
# from tensorflow.keras.models import model_from_json
# from tensorflow.keras.utils import img_to_array
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# import numpy as np
# import face_recognition
# from datetime import datetime
# from core import rec_face_image
# from database import *
# from keras import backend as K  # Clear session properly

# def camclick():
#     # Clear previous Keras session to free up memory
#     K.clear_session()

#     # Load the facial expression model
#     model = model_from_json(open(r"model\facial_expression_model_structure.json", "r").read())
#     model.load_weights(r'model\facial_expression_model_weights.h5')  # Load weights

#     # Load the face cascade for face detection
#     face_cascade = cv2.CascadeClassifier(r'model\haarcascade_frontalface_default.xml')

#     # Open the webcam feed
#     cap = cv2.VideoCapture(0)
#     emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

#     while True:
#         # Capture frame-by-frame
#         ret, img = cap.read()
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         # Detect faces in the image
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#         emotion = None
#         for (x, y, w, h) in faces:
#             # Draw rectangle around the face
#             cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

#             # Crop the face from the image
#             detected_face = img[int(y):int(y + h), int(x):int(x + w)]
#             detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
#             detected_face = cv2.resize(detected_face, (48, 48))  # Resize to 48x48

#             # Normalize the image
#             img_pixels = img_to_array(detected_face)
#             img_pixels = np.expand_dims(img_pixels, axis=0)
#             img_pixels /= 255  # Normalize to [0, 1]

#             # Make prediction
#             predictions = model.predict(img_pixels)
#             max_index = np.argmax(predictions[0])  # Get the index of the highest prediction
#             emotion = emotions[max_index]  # Map the index to the emotion

#             # Put emotion text above the face
#             cv2.putText(img, emotion, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

#             # Save the face image
#             sub_face = img[y:y + h, x:x + w]
#             FaceFileName = "static/test.jpg"  # Saving the current image from the webcam
#             cv2.imwrite(FaceFileName, sub_face)

#             # Recognize the face
#             val = rec_face_image(FaceFileName)
#             str1 = ""
#             for ele in val:
#                 str1 = ele
#                 val = str1.replace("'", "")  # Clean the value
#             print("Recognized User: ", val)

#         # Show the image
#         cv2.imshow('img', img)

#         # Quit on 'q' key press
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release resources and close windows
#     cap.release()
#     cv2.destroyAllWindows()

#     # Clear Keras session again
#     K.clear_session()

#     return emotion

# # Face recognition function
# def rec_face_image(imagepath):
#     print("Processing image:", imagepath)

#     # Load the face encoding data
#     data = pickle.loads(open('faces.pickles', "rb").read())
#     print("Loaded data:", data)

#     # Load the image and convert it to RGB
#     image = cv2.imread(imagepath)
#     rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # Detect faces in the image
#     print("[INFO] Recognizing faces...")
#     boxes = face_recognition.face_locations(rgb, model='hog')
#     encodings = face_recognition.face_encodings(rgb, boxes)

#     names = []

#     for encoding in encodings:
#         # Compare the detected face with known faces
#         matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance=0.4)
#         name = "Unknown"

#         if True in matches:
#             matchedIdxs = [i for (i, b) in enumerate(matches) if b]
#             counts = {}

#             # Count the number of times each face matches
#             for i in matchedIdxs:
#                 name = data["names"][i]
#                 counts[name] = counts.get(name, 0) + 1

#             # Get the name with the most votes
#             if len(counts) == 1:
#                 name = max(counts, key=counts.get)
#             else:
#                 name = "-1"

#         # Add name to the list if not "Unknown"
#         if name != "Unknown":
#             names.append(name)

#     return names


from flask import session
import cv2
import pickle
from tensorflow.keras.models import model_from_json
from tensorflow.keras.utils import img_to_array
import numpy as np
import face_recognition
from keras import backend as K  # Clear session properly

def camclick():
    # Clear previous Keras session to free up memory
    K.clear_session()

    # Load the facial expression model
    with open(r"model\facial_expression_model_structure.json", "r") as json_file:
        model = model_from_json(json_file.read())
    model.load_weights(r'model\facial_expression_model_weights.h5')  # Load weights

    # Load the face cascade for face detection
    face_cascade = cv2.CascadeClassifier(r'model\haarcascade_frontalface_default.xml')

    # Open the webcam feed
    cap = cv2.VideoCapture(0)
    emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

    while True:
        # Capture frame-by-frame
        ret, img = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        emotion = None
        for (x, y, w, h) in faces:
            # Draw rectangle around the face
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Crop the face from the image
            detected_face = img[y:y + h, x:x + w]
            detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
            detected_face = cv2.resize(detected_face, (48, 48))  # Resize to 48x48

            # Normalize the image
            img_pixels = img_to_array(detected_face)
            img_pixels = np.expand_dims(img_pixels, axis=0)
            img_pixels /= 255  # Normalize to [0, 1]

            # Make prediction
            predictions = model.predict(img_pixels)
            max_index = np.argmax(predictions[0])  # Get the index of the highest prediction
            emotion = emotions[max_index]  # Map the index to the emotion

            # Put emotion text above the face
            cv2.putText(img, emotion, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            # Save the face image
            FaceFileName = "static/test.jpg"  # Saving the current image from the webcam
            cv2.imwrite(FaceFileName, detected_face)

            # Recognize the face
            val = rec_face_image(FaceFileName)
            if val:
                recognized_user = val[0].replace("'", "")  # Clean the value
                print("Recognized User: ", recognized_user)

        # Show the image
        cv2.imshow('img', img)

        # Quit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources and close windows
    cap.release()
    cv2.destroyAllWindows()

    # Clear Keras session again
    K.clear_session()

    return emotion

# Face recognition function
def rec_face_image(imagepath):
    print("Processing image:", imagepath)

    # Load the face encoding data
    with open('faces.pickles', "rb") as f:
        data = pickle.load(f)
    print("Loaded data:", data)

    # Load the image and convert it to RGB
    image = cv2.imread(imagepath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect faces in the image
    print("[INFO] Recognizing faces...")
    boxes = face_recognition.face_locations(rgb, model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)

    names = []

    for encoding in encodings:
        # Compare the detected face with known faces
        matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance=0.4)
        name = "Unknown"

        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            # Count the number of times each face matches
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            # Get the name with the most votes
            if len(counts) == 1:
                name = max(counts, key=counts.get)
            else:
                name = "-1"

        # Add name to the list if not "Unknown"
        if name != "Unknown":
            names.append(name)

    return names
