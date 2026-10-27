# 电池目标检测 / Battery Detection (YOLO)

基于 Ultralytics YOLO26n 的电池目标检测项目，可识别锂电池、铅酸蓄电池及其缺陷（鼓包、漏液）与干扰物（瓶子）。

An object detection project based on Ultralytics YOLO26n, detecting lithium batteries, lead-acid batteries, their defects (swelling, leakage), and distractors (bottles).

---

## 功能特性 / Features

- 🔋 检测 6 个类别 / Detects 6 classes:
  | 类别 (拼音) | 中文 | English |
  |---|---|---|
  | `lidianchi` | 锂电池 | Lithium battery |
  | `lidianchi-gubao` | 锂电池鼓包 | Lithium battery (swollen) |
  | `pingzi` | 瓶子 | Bottle |
  | `qiansuanxudianchi` | 铅酸蓄电池 | Lead-acid battery |
  | `qiansuanxudianchi-gubao` | 铅酸蓄电池鼓包 | Lead-acid battery (swollen) |
  | `qiansuanxudianchi-louye` | 铅酸蓄电池漏液 | Lead-acid battery (leaking) |
- 包含训练数据集（Roboflow 导出，YOLO 格式）/ Includes training dataset (Roboflow export, YOLO format)
- 包含多轮训练输出（权重、曲线图、混淆矩阵）/ Includes multiple training runs (weights, curves, confusion matrices)

## 项目结构 / Project Structure

```
battery-cv/
├── text_yolo.py        # 训练 + 推理示例脚本 / Training + inference demo script
├── yolo26n.pt          # 预训练权重 / Pretrained weights
├── bus.jpg             # 示例输入图片 / Sample input image
├── result.jpg          # 推理结果示例 / Sample inference result
├── dataset/            # 数据集 / Dataset
│   ├── data.yaml       # 数据集配置 / Dataset config
│   ├── images/         # 训练集与验证集图片 / Train & val images
│   └── labels/         # YOLO 格式标注 / YOLO-format labels
└── runs/detect/        # 训练与预测输出 / Training & prediction outputs
    ├── train-2 ~ 6/    # 历次训练（含 weights/best.pt）/ Training runs
    └── predict*/       # 推理输出 / Prediction outputs
```

## 环境依赖 / Requirements

- Python 3.8+
- [Ultralytics](https://github.com/ultralytics/ultralytics)

```bash
pip install ultralytics
```

## 使用方法 / Usage

### 训练 / Training

```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
model.train(data="dataset/data.yaml", epochs=100, imgsz=640, batch=2, device="cpu")
```

> 本项目在 CPU 上训练（batch=2, imgsz=640, 100 epochs）。如有 GPU，可将 `device` 改为 `"0"` 以加速。
>
> This project was trained on CPU (batch=2, imgsz=640, 100 epochs). If you have a GPU, set `device="0"` for faster training.

### 推理 / Inference

```python
results = model("https://ultralytics.com/images/bus.jpg")
print(results[0].boxes)
results[0].save("result.jpg")
results[0].show()
```

也可以直接使用训练好的最佳权重 / You can also use the trained best weights directly:

```python
model = YOLO("runs/detect/train-6/weights/best.pt")
results = model("your_image.jpg")
```

## 数据集 / Dataset

- 来源 / Source: [Roboflow](https://app.roboflow.com/shangqis-workspace-cljs3/-jsgc2/1)
- 训练集 / Train: 60 张图片 / images
- 验证集 / Val: 14 张图片 / images
- 格式 / Format: YOLO（txt 标注文件）/ (txt label files)

## 训练结果 / Results

各轮训练的损失曲线、F1/PR/P/R 曲线与混淆矩阵见 / Loss curves, F1/PR/P/R curves and confusion matrices for each run are in:
`runs/detect/train-*/`

## 许可证 / License

本项目仅供学习与研究使用。数据集许可证请参考 Roboflow 页面。

For learning and research purposes only. Please refer to the Roboflow page for the dataset license.
