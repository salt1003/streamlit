### import ###
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from array import array
import os
from PIL import Image
import sys
import time
import json
import streamlit as st

# タグ取得の関数
with open('./secret.json') as f:
    secret = json.load(f)

KEY = secret['KEY']
ENDPOINT = secret['ENDPOINT']

computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# 物体の検出関数
def getTags(filepath):
    localImage = open(filepath, "rb")

    tagsResult = computervision_client.tag_image_in_stream(local_image)
    tags = tagsResult.tags
    tagsName = []
    for tag in tags:
        tagsName.append(tag.name)

    return tagsName

#  v-アプリの処理
def detectObjects(filepath):
    localImage = open(filepath, "rb")

    detectObjectsResults = computervision_client.detect_objects_in_stream(local_image)
    objects = detectObjectsResults.objects
    return objects

#
st.title('物体検出アプリ')

uploadedFile = st.file_uploader('Choose an image...', type=['jpg','png'])

if uploadedFile is not None:
    img = Image.open(uploadedFile)
    # imgPath = f'img/{uploadedFile.name}'
    # img.save(imgPath)
    # objects = detectObjects(imgPath)
    st.image(img)
    st.markdown('**認識されたコンテンツタグ**')