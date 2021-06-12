import pymba
import numpy as np
import cv2
import time
import tifffile as tf


with pymba.Vimba() as vimba: #insures that camera is appropriately shut down
    vimba.startup()
    system = vimba.system()
    system.run_feature_command("GeVDiscoveryAllOnce")
    time.sleep(0.5)
    camera_ids = vimba.camera_ids()
    vmb_cam = vimba.camera(camera_ids[0])
    vmb_cam.open()
    vmb_cam.Gain= 10
    vmb_cam.PixelFormat = 'Mono12'
    vmb_cam.arm(mode = pymba.camera.SINGLE_FRAME)
    frame = vmb_cam.acquire_frame()

    img = frame.buffer_data_numpy()
    imgSc = np.uint8(img/4095*255)
    cv2.imshow(winname = 'win',mat = np.uint8(img))
    vmb_cam.disarm()
    vimba.shutdown()    
