import tkinter as tk
import cv2


window = tk.Tk()
window.title("Face Auth")
window.geometry("400x400")


def take_photo():
	camera_port = 0 
	ramp_frames = 30 
	camera = cv2.VideoCapture(camera_port)

	def get_image():
		retval, im = camera.read()
		return im 
	for i in range(ramp_frames):
		temp = camera.read()

	camera_capture = get_image()
	filename = "image.jpg"
	cv2.imwrite(filename,camera_capture)
	del(camera)


b1 = tk.Button(window, text='take photo', command=take_photo)
b1.pack()


window.mainloop()






