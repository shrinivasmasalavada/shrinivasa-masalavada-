for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]

        if label in ["elephant", "cow", "dog"]:
            print("⚠️ Animal Detected:", label)