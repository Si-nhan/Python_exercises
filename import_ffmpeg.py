import ffmpeg
import numpy as np
import cv2

source = "rtsp://admin:sinhan123@192.168.1.36:554/onvif1"
size: int = 720*1280*3 # Kích thước frame của stream

capture = (
ffmpeg
.input(source, rtsp_transport="udp")
.output(filename="pipe:", format="rawvideo", pix_fmt="bgr24")
.run_async(pipe_stdout=True, quiet=False)
)

while True:
   in_bytes = capture.stdout.read(size)
   if len(in_bytes) == 0:
      print("Lose connection")
      exit()
   frame =  (
                np.frombuffer(in_bytes, np.uint8).
                reshape(720, 1280, 3)
        )
   cv2.imshow('camera', frame)
   if cv2.waitKey(1) == ord('q'):
        break
   
# fflags="nobuffer", flags="low_delay"