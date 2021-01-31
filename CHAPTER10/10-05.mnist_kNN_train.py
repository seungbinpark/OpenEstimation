import numpy as np, cv2
import pickle, gzip, os
from urllib.request import urlretrieve
import matplotlib.pyplot as plt

def load_mnist(filename):
    if not os.path.exists(filename):
        print("Downloading")
        link = "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"

        urlretrieve(link, filename)
    with gzip.open(filename, 'rb') as f:
        return pickle.load(f, encoding='latin1')

def graph_image(data, lable, title, nsample):
    plt.figure(num=title, figsize=(10,10))
    rand_idx = np.random.choice(range(data.shape[0]), nsample)
    for i, id in enumerate(rand_idx):
        img = data[id].reshape(28, 28)
        plt.subplot(6, 4, i+1), plt.axis('off'), plt.imshow(img, cmap='gray')
        plt.title("%s: %d" %(title, lable[id]))
        plt.tight_layout()

train_set, valid_set, test_set = load_mnist("mnist.pkl.gz")

print("train_set=", train_set[0].shape)
print("valid_set=", valid_set[0].shape)
print("test_set=", test_set[0].shape)

print("training...")
knn = cv2.ml.KNearest_create()
knn.train(train_set, cv2.ml.ROW_SAMPLE, valid_set)

nsample = 100
print("%d 개 predicting..." % nsample)
_, resp, _, _ = knn.findNearest(test_set[:nsample], k=5)
accur = sum(resp.flatten() == test_set[:nsample])

print("정확도=", accur / nsample * 100, '%')
graph_image(train_set, valid_set, 'label', 24)
graph_image(test_set[:nsample], resp, 'predict', 24)
plt.show()