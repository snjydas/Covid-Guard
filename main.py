# import the necessary packages
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model
from imutils.video import VideoStream,FileVideoStream
import imutils
import numpy as np
import time
import os
import cv2
import math


def mainc():

	scale_percent = 20 # percentage of original size
	width = 0
	height = 0

	labelsPath = "Model/coco.names" #path for model
	LABELS = open(labelsPath).read().strip().split("\n")

	np.random.seed(42)
	COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
		dtype="uint8")

	weightsPath = "Model/yolov3.weights" #path for yolov3 weights
	configPath = "Model/yolov3.cfg" #path for yolov3 configuration file

	net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

	cap = cv2.VideoCapture(0)
	if not cap.isOpened():
		print("Could not open webcam")
		exit()
	else: #get dimension info
		width =  int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		dim = (width, height)
		print('Original Dimensions : ',dim)
		width = int(width * scale_percent / 100)
		height = int(height * scale_percent / 100)
		dim = (width, height)
		print('Resized Dimensions : ', dim)


	def detect_and_predict_mask(frame, faceNet, maskNet):
		# grab the dimensions of the frame and then construct a blob from it
		(h, w) = frame.shape[:2]
		blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
			(104.0, 177.0, 123.0))
		# pass the blob through the network and obtain the face detections
		faceNet.setInput(blob)
		detections = faceNet.forward()
		# initialize our list of faces, their corresponding locations,
		# and the list of predictions from our face mask network
		faces = []
		locs = []
		preds = []


		# loop over the detections
		for i in range(0, detections.shape[2]):
			# extract the confidence (i.e., probability) associated with
			# the detection
			confidence = detections[0, 0, i, 2]
			# filter out weak detections by ensuring the confidence is
			# greater than the minimum confidence
			if confidence > 0.5:
				# compute the (x, y)-coordinates of the bounding box for
				# the object
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")
				# ensure the bounding boxes fall within the dimensions of
				# the frame
				(startX, startY) = (max(0, startX), max(0, startY))
				(endX, endY) = (min(w - 1, endX), min(h - 1, endY))


				# extract the face ROI, convert it from BGR to RGB channel
				# ordering, resize it to 224x224, and preprocess it
				face = frame[startY:endY, startX:endX]
				face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
				face = cv2.resize(face, (224, 224))
				face = img_to_array(face)
				face = preprocess_input(face)
				# add the face and bounding boxes to their respective
				# lists
				faces.append(face)
				locs.append((startX, startY, endX, endY))


		# only make a predictions if at least one face was detected
		if len(faces) > 0:
			# for faster inference we'll make batch predictions on *all*
			# faces at the same time rather than one-by-one predictions
			# in the above `for` loop
			faces = np.array(faces, dtype="float32")
			preds = maskNet.predict(faces, batch_size=32)
		# return a 2-tuple of the face locations and their corresponding
		# locations
		return (locs, preds)



	base_dir=os.getcwd()
	base_dir=base_dir.replace('\\','/')

	print(base_dir)
	dataset_path=base_dir+'/dataset'
	accuracy_plot_dir=base_dir+'/Model'
	model_store_dir=base_dir+'/Model/mask_detector.model'
	example=base_dir+'/Image/1.jpg'

	confidence=0.4


	face_detector_caffe=base_dir+'/Face Detector/res10_300x300_ssd_iter_140000.caffemodel'



	# load our serialized face detector model from disk
	print("[INFO] loading face detector model...")
	prototxtPath = base_dir+'/Face Detector/deploy.prototxt'
	weightsPath = face_detector_caffe
	faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)
	# load the face mask detector model from disk
	print("[INFO] loading face mask detector model...")
	maskNet = load_model(model_store_dir)
	# initialize the video stream and allow the camera sensor to warm up
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	#time.sleep(2.0)







	# loop over the frames from the video stream
	iter=0
	while True:



		# grab the frame from the threaded video stream and resize it
		# to have a maximum width of 400 pixels
		frame = vs.read()
		frame = imutils.resize(frame, width=1200)

		resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

		(H, W) = frame.shape[:2]
		ln = net.getLayerNames()
		ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
		blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (224, 224), swapRB=True, crop=False)
		net.setInput(blob)
		start = time.time()
		layerOutputs = net.forward(ln)
		end = time.time()
		# print("Frame Prediction Time : {:.6f} seconds".format(end - start))
		boxes = []
		confidences = []
		classIDs = []

		for output in layerOutputs:
			for detection in output:
				scores = detection[5:]
				classID = np.argmax(scores)
				confidence = scores[classID]
				if confidence > 0.1 and classID == 0:
					box = detection[0:4] * np.array([W, H, W, H])
					(centerX, centerY, width, height) = box.astype("int")
					x = int(centerX - (width / 2))
					y = int(centerY - (height / 2))
					boxes.append([x, y, int(width), int(height)])
					confidences.append(float(confidence))
					classIDs.append(classID)

		if iter % 3 == 0:

			idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)
			ind = []
			for i in range(0, len(classIDs)):
				if (classIDs[i] == 0):
					ind.append(i)
			a = []
			b = []

			if len(idxs) > 0:
				for i in idxs.flatten():
					(x, y) = (boxes[i][0], boxes[i][1])
					(w, h) = (boxes[i][2], boxes[i][3])
					a.append(x)
					b.append(y)

			distance = []
			nsd = []
			for i in range(0, len(a) - 1):
				for k in range(1, len(a)):
					if (k == i):
						break
					else:
						x_dist = (a[k] - a[i])
						y_dist = (b[k] - b[i])
						d = math.sqrt(x_dist * x_dist + y_dist * y_dist)
						distance.append(d)
						if (d <= 6912):
							nsd.append(i)
							nsd.append(k)
						nsd = list(dict.fromkeys(nsd))
					# print(nsd)

			color = (0, 0, 255)
			for i in nsd:
				(x, y) = (boxes[i][0], boxes[i][1])
				(w, h) = (boxes[i][2], boxes[i][3])
				cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
				text = "Alert"
				cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
			color = (0, 255, 0)
			if len(idxs) > 0:
				for i in idxs.flatten():
					if (i in nsd):
						break
					else:
						(x, y) = (boxes[i][0], boxes[i][1])
						(w, h) = (boxes[i][2], boxes[i][3])
						cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
						text = 'OK'
						cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

		text = "Social Distancing Violators: {}".format(len(nsd))
		cv2.putText(frame, text, (660, frame.shape[0] - 45),
					cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)

		cv2.putText(frame, "Covid Guard: Team TrojanWave", (140, 45),
					cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
		cv2.rectangle(frame, (20, 60), (1170, 100), (170, 170, 170), 2)
		cv2.putText(frame, "COLOR CODE: RISK ANALYSIS", (30, 85),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
		cv2.putText(frame, "--- GREEN : SAFE", (500, 85),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
		cv2.putText(frame, "--- RED: UNSAFE", (1000, 85),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)


		tot_str = "TOTAL: " + str(len(idxs))
		high_str = "HIGH RISK: " + str(len(nsd))
		low_str = "LOW RISK: " + str(0)
		safe_str = "SAFE: " + str(len(idxs)-len(nsd))

		sub_img = frame[H - 270: H , 0:240]
		black_rect = np.ones(sub_img.shape, dtype=np.uint8) * 0

		res = cv2.addWeighted(sub_img, 0.8, black_rect, 0.2, 1.0)

		frame[H - 270:H, 0:240] = res

		cv2.putText(frame, tot_str, (10, H - 235),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
		cv2.putText(frame, safe_str, (10, H - 200),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
		cv2.putText(frame, low_str, (10, H - 165),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 120, 255), 2)
		cv2.putText(frame, high_str, (10, H - 130),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 150), 2)

		#cv2.imshow("Social Distancing Detector", frame)

		cv2.rectangle(frame, (10, H-100 ), (600, H-10), (170, 170, 170), 2)
		cv2.putText(frame, "COLOR CODE: MASK DETECTION", (40, H-40),
					cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
		cv2.putText(frame, "--- RED : NO MASK", (420, H-70),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
		cv2.putText(frame, "--- GREEN : MASK", (420, H-35),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

		# cv2.putText(frame, "--    GREEN: SAFE", (565, 150),
		# 			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

		# detect faces in the frame and determine if they are wearing a
		# face mask or not
		(locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

		# loop over the detected face locations and their corresponding
		# locations
		for (box, pred) in zip(locs, preds):
			# unpack the bounding box and predictions
			(startX, startY, endX, endY) = box
			(mask, withoutMask) = pred
			# determine the class label and color we'll use to draw
			# the bounding box and text
			label = "Mask" if mask > withoutMask else "No Mask"
			color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
			# include the probability in the label
			label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
			# display the label and bounding box rectangle on the output
			# frame
			cv2.putText(frame, label, (startX, startY - 10),
				cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
			cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)


		# show the output frame
		cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
		cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
		cv2.imshow('frame', frame)
		key = cv2.waitKey(1) & 0xFF
		# if the `q` key was pressed, break from the loop

	
		if key == ord("q"):
			break



	# do a bit of cleanup
	cv2.destroyAllWindows()
	vs.stop()

