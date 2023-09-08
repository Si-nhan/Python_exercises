import cv2
# import os

# os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport; udp"

rtsp = 'rtsp://admin:sinhan123@192.168.1.41:554/onvif1'
rtsp += '/;rtsp_transport=udp'
video_codec = 'h264'

# Khởi tạo đối tượng VideoCapture để đọc video stream từ camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*video_codec))

# Kiểm tra xem camera có sẵn sàng để đọc hay không
if not cap.isOpened():
    print("Không thể kết nối đến camera")
    exit()

# Đọc và hiển thị từng khung hình trong video stream
while True:
    # Đọc từng khung hình từ video stream
    ret, frame = cap.read()

    # Kiểm tra xem khung hình có được đọc thành công hay không
    if not ret:
        print("Không thể đọc khung hình")
        break

    # Hiển thị khung hình
    cv2.imshow("Camera", frame)

    # Nhấn phím 'q' để thoát
    if cv2.waitKey(1) == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
