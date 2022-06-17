class ConvNet(nn.Module):
  def __init__(self):
    super(ConvNet, self).__init__()
    #Input shape: (batch_size,3,256,256)
        
    # Convolutional 1 layer: 3x3 kernel, stride=1, padding=0, 2 output channels / feature maps
    self.conv1 = nn.Conv2d(in_channels=3, out_channels=2, kernel_size=3, stride=1, padding=0)
    # Conv1 layer output size = (W-F+2P)/S+1 = ((256-3)/1)+1 = 254
    # Conv1 layer output shape for one image: [2,254,254]
    
    # Maxpool layer: kernel_size=2, stride=2
    self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
    # Pool output shape for one image: ((254-2)/2)+1 = 127 [2,127,127]
    
    # Convolutional 2 layer: 3x3 kernel, stride=1, padding=0, 20 output channels / feature maps
    self.conv2 = nn.Conv2d(in_channels=2,out_channels=4,kernel_size=3, stride=1, padding=0)
    # Conv2 layer output size = (W-F+2P)/S+1 = ((127-3)/1)+1 = 125
    # Conv2 layer output shape for one image: [4,125,125]
    
    # Maxpool layer: kernel_size=2, stride=2
    self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
    # Pool output shape for one image: ((125-2)/2)+1 = 62 (rounded down)  [4,62,62]
    
    # Input size: 4 * 62 * 62 = 15376  from pool2 pooling layer
    # 2 output channels (for the 2 classes)
    self.fc1 = nn.Linear(4*62*62, 2)
  
  def forward(self, x):
    # Two convolutional layers followed by relu and then pooling
    x = F.relu(self.conv1(x))
    x = self.pool1(x)
    x = F.relu(self.conv2(x))
    x = self.pool2(x)

    # Flatten into a vector to feed into linear layer
    x = x.view(x.size(0), -1)
    
    # Linear layer
    x = self.fc1(x)
    return x
    net = ConvNet()

  #display a summary of the layers of the model and output shape after each layer
  summary(net, (images.shape[1:]), batch_size=batch_size, device='cpu')

  criterion = nn.CrossEntropyLoss()
  optimizer = optim.SGD(net.parameters(), lr=0.01)

  def train_model(model, criterion, optimizer, train_loader, n_epochs, device):
    loss_over_time = [] # to track the loss as the network trains 
    model = model.to(device) # Send model to GPU if available
    model.train() # Set the model to training mode

  for epoch in range(n_epochs):  # loop over the dataset multiple times
      
      running_loss = 0.0
      
      for i, data in enumerate(train_loader):
          
          # Get the input images and labels, and send to GPU if available
          inputs, labels = data[0].to(device), data[1].to(device)

          # Zero the weight gradients
          optimizer.zero_grad()

          # Forward pass to get outputs
          outputs = model(inputs)

          # Calculate the loss
          loss = criterion(outputs, labels)

          # Backpropagation to get the gradients with respect to each weight
          loss.backward()

          # Update the weights
          optimizer.step()

          # Convert loss into a scalar and add it to running_loss
          running_loss += loss.item()
          
          if i % 1000 == 999:    # print every 1000 batches
              avg_loss = running_loss/1000
              # record and print the avg loss over the 1000 batches
              loss_over_time.append(avg_loss)
              print('Epoch: {}, Batch: {}, Avg. Loss: {:.4f}'.format(epoch + 1, i+1, avg_loss))
              running_loss = 0.0

  return loss_over_time

  def test_model(model,test_loader,device):
    # Turn autograd off
    with torch.no_grad():

        # Set the model to evaluation mode
        model = model.to(device)
        model.eval()

        # Set up lists to store true and predicted values
        y_true = []
        test_preds = []
        test_probs = []

        # Calculate the predictions on the test set and add to list
        for data in test_loader:
            inputs, labels = data[0].to(device), data[1].to(device)
            # Feed inputs through model to get raw scores
            logits = model.forward(inputs)
            # Convert raw scores to probabilities 
            probs = F.softmax(logits,dim=1)
            # Get discrete predictions using argmax
            preds = np.argmax(probs.cpu().numpy(),axis=1)
            # Add predictions and actuals to lists
            test_preds.extend(preds)
            test_probs.extend(probs)
            y_true.extend(labels.cpu().numpy())

        # Calculate the accuracy
        test_preds = np.array(test_preds)
        test_probs = np.array(test_probs)
        y_true = np.array(y_true)
        test_acc = np.sum(test_preds == y_true)/y_true.shape[0]
        
        # Recall for each class
        recall_vals = []
        for i in range(10):
            class_idx = np.argwhere(y_true==i)
            total = len(class_idx)
            correct = np.sum(test_preds[class_idx]==i)
            recall = correct / total
            recall_vals.append(recall)
    
    return test_acc, recall_vals,test_preds,test_probs

    if __name__ == "__main__":
  
    additional_test_path = Path('test-jpg-additional/test-jpg-additional')

    test_path = Path('planet/planet/test-jpg')

    submission_df = pd.read_csv(path/'sample_submission.csv')

    testing_path = (submission_df['image_name'] + '.jpg').apply(lambda x: test_path/x if x.startswith('test') else additional_test_path/x)
    train_model()  # pylint: disable=no-value-for-parameter
    test_model()
