import recognition
import picamera
import numpy as np
import cv2

class Face(recognition.Face):

    def __init__(self, list_known_images, sep_name="#", tolerance=0.55):
        super(Face, self).__init__(list_known_images, sep_name)

    def camera(self, resolution=(320, 240)):
        '''
        Recognize faces from camera raspberry
        :param resolution: image resolution (tuple (width, height))
        :return:
        '''

        # Get a reference to the Raspberry Pi camera.
        # If this fails, make sure you have a camera connected to the RPi and that you
        # enabled your camera in raspi-config and rebooted first.
        camera = picamera.PiCamera()
        camera.resolution = resolution
        output = np.empty((resolution[1], resolution[0], 3), dtype=np.uint8)

        face_names = []
        process_this_frame = True

        while True:

            # Grab a single frame of video
            camera.capture(output, format="rgb")

            # Only process every other frame of video to save time
            if process_this_frame:
                face_names, face_locations, face_encodings, min_distance = self.comparison(output)
            process_this_frame = not process_this_frame

            self.format_results(output, face_locations, face_names, min_distance, scale_back=4)

            # Display the resulting unknown_image
            cv2.imshow('Video', output)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle
        # cv2.destroyAllWindows()