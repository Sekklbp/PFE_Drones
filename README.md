# PFE_Drones
PFE Essaim de Drones

Dépot git sur le projet Essaim de Drones.
Expérimentations faites au Laboratoire Robotique Cristal à Lille.
Drones :  DJI Tello EDU

Langages : Python , C

Notebooks :
Essai_Yolo_NoteBook fichier essayant d'utiliser des fichiers de configuration et de poids yolo
EssaiEssaiEvitementObstacle première version d'un évitement d'obstacle naïf
SoloVideo permet de récupérer la vidéo live d'un drone
Video_to_photo permet de transformer les vidéos en ensemble de photos
MultiVideo aurait permit de capturer la vidéo de plusieurs drones en même temps
Photos_to_Video aurait permit de transformer les photos en vidéo
Remove_Empty_Labels permet de supprimer les images et les fichiers txt associés de labélisation là où il n'y a pas de drone, à ne pas utiliser si on a des photos anti Faux positif ( photos sans drone permettant d'entrainer la non détection )
Traitement_Image permet de faire les manipulation d'évitement d'obstacle naîf



Pour utiliser yolov5:
make <commande>
  train2 pour entrainer sur les images fournies un bon entrainement durant une petite heure
  detect_drone_photo detecte en temps réel les photos du drone , à finir
  detect_video detecte sur une video
  live1 detecte sur la webcam
  live2 commande incomplète pouvant potentiellement permettre de faire sur la caméra du drone
  
 best.pt est le fichier de poids
 my-drone.yaml dans data permet de spécifier l'emplacement des images d'entrainements

Pistes d'amélioration :
Envoyer les commandes directement au drone via des messages UDP -> meilleure précision et amplitude de mouvements
Essayer d'avoir la cméra en direct sur l'ordinateur
Essayer en laboratoire ( le code le plus récent n'a pas pû être testé )
