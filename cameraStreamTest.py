import pymba
import numpy as np
import cv2
import time



def streamFrame_callback(frame):
    img = frame.buffer_data_numpy()
    cv2.imshow(winname = 'preview',mat = img)
    cv2.waitKey(10)

    
with pymba.Vimba() as vimba: #insures that camera is appropriately shut down
    vimba.startup()
    system = vimba.system()
    system.run_feature_command("GeVDiscoveryAllOnce")
    time.sleep(0.5)
    camera_ids = vimba.camera_ids()
    vmb_cam = vimba.camera(camera_ids[0])
    vmb_cam.open()
    vmb_cam.PixelFormat = 'Mono8'
    vmb_cam.arm(mode = pymba.camera.CONTINUOUS,callback = streamFrame_callback, \
                frame_buffer_size=10)
    #vmb_cam.start_capture()

    vmb_cam.start_frame_acquisition()
    time.sleep(30) #acquire 30s
    vmb_cam.stop_frame_acquisition()
    time.sleep(0.5)
    vmb_cam.flush_capture_queue()
    vmb_cam.revoke_all_frames()
    
    



