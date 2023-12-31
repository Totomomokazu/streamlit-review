from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from array import array
import os
from PIL import Image
import sys
import time


computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# 物体のタグ（名前）を取得する関数
def get_tags(filepath):
    local_image = open(filepath, "rb")

    tags_result_local = computervision_client.tag_image_in_stream(local_image)
    tags=tags_result_local.tags
    tag_name=[]
    for tag in tags:
        tag_name.append(tag.name)
    return tag_name

# 物体を検知する関数
def detect_objects(filepath):
    local_image_objects = open(filepath, "rb")
    
    detect_objects_results_local = computervision_client.detect_objects_in_stream(local_image_objects)
    objects=detect_objects_results_local.objects
    return objects


import streamlit as st

# PILというライブラリから二つのモジュールをインポートしている
from PIL import ImageDraw
# ImageDrawは画像上に描画するための機能
from PIL import ImageFont
# 画像にテキストを描く際に使用するフォントの管理をするためのモジュール



st.title("物体検出アプリ")

uploaded_file=st.file_uploader("Choose an image",type=["jpg","png"])
# ファイルアップロード場所の作成し、アップロードされた画像データを変数に保存

if uploaded_file is not None:
    img=Image.open(uploaded_file)
    # 変数に保存された画像を開くメソッドを利用
    img_path= f"img/{uploaded_file.name}"
    # ファイル名をuploaded_file.nameで取得。streamlitは保存したpathを指定できないので、ファイル名を取得し、指定したフォルダへ指定したファイル名で保存する
    img.save(img_path)
    # 指定してたpathに画像を保存する
    objects = detect_objects(img_path)


    # 描画する画像をImageDrawのDrawメソッドに入れている
    draw = ImageDraw.Draw(img)


    for object in objects:
        x=object.rectangle.x
        y=object.rectangle.y
        w=object.rectangle.w
        h=object.rectangle.h
        # 座標情報の取得
        caption = object.object_property
        # objectの名前情報を取得

        font = ImageFont.truetype(font='./Helvetica 400.ttf', size=50)

        text_w,text_h=draw.textsize(caption,font=font)
        draw.rectangle([(x,y),(x+w,y+h)], fill=None, outline="green",width=5)
        draw.rectangle([(x,y),(x+text_w,y+text_h)], fill="green")
        draw.text([x,y],caption,fill="white",font=font)




    st.image(img)   
    tag_name=get_tags(img_path)
    tags_name=",".join(tag_name)

    st.markdown("**認識されたコンテンツタグ**")
    st.markdown(f">{tag_name}")
    


