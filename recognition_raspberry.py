import recognition

class Face(recognition.Face):

    def __init__(self, list_known_images, sep_name="#", tolerance=0.55):
        super(Face, self).__init__(list_known_images, sep_name)

    # def raspberry_cam(self, size_frame=0.25):
    #     '''
    #     Recognize faces from camena raspberry
    #     :param size_frame: size frame
    #     :return:
    #     '''
    #
    #     # open webcam
    #     video_capture = cv2.VideoCapture(0)
    #
    #     if not video_capture.isOpened():
    #         print("Could not open webcam!")
    #         exit()
    #
    #     face_names = []
    #     process_this_frame = True
    #
    #     while True:
    #
    #         # Grab a single frame of video
    #         ret, frame = video_capture.read()
    #
    #         # Resize frame of video to 1/4 size for faster face recognition processing
    #         small_frame = cv2.resize(frame, (0, 0), fx=size_frame, fy=size_frame)
    #
    #         # Convert the unknown_image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    #         rgb_small_frame = small_frame[:, :, ::-1]
    #
    #         # Only process every other frame of video to save time
    #         if process_this_frame:
    #             face_names, face_locations, face_encodings, min_distance = self.comparison(rgb_small_frame)
    #         process_this_frame = not process_this_frame
    #
    #         self.format_results(frame, face_locations, face_names, min_distance, scale_back=4)
    #
    #         # Display the resulting unknown_image
    #         cv2.imshow('Video', frame)
    #
    #         # Hit 'q' on the keyboard to quit!
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break
    #
    #     # Release handle to the webcam
    #     video_capture.release()
    #     cv2.destroyAllWindows()