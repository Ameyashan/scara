import cv2
from time import sleep
import os

def get_image_saving_path() : 
	#print(os.getcwd())
	path = (os.getcwd().split('\\'))
	path.append('Pictures')
	return_path = ''
	for element in path : 
		return_path += element + '\\'
	path = return_path
	return path

IMAGE_SAVING_PATH = get_image_saving_path()

def image_gen(number_of_images=100):
        camera_port=0  
        #Number of frames to throw away while the camera adjusts to light levels
        ramp_frames = 30
                
        # Now we can initialize the camera capture object with the cv2.VideoCapture class.
        # All it needs is the index to a camera port.
        camera = cv2.VideoCapture(camera_port)
        # Camera 0 is the integrated web cam on my netbook
        
        def get_image():
                retval, im = camera.read()
                return im

      # Ramp the camera - these frames will be discarded and are only used to allow v4l2
     # to adjust light levels, if necessary
        for i in xrange(ramp_frames):
                temp = get_image()
        # print("Taking image...")
     # Take the actual image we want to keep
        for i in range(number_of_images):
                camera_capture = get_image()
                file = IMAGE_SAVING_PATH + "test_image" +str(i)+ ".png"
                cv2.imwrite(file, camera_capture)
                # sleep(0.2)
          # sleep(0.5)
     # A nice feature of the imwrite method is that it will automatically choose the
     ######
      
     # You'll want to release the camera, otherwise you won't be able to create a new
     # capture object until your script exits

