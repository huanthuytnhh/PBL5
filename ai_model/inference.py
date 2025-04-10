import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import librosa
import pickle
import time

# Thiết lập các đường dẫn
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'model')
MODEL_PATH = os.path.join(MODEL_DIR, 'speaker_model.h5')
LABEL_ENCODER_PATH = os.path.join(MODEL_DIR, 'label_encoder.pkl')

# Tham số trích xuất đặc trưng (phải giống với tham số khi train)
SAMPLE_RATE = 44100  # Hz
N_MFCC = 40  # Số lượng đặc trưng MFCC
MAX_LENGTH = 200  # Độ dài tối đa của mảng đặc trưng

def extract_features(audio_path):
    """Trích xuất đặc trưng MFCC từ file âm thanh"""
    try:
        # Nạp file âm thanh
        y, sr = librosa.load(audio_path, sr=SAMPLE_RATE)
        
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
        print(f"Lỗi trích xuất đặc trưng: {e}")
        return None

def load_trained_model():
    """Tải mô hình đã huấn luyện"""
    try:
        # Tải mô hình
        model = load_model(MODEL_PATH)
        
        # Tải label encoder
        with open(LABEL_ENCODER_PATH, 'rb') as f:
            label_encoder = pickle.load(f)
        
        return model, label_encoder
    except Exception as e:
        print(f"Lỗi tải mô hình: {e}")
        return None, None

def predict_speaker(audio_path, threshold=0.7):
    """Dự đoán người nói từ file âm thanh"""
    # Tải mô hình và label encoder
    model, label_encoder = load_trained_model()
    if model is None or label_encoder is None:
        return None, 0.0
    
    # Trích xuất đặc trưng
    features = extract_features(audio_path)
    if features is None:
        return None, 0.0
    
    # Dự đoán
    start_time = time.time()
    
    # Thêm chiều batch
    features = np.expand_dims(features, axis=0)
    
    # Dự đoán
    predictions = model.predict(features)[0]
    
    # Tính thời gian dự đoán
    inference_time = time.time() - start_time
    
    # Lấy kết quả dự đoán có xác suất cao nhất
    max_prob = np.max(predictions)
    predicted_index = np.argmax(predictions)
    
    # Chỉ trả về kết quả nếu xác suất vượt ngưỡng
    if max_prob >= threshold:
        predicted_speaker = label_encoder.inverse_transform([predicted_index])[0]
        return predicted_speaker, max_prob, inference_time
    else:
        return "Không xác định", max_prob, inference_time

def main():
    """Hàm chính để kiểm tra dự đoán"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Dự đoán người nói từ file âm thanh')
    parser.add_argument('audio_path', type=str, help='Đường dẫn đến file âm thanh')
    parser.add_argument('--threshold', type=float, default=0.7, help='Ngưỡng xác suất để chấp nhận dự đoán')
    
    args = parser.parse_args()
    
    speaker, confidence, inference_time = predict_speaker(args.audio_path, args.threshold)
    
    print(f"Người nói: {speaker}")
    print(f"Độ tin cậy: {confidence:.4f}")
    print(f"Thời gian dự đoán: {inference_time:.4f} giây")

if __name__ == "__main__":
    main()