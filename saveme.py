import torch

m = torch.load("F:\cccc/flutestudy\yolo\yolov5/best.pt")
torch.save(m["model"].state_dict(), "F:\cccc/flutestudy\yolo\yolov5/best1.pt")