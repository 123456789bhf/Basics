import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np

# Define Transformer Encoder Model
class TransformerEncoderModel(nn.Module):
    def __init__(self, input_dim, model_dim, num_heads, num_layers, ff_dim, dropout=0.1):
        super(TransformerEncoderModel, self).__init__()
        self.input_linear = nn.Linear(input_dim, model_dim)
        encoder_layer = nn.TransformerEncoderLayer(d_model=model_dim, nhead=num_heads, dim_feedforward=ff_dim, dropout=dropout)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.output_linear = nn.Linear(model_dim, input_dim)

    def forward(self, x):
        x = self.input_linear(x)
        x = self.transformer_encoder(x)
        x = self.output_linear(x)
        return x

# Create synthetic dataset
def create_synthetic_data(num_samples, sequence_length, input_dim):
    X = np.random.rand(num_samples, sequence_length, input_dim).astype(np.float32)
    y = np.random.rand(num_samples, sequence_length, input_dim).astype(np.float32)
    return torch.tensor(X), torch.tensor(y)

# Hyperparameters
input_dim = 10
model_dim = 32
num_heads = 4
num_layers = 2
ff_dim = 64
sequence_length = 20
num_samples = 1000
batch_size = 32
num_epochs = 5
learning_rate = 0.001

# Prepare data
X, y = create_synthetic_data(num_samples, sequence_length, input_dim)
dataset = TensorDataset(X, y)
data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Model, loss, optimizer
model = TransformerEncoderModel(input_dim, model_dim, num_heads, num_layers, ff_dim)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
model.train()
for epoch in range(num_epochs):
    epoch_loss = 0
    for batch in data_loader:
        inputs, targets = batch
        inputs, targets = inputs.to(device), targets.to(device)

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

    avg_loss = epoch_loss / len(data_loader)
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.4f}")

print("Training complete.")