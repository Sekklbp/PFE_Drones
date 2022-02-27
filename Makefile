
live1:
	python3 yolov5/detect.py --weights /yolov5/best.pt --source 0

live2:
	python3 yolov5/detect.py --weights /yolov5/best.pt --source 

train2:
	
	python3 yolov5/train.py --img 640 --batch 16 --epochs 15 --data my-drone.yaml --weights yolov5/data/base_weights/best.pt
	

detect_video:
	python3 yolov5/detect.py --weights yolov5/best.pt --source yolov5/data/videos/output.avi

detect_drone_photo:
	python3 yolov5/detect_1.py --weights yolov5/best.pt 

train1:
	
	python3 yolov5/train.py --img 640 --batch 16 --epochs 2 --data my-drone.yaml --weights yolov5/data/base_weights/best.pt
