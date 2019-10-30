import recognition
import helper


path_out_images = 'sources_images/output/'
path_known_images = 'sources_images/known_people/'
path_unknow_images = 'sources_images/unknown/'
image_extension = "*.jpeg"
width_max_image = 800

# Make dirs if not exists
helper.make_dirs(path_out_images, True)
helper.make_dirs(path_known_images, True)
helper.make_dirs(path_unknow_images, True)

list_known_images = helper.get_files_dir(path_known_images, image_extension)


face_recog = recognition.Face(list_known_images)

face_recog.webcam_Test()

# list_images_unknow = helper.get_files_dir(path_unknow_images, image_extension)
# for img in list_images_unknow:
#     face_recog.process(img)



