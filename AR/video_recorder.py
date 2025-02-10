import cv2

def capture_video(output_path, frame_width=640, frame_height=480, fps=30):
    # Open the camera (usually 0 is the default webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Set the frame width and height
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    # Define the codec and create VideoWriter object to save the video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for .avi files
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    print("Press 'q' to stop recording...")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame.")
            break

        # Write the frame to the video file
        out.write(frame)

        # Display the frame in a window
        cv2.imshow('Recording Video', frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything when done
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved to {output_path}")

if __name__ == "__main__":
    output_path = 'captured_video.mp4'  # Change this to your desired output path
    capture_video(output_path)
