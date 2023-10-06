from typing import Any
import torchvision
from torchvision import transforms
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

def data():
    train_data_path = './pic/'
    transform = transforms.Compose([
        transforms.Resize(64),
        transforms.ToTensor(),
        transforms.Normalize(mean = [0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225])
    ])
    train_data = torchvision.datasets.ImageFolder(root = train_data_path, transform = transform)
    return train_data

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

class SimpleNet(nn.Module):

    def __init__(self):
        super.__init__()
        self.l1 = nn.Linear(12288, 84)
        self.l2 = nn.Linear(84, 50)
        self.l3 = nn.Linear(50, 2)

    def forward(self, x: torch.tensor):
        x = x.view(-1, 12288)
        x = F.softmax(self.l3(F.relu(self.l2(F.relu(self.l1)))))
        return x

# opt = optim.Adam(lr = 0.001)

class CNN(nn.Module):
    
    def __init__(self, num_class = 2):
        super.__init__()
        self.feature = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size = 11, stride = 4, padding = 2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size = 3, stride = 2),

            nn.Conv2d(64, 192, kernel_size = 5, padding = 2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size = 3, stride = 2),

            nn.Conv2d(192, 384, kernel_size = 3, padding = 1),
            nn.ReLU(),
            nn.Conv2d(384, 256, kernel_size = 3, padding = 1),
            nn.ReLU(),
            nn.Conv2d(256, 256, kernel_size = 3, padding = 1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size = 3, stride = 2)
        )
        self.avgpool = nn.AdaptiveAvgPool2d((6, 6))
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(),
            nn.Linear(4096, num_class)
        )
    
    def forward(self, x):
        x = self.feature(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

class Noise():
    """
    Adds gaussian noise to a tensor.
        transforms.Compose([
            transforms.ToTensor(),
            Noise(0.1, 0.05)),
            ])
    """
    def __init__(self, mean, stddev) -> None:
        self.mean = mean
        self.stddev = stddev
    
    def __call__(self, tensor: torch.tensor) -> Any:
        noise = torch.zeros_like(tensor).normal_(self.mean, self.stddev)
        return tensor.add_(noise)

    def __repr__(self):
        rep = f"{self.__class__.__name__ }(mean={self.mean}, stddev={self.stddev})"
        return rep
