import glob
import os
import pickle

import librosa
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential

print("TensorFlow version:", tf.__version__)
print("Built with CUDA:", tf.test.is_built_with_cuda())
print("GPU available:", tf.config.list_physical_devices("GPU"))

# Thiết lập các tham số
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'model')
os.makedirs(MODEL_DIR, exist_ok=True)

# Tham số trích xuất đặc trưng
SAMPLE_RATE = 44100  # Hz
N_MFCC = 40  # Số lượng đặc trưng MFCC
MAX_LENGTH = 200  # Độ dài tối đa của mảng đặc trưng

# Tham số huấn luyện
BATCH_SIZE = 32
EPOCHS = 100
LEARNING_RATE = 0.001

def extract_features(file_path):
    """Trích xuất đặc trưng MFCC từ file âm thanh"""
    try:
        # Nạp file âm thanh
        y, sr = librosa.load(file_path, sr=SAMPLE_RATE)
        
        # Xóa khoảng lặng đầu và cuối
        y, _ = librosa.effects.trim(y, top_db=30)
        
        # Trích xuất đặc trưng MFCC
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC)
        
        # Chuyển đổi định dạng (f, t) -> (t, f)
        mfcc = mfcc.T
        
        # Cắt hoặc đệm để đảm bảo kích thước đồng nhất
        if mfcc.shape[0] > MAX_LENGTH:
            mfcc = mfcc[:MAX_LENGTH, :]
        else:
            pad_width = MAX_LENGTH - mfcc.shape[0]
            mfcc = np.pad(mfcc, ((0, pad_width), (0, 0)), mode='constant')
        
        return mfcc
    except Exception as e:
        print(f"Lỗi trích xuất đặc trưng từ {file_path}: {e}")
        return None

def load_data():
    """Tải và chuẩn bị dữ liệu"""
    X = []
    y = []
    
    # Tìm tất cả các thư mục người dùng
    user_dirs = [d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d))]
    
    for user_dir in user_dirs:
        user_path = os.path.join(DATA_DIR, user_dir)
        audio_files = glob.glob(os.path.join(user_path, "*.wav"))
        
        for audio_file in audio_files:
            features = extract_features(audio_file)
            if features is not None:
                X.append(features)
                y.append(user_dir)  # Sử dụng tên thư mục làm nhãn người dùng
    
    # Chuyển đổi danh sách thành mảng numpy
    X = np.array(X)
    y = np.array(y)
    
    # Mã hóa nhãn
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    
    # Lưu label_encoder để sử dụng khi dự đoán
    with open(os.path.join(MODEL_DIR, 'label_encoder.pkl'), 'wb') as f:
        pickle.dump(label_encoder, f)
    
    # Chia dữ liệu thành tập train và validation
    X_train, X_val, y_train, y_val = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )
    
    return X_train, X_val, y_train, y_val, label_encoder.classes_

def create_model(num_classes):
    """Tạo mô hình LSTM"""
    model = Sequential([
        # Input shape: (timesteps, features)
        LSTM(128, input_shape=(MAX_LENGTH, N_MFCC), return_sequences=True),
        Dropout(0.3),
        LSTM(64),
        Dropout(0.3),
        Dense(32, activation='relu'),
        Dropout(0.3),
        Dense(num_classes, activation='softmax')
    ])
    
    # Biên dịch mô hình
    optimizer = tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE)
    model.compile(
        optimizer=optimizer,
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

def train_model():
    """Huấn luyện mô hình"""
    # Tải dữ liệu
    X_train, X_val, y_train, y_val, class_names = load_data()
    
    print(f"Dữ liệu huấn luyện: {X_train.shape}")
    print(f"Số lượng lớp: {len(class_names)}")
    print(f"Các lớp: {class_names}")
    
    # Tạo mô hình
    model = create_model(len(class_names))
    model.summary()
    
    # Thiết lập callback
    checkpoint = ModelCheckpoint(
        os.path.join(MODEL_DIR, 'speaker_model.h5'),
        monitor='val_accuracy',
        save_best_only=True,
        verbose=1
    )
    
    early_stopping = EarlyStopping(
        monitor='val_accuracy',
        patience=10,
        restore_best_weights=True,
        verbose=1
    )
    
    # Huấn luyện mô hình
    history = model.fit(
        X_train, y_train,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        validation_data=(X_val, y_val),
        callbacks=[checkpoint, early_stopping]
    )
    
    # Lưu mô hình
    model_filepath = os.path.join(MODEL_DIR, 'speaker_model.h5')
    model.save(model_filepath)
    print(f"Mô hình đã được lưu tại: {model_filepath}")
    
    # Đánh giá mô hình
    evaluation = model.evaluate(X_val, y_val)
    print(f"Độ chính xác trên tập validation: {evaluation[1]:.4f}")
    
    # Lưu thông tin mô hình
    with open(os.path.join(MODEL_DIR, 'model_info.txt'), 'w') as f:
        f.write(f"Số lượng lớp: {len(class_names)}\n")
        f.write(f"Các lớp: {', '.join(class_names)}\n")
        f.write(f"Kích thước input: {X_train.shape[1:]}\n")
        f.write(f"Độ chính xác validation: {evaluation[1]:.4f}\n")
    
    return model, history, class_names

if __name__ == "__main__":
    train_model()
