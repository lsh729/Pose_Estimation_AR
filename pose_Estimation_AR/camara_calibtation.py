# camera_calibration.py
import cv2 as cv
import numpy as np

def calib_from_video(video_path, board_pattern=(10, 7), board_cellsize=0.025):
    video = cv.VideoCapture("C:/Users/user/OneDrive/바탕 화면/pose_Estimation_AR/chessboard.avi")
    img_points, obj_points = [], []

    objp = np.array([[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])], dtype=np.float32)
    objp *= board_cellsize

    while True:
        valid, img = video.read()
        if not valid:
            break
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        found, corners = cv.findChessboardCorners(gray, board_pattern)
        if found:
            img_points.append(corners)
            obj_points.append(objp)

    assert len(img_points) > 0, "체스보드를 찾지 못했습니다!"
    ret, K, dist, _, _ = cv.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)
    np.savez("calibration_data.npz", mtx=K, dist=dist)
    print("[INFO] K와 dist 저장 완료")
    return K, dist

if __name__ == "__main__":
    calib_from_video("C:/Users/user/OneDrive/바탕 화면/pose_Estimation_AR/chessboard.avi")
