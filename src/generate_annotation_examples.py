import argparse
from pathlib import Path
import cv2
from ultralytics import YOLO

TARGET_CLASSES = [0, 1, 2, 3, 5, 7]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("video")
    parser.add_argument("--conf", type=float, default=0.40)
    parser.add_argument("--output", default="annotation_examples")
    args = parser.parse_args()

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    model = YOLO("yolo11n.pt")
    cap = cv2.VideoCapture(args.video)

    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    target = int(total * 0.55)
    cap.set(cv2.CAP_PROP_POS_FRAMES, target)
    ok, frame = cap.read()
    cap.release()

    if not ok:
        raise RuntimeError("Could not read representative frame.")

    result = model.predict(
        frame,
        conf=args.conf,
        classes=TARGET_CLASSES,
        verbose=False
    )[0]

    output = frame.copy()

    if result.boxes is not None:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
            class_id = int(box.cls[0])
            conf = float(box.conf[0])
            name = model.names[class_id]

            cv2.rectangle(output, (x1, y1), (x2, y2), (80, 220, 120), 2)
            cv2.putText(
                output,
                f"{name} {conf:.2f}",
                (x1, max(20, y1 - 6)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (80, 220, 120),
                2,
                cv2.LINE_AA
            )

    path = out / "05_bounding-box-annotation.jpg"
    cv2.imwrite(str(path), output)
    print(f"Saved: {path}")

if __name__ == "__main__":
    main()
