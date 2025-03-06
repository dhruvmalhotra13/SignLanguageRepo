# Sign Language Detection using Autoencoders and Digital Image Processing

## Overview
This project focuses on detecting sign language gestures using an unsupervised learning approach. We leverage autoencoders for feature extraction and clustering, followed by manual labeling to improve detection accuracy. OpenCV is used for digital image processing, enhancing gesture recognition.

## Features
- **Unsupervised Learning**: Uses autoencoders to extract meaningful features from unlabelled images.
- **Clustering**: Groups similar sign language gestures for efficient labeling.
- **Manual Annotation**: Provides a mechanism for refining clusters with human input.
- **Digital Image Processing**: Utilizes OpenCV for preprocessing images to enhance recognition.

## Tech Stack
- **Python**
- **TensorFlow/Keras** (for autoencoder implementation)
- **OpenCV** (for image processing)
- **Scikit-learn** (for clustering and evaluation)
- **NumPy & Pandas** (for data handling)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/sign-language-detection.git
   cd sign-language-detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Preprocess Images**
   ```bash
   python preprocess.py --input path/to/dataset --output path/to/preprocessed
   ```
2. **Train Autoencoder**
   ```bash
   python train_autoencoder.py --data path/to/preprocessed --epochs 50
   ```
3. **Cluster Features**
   ```bash
   python cluster.py --encoded_data path/to/encoded
   ```
4. **Manually Label Clusters**
   - Open the generated cluster visualization and label groups accordingly.

## Dataset
- The dataset consists of unlabelled sign language images.
- Images are preprocessed using OpenCV techniques such as grayscale conversion, thresholding, and contour detection.

## Model Architecture
- The autoencoder consists of convolutional layers to learn latent representations of gestures.
- The encoded representations are clustered using K-Means or DBSCAN.

## Future Improvements
- Implement real-time detection using a webcam feed.
- Improve clustering accuracy with contrastive learning.
- Develop a UI for easier annotation and model interaction.

## Acknowledgments
- OpenCV for image processing techniques.
- TensorFlow/Keras for deep learning capabilities.
- The sign language community for inspiring this project.

