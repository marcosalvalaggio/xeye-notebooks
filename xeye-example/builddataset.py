import xeye

# list of directory (paths for the .npz files)
path = ['../batch_1.npz','../batch_2.npz', '../batch_3.npz']
# list of labels associated with the images inside the .npz files
label = [0,1,2]
# initializes the class
data = xeye.BuildDataset(path=path, label=label, size = None, color=True, split=True, perc=0.2)
data.build()