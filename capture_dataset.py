import cv2
import os

# Ask for student name/ID
student_name = input("Enter Student Name or ID: ")
save_path = f"dataset/{student_name}"
os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not access the webcam")
    exit()

count = 0

while count < 5:   # capture only 5 images
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    cv2.imshow("Capturing Images - Press Q to Quit", frame)

    # Save one image per loop
    file_name = os.path.join(save_path, f"img{count+1}.jpg")
    cv2.imwrite(file_name, frame)
    print(f"✅ Saved: {file_name}")

    count += 1

    # Wait a little so the frame refreshes
    key = cv2.waitKey(1000)  # 1 second delay
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"🎉 Done! {count} images saved in {save_path}")
