# Pose_Estimation_AR
A simple camera pose estimation and AR object visualization project using OpenCV

# CameraPoseAR

OpenCV를 사용한 간단한 카메라 자세 추정 및 AR 객체 시각화 프로젝트입니다.

## 설명

 이 프로젝트는 체스보드 영상으로부터 카메라를 캘리브레이션하고, 그 결과를 이용해 카메라의 자세를 추정합니다.
이후 추정된 자세를 바탕으로 실시간으로 3D 도형(숫자 7 모양)을 영상 위에 오버레이합니다.

- 카메라 캘리브레이션 수행 (체스보드 영상 기반)

- 자세 추정 기반 AR 시각화

- 숫자 '7' 형태의 3D 도형을 실시간으로 그려줌

## 기능

- 영상 파일에서 프레임 읽기

- 체스보드 코너 검출

- `cv.solvePnP`를 이용한 카메라 자세 추정

- `cv.projectPoints`를 이용한 3D → 2D 투영

- 3D 도형(숫자 '7') 오버레이

- 카메라의 XYZ 좌표를 화면에 표시

## 파일 구성

- `camera_calibration.py`
     체스보드 영상을 기반으로 카메라 내부 파라미터 추정

- `pose_estimation_ar.py`
     캘리브레이션 결과를 이용해 AR 도형 시각화

- `calibration_data.npz`
     저장된 캘리브레이션 결과 (카메라 행렬 K, 왜곡 계수 dist)

- `chessboard.avi`
     체스보드 영상 파일

## 실행 방법

1. `camera_calibration.py`를 실행해 캘리브레이션 파일을 생성합니다:

2. `pose_estimation_ar.py`를 실행해 AR 결과를 확인합니다:


