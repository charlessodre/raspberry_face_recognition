import face_recognition
import numpy as np
import cv2
import os


class FaceRecognize(object):

    def __init__(self, list_known_images, sep_name="#", tolerance=0.55):

        self.known_face_encodings, self.known_face_names = self.get_list_face_encodings_and_names(list_known_images,
                                                                                                  sep_name)
        self.tolerance = tolerance

        if len(self.known_face_encodings) == 0:
            exit('No Known images found!')

    def get_list_face_encodings_and_names(self, list_known_images, sep_name):
        '''
        # Get list know images
        :param list_known_images: List of images known
        :param sep_name: Image name separator
        :return: Return Face Encodings and Face names list
        '''

        known_face_encodings = []
        known_face_names = []

        for img_know in list_known_images:
            image_load = face_recognition.load_image_file(img_know)
            if len(face_recognition.face_encodings(image_load)) > 0:
                known_face_encoding = face_recognition.face_encodings(image_load)[0]
                known_face_encodings.append(known_face_encoding)
                known_face_names.append(img_know.split(os.sep)[-1].split(sep_name)[0].capitalize())

        return known_face_encodings, known_face_names

    def format_results(self, unknown_image, face_locations, face_names, distance, scale_back=1):
        '''
        Format results
        :param unknown_image: image for face recognition
        :param face_locations: face location list
        :param face_names: face names list
        :param distance: min distance from face
        :param scale_back: restore frame scale size
        :return:
        '''
        text_height = 1
        font = cv2.FONT_HERSHEY_PLAIN
        color_rect = (0, 255, 0)
        color_font = (0, 0, 0)

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detect if was scaled.
            top *= scale_back
            right *= scale_back
            bottom *= scale_back
            left *= scale_back

            if name == "Unknown":
                # color in GBR
                color_rect = (0, 0, 255)
                color_font = (255, 255, 255)

            # draw rectangle over face
            cv2.rectangle(unknown_image, (left, top), (right, bottom), color_rect, 1)

            # draw rectangle to put name
            cv2.rectangle(unknown_image, (left, int(bottom - text_height - 12)), (right, bottom), color_rect, -1)

            # put recognized unknown_image name
            cv2.putText(unknown_image, name, (left + 5, bottom - 2), font, text_height, color_font)

            # put distance over unknown_image
            cv2.putText(unknown_image, "distance {:.2}".format(distance), (left + 5, top - 5),
                        font, text_height, (0, 255, 255))

    def comparison(self, unknown_image):
        '''
        Recognize faces in unknown image
        :param unknown_image: image for face recognition
        :return: face_names, face_locations, face_encodings, min_distance
        '''
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

        face_names = []
        min_distance = None

        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=self.tolerance)
            name = "Unknown"

            # use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            min_distance = face_distances[best_match_index]

            face_names.append(name)

        return face_names, face_locations, face_encodings, min_distance

    def webcam(self, size_frame=0.25):
        '''
        Recognize faces from webcam
        :param size_frame: size frame
        :return:
        '''

        # open webcam
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            print("Could not open webcam!")
            exit()

        face_names = []
        process_this_frame = True

        while True:

            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=size_frame, fy=size_frame)

            # Convert the unknown_image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                face_names, face_locations, face_encodings, min_distance = self.comparison(rgb_small_frame)
            process_this_frame = not process_this_frame

            self.format_results(frame, face_locations, face_names, min_distance, scale_back=4)

            # Display the resulting unknown_image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

    def process(self, unknown_image_file, show=True, save=False, path_output=None):
        '''
        Recognize faces from unknown image files
        :param unknown_image_file:  File image for face recognition
        :param show: Show recognition results
        :param save: Save recognition results
        :param path_output: Path to save recognition results
        :return:
        '''

        # Load an image with an unknown face
        unknown_image = face_recognition.load_image_file(unknown_image_file)

        face_names, face_locations, face_encodings, min_distance = self.comparison(unknown_image)

        # Convert the unknown_image from RGB color to BGR color.
        unknown_image_BGR = cv2.cvtColor(unknown_image, cv2.COLOR_RGB2BGR)

        self.format_results(unknown_image_BGR, face_locations, face_names, min_distance)

        # display output (convert RGB to GBR)
        if show:
            cv2.imshow("Face Recognized", unknown_image_BGR)
            # press any key to close window
            cv2.waitKey()

        # save image with recognize name
        if save:
            # get image name into current_file
            current_file_name = unknown_image.split(os.sep)[-1]
            cv2.imwrite(path_output + current_file_name, unknown_image_BGR)

        # release resources
        cv2.destroyAllWindows()





