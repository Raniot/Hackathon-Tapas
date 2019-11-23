import numpy as np
import argparse
import time
from cv2 import cv2
import os
from AudioPlayer import AudioPlayer
from threading import Timer

class Yolo:
    def __init__(self):
        self.Labels = open("./yolo-coco/coco.names").read().strip().split("\n")
        self.Colors = np.random.randint(
            0, 255, size=(len(self.Labels), 3), dtype="uint8")
        self.Model = cv2.dnn.readNetFromDarknet(
            "./yolo-coco/yolov3.cfg", "./yolo-coco/yolov3.weights")
        self.LayerNames = [self.Model.getLayerNames()[i[0] - 1] for i in self.Model.getUnconnectedOutLayers()]
        self.SafePassing = True

    def _SetSafePassingTrue(self):
        self.SafePassing = True

    def ProcessImage(self, image):
        imageHeight, imageWidth = image.shape[:2]
        blob = cv2.dnn.blobFromImage(
            image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        self.Model.setInput(blob)

        layerOutputs = self.Model.forward(self.LayerNames)
        return self.PlaceBoundingBoxes(image, imageHeight, imageWidth, layerOutputs)

    def PlaceBoundingBoxes(self, image, imageHeight, imageWidth, layerOutputs):
        boxes = []
        confidences = []
        classIDs = []
        objectClose = False

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]

                if confidence > 0.5:
                    box = detection[0:4] * \
                        np.array([imageWidth, imageHeight,
                                  imageWidth, imageHeight])
                    (centerX, centerY, width, height) = box.astype("int")

                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)
        
        if len(idxs) > 0:
            for i in idxs.flatten():
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])

                color = [int(c) for c in self.Colors[classIDs[i]]]
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                
                if self.Labels[classIDs[i]] == 'Car' or self.Labels[classIDs[i]] == 'Bicycle':
                    self.SafePassing = False
                    Timer(7, self._SetSafePassingTrue)
                
                text = "{}: {:.4f}".format(self.Labels[classIDs[i]], confidences[i])
                cv2.putText(image, text, (x, y - 5),cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                widthProcent = w/imageWidth
                heightProcent = h/imageHeight

                squareSize = widthProcent * heightProcent
                mid_x = (x + w/2)/imageWidth

                if squareSize >= 0.25 and mid_x > 0.15 and mid_x < 0.85:
                    objectClose = True

        return image, objectClose, self.SafePassing
