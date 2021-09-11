import cv2 as cv
import numpy as np


class PersonnelDetection:
    classes = ['nopersonnel', 'personnel']

    def detection(self):
        net = cv.dnn.readNetFromDarknet("conf/yolov3_custom.cfg",
                                        r"conf/yolov3_custom_3000.weights")
        img = cv.imread('image.jpg')
        hight, width, _ = img.shape
        blob = cv.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)

        net.setInput(blob)

        output_layers_name = net.getUnconnectedOutLayersNames()
        layerOutputs = net.forward(output_layers_name)

        boxes = []
        confidences = []
        class_ids = []

        for output in layerOutputs:
            for detection in output:
                score = detection[5:]
                class_id = np.argmax(score)
                print('class_id', class_id)
                confidence = score[class_id]
                print('confidence', confidence)
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * hight)
                    w = int(detection[2] * width)
                    h = int(detection[3] * hight)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append((float(confidence)))
                    class_ids.append(class_id)

        # indexes = cv.dnn.NMSBoxes(boxes, confidences, .5, .4)

        indexes = cv.dnn.NMSBoxes(boxes, confidences, .8, .4)

        if len(indexes) > 0:
            for i in indexes.flatten():
                label = str(self.classes[class_ids[i]])
                return label
        else:
            return 'Unknown'
