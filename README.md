# PFE_Drones
PFE Essaim de Drones<br/>

Dépot git sur le projet Essaim de Drones.<br/>
Expérimentations faites au Laboratoire Robotique Cristal à Lille.<br/>
Drones :  DJI Tello EDU<br/>

Langages : Python , C<br/>

Notebooks :<br/>
Essai_Yolo_NoteBook fichier essayant d'utiliser des fichiers de configuration et de poids yolo<br/>
EssaiEssaiEvitementObstacle première version d'un évitement d'obstacle naïf<br/>
SoloVideo permet de récupérer la vidéo live d'un drone<br/>
Video_to_photo permet de transformer les vidéos en ensemble de photos<br/>
MultiVideo aurait permit de capturer la vidéo de plusieurs drones en même temps<br/>
Photos_to_Video aurait permit de transformer les photos en vidéo<br/>
Remove_Empty_Labels permet de supprimer les images et les fichiers txt associés de labélisation là où il n'y a pas de drone, à ne pas utiliser si on a des photos anti Faux positif ( photos sans drone permettant d'entrainer la non détection )<br/>
Traitement_Image permet de faire les manipulation d'évitement d'obstacle naîf<br/>

process.py permet de séparer les photos en train et en test<br/>
train_val_generator permet de faire pareil mais adapté à yolov5<br/>
yolov4 et yolov4 recording permettent d'analyser une vidéo ou une photo avec yolo<br/>


main de Yolo_annotation_tool_mastern permet de lancer le labelling d'image<br/>
appuyer sur le bouton b pour choisir un dossier<br/>
avoir un fichier classes.txt avec les classes à annoter<br/>
à lancer avec un terminal<br/>



Pour utiliser yolov5:<br/>
make <commande><br/>
  train2 pour entrainer sur les images fournies un bon entrainement durant une petite heure<br/>
  detect_drone_photo detecte en temps réel les photos du drone , à finir<br/>
  detect_video detecte sur une video<br/>
  live1 detecte sur la webcam<br/>
  live2 commande incomplète pouvant potentiellement permettre de faire sur la caméra du drone<br/>
  
 best.pt est le fichier de poids<br/>
 my-drone.yaml dans data permet de spécifier l'emplacement des images d'entrainements<br/>
  
Une fois un entrainement ou une detection finie, les résultats sont dans yolov5/runs/ detect ou train<br/>

Pistes d'amélioration :<br/>
Envoyer les commandes directement au drone via des messages UDP -> meilleure précision et amplitude de mouvements<br/>
Essayer d'avoir la cméra en direct sur l'ordinateur<br/>
Essayer en laboratoire ( le code le plus récent n'a pas pû être testé )<br/>
