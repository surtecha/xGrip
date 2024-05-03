import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

    while cap.isOpened():
        ret, frame = cap.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = holistic.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Draw bounding box around the detected hand
        if results.right_hand_landmarks:
            # Extract the bounding box coordinates
            x_min, y_min, x_max, y_max = 9999, 9999, 0, 0
            for landmark in results.right_hand_landmarks.landmark:
                x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])
                if x < x_min:
                    x_min = x
                if x > x_max:
                    x_max = x
                if y < y_min:
                    y_min = y
                if y > y_max:
                    y_max = y
            # Draw the bounding box
            cv2.rectangle(image, (x_min - 50, y_min - 50), (x_max + 50, y_max + 50), (0, 0, 0), 4)

        # Draw hand landmarks and connections
        mp_draw.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                               mp_draw.DrawingSpec(color=(0, 0, 200), thickness=4, circle_radius=4),
                               mp_draw.DrawingSpec(color=(0, 0, 0), thickness=6, circle_radius=4)
                              )

        cv2.imshow('Webcam Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
