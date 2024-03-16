# deeplearning-assignment-8

video link :  https://drive.google.com/drive/folders/10LmwB516RvbbFlmAW3iq3GF_zpIil7sg?usp=share_link

DESCRIPTION:
cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "qN_Sprsqsvg9"
   },
   "source": [
    "Import libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "id": "WJbVE-AVaGpA"
   },
   
   import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import tensorflow as tf\n",
    "from tensorflow.keras.datasets import mnist\n",
    "\n",
    "from tensorflow.keras.optimizers import RMSprop\n",
    "from keras.preprocessing import image\n",
    "from tensorflow.keras.preprocessing.image import ImageDataGenerator\n",
    "from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout, BatchNormalization\n",
    "\n",
    "%matplotlib inline"
    
    cell_type": "markdown",
   "metadata": {
    "id": "nxgdjVg0suGK"
   },
   "source": [
    "Extract data and train and test dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "id": "wRRU6txYaZ1m"
    
    source": [
    "#cifar100 = tf.keras.datasets.cifar100\n",
    "(X_train,Y_train) , (X_test,Y_test) = cifar10.load_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "id": "OrVy37gUa4Jc"
   },
   "outputs": [],
   "source": [
    "classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "vI8qStc7uGvO"
   },
   "source": [
    "Let's look into the dataset images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "Tgzh-Ot_bCh0"
