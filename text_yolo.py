from ultralytics import YOLO
model = YOLO("yolo26n.pt")
model.train(data="D:/Desktop/battery-cv/dataset/data.yaml", epochs=100, imgsz=640, batch=2, device="cpu")

results = model("https://ultralytics.com/images/bus.jpg")

print(results[0].boxes)

results[0].save("result.jpg")

results[0].show()