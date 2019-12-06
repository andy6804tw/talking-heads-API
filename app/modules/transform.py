import cv2
import time
import pickle as pkl
import imageio
import numpy as np
import matplotlib.pyplot as plt

import torchvision.transforms.functional as TF
from face_alignment import FaceAlignment, LandmarksType

from app.modules.talkingHeads.utils import load_model, generate_image, plot_landmarks, generate_lm, image_to_video, generate_moving_video, generate_moving_image, get_e_vector
import app.modules.talkingHeads.network as network

from flask import jsonify

# %load_ext autoreload
# %autoreload 2

def getTransform(videoName,modelIdx):
    modelList=['sw','han','tsai']
    G = network.Generator()
    G = load_model(G, "app/modules/talkingHeads/resource/"+modelList[modelIdx], modelList[modelIdx])
    G = G.to("cuda:0")
    fa = FaceAlignment(LandmarksType._2D, device='cuda:0')
    e_vector = get_e_vector("app/modules/talkingHeads/resource/"+modelList[modelIdx]+"/"+modelList[modelIdx]+".npy")
    timestamp=str(int(time.time()))
    print(timestamp)
#     generate_moving_video(G, "app/static/"+videoName, "app/modules/talkingHeads/resource/"+modelList[modelIdx]+"/"+modelList[modelIdx]+".npy", "app/static/result-"+timestamp+".mp4", "cuda:0")
    generate_moving_video(G, "app/static/"+videoName, e_vector, "app/static/result-"+timestamp+".mp4", "cuda:0", fa)
    return jsonify({"code":200,"message": "轉換成功",'token':timestamp})

def getResult():
    return 'ddon'

