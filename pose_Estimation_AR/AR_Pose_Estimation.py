import cv2 as cv
import numpy as np

# -----------------------------
# 체스보드 설정
board_pattern = (9, 6)                # 내부 코너 수 (가로 10 × 세로 7)
board_cellsize = 0.025                 # 한 칸의 크기 (25mm = 0.025m)
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# -----------------------------
# 캘리브레이션 데이터 로드
# 예제에서 제공된 K, dist를 사용한 경우
data = np.load("C:/Users/user/OneDrive/바탕 화면/pose_Estimation_AR/calibration_data.npz")
K = data['mtx']
dist = data['dist']

# -----------------------------
# 3D 체스보드 점 좌표 생성
obj_points = board_cellsize * np.array(
    [[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])]
)

# -----------------------------
# AR에 사용할 3D 도형 점 (숫자 7 모양)
digit_3d = board_cellsize * np.array([
    [4, 2, 0],
    [5, 2, 0],
    [4.5, 3, 0],
    [4.5, 4, 0]
])

# -----------------------------
# 비디오 로드
video = cv.VideoCapture("C:/Users/user/OneDrive/바탕 화면/pose_Estimation_AR/chessboard.avi")
if not video.isOpened():
    print("❌ 비디오를 열 수 없습니다.")
    exit()

while True:
    valid, img = video.read()
    if not valid:
        break

    # 체스보드 코너 검출
    complete, img_points = cv.findChessboardCorners(img, board_pattern, criteria)
    if complete:
        # 포즈 추정
        ret, rvec, tvec = cv.solvePnP(obj_points, img_points, K, dist)

        # AR 도형 3D → 2D로 투영
        proj_pts, _ = cv.projectPoints(digit_3d, rvec, tvec, K, dist)
        for pt in proj_pts:
            cv.circle(img, tuple(pt.ravel().astype(int)), 5, (0, 255, 255), -1)

        # 카메라 위치 출력
        R, _ = cv.Rodrigues(rvec)
        cam_pos = (-R.T @ tvec).flatten()
        pos_text = f"Camera XYZ: [{cam_pos[0]:.2f}, {cam_pos[1]:.2f}, {cam_pos[2]:.2f}]"
        cv.putText(img, pos_text, (10, 25), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # 결과 출력
    cv.imshow("AR Pose Estimation", img)
    if cv.waitKey(1) == 27:  # ESC
        break

video.release()
cv.destroyAllWindows()
