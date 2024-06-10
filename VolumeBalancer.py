import os
from pydub import AudioSegment
import numpy as np
from tqdm import tqdm


def calculate_volume(audio_file):
    """ 計算音量 """
    audio = AudioSegment.from_file(audio_file)
    return audio.dBFS


def adjust_volume(audio_file, target_volume):
    """ 調整音量 """
    audio = AudioSegment.from_file(audio_file)
    current_volume = audio.dBFS
    dB_difference = target_volume - current_volume
    adjusted_audio = audio + dB_difference
    return adjusted_audio


def find_minimum_volume(files):
    """ 尋找最低音量做為標準 """
    min_volume = float('inf')
    min_file = None
    for file in tqdm(files, desc="尋找最低音量"):
        volume = calculate_volume(file)
        if volume < min_volume and not (volume == float('-inf') or volume == float('inf')):
            min_volume = volume
            min_file = file
    return min_file, min_volume


def get_file_path(folder):
    """ 取得資料夾下所有音樂檔案的路徑 """
    audio_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith('.mp3') or file.endswith('.wav'):
                audio_files.append(os.path.join(root, file))
    return audio_files


def balancer(orig_folder):
    """ 放入資料夾，平衡其中的音樂的音量，以最小音量為標準 """
    # 創建新的資料夾
    new_folder = orig_folder + "_balance"
    os.makedirs(new_folder, exist_ok=True)

    # 讀取音樂檔案
    files = get_file_path(orig_folder)

    # 尋找標準音量
    min_file, min_volume = find_minimum_volume(files)
    print("最小音量的檔案是：", min_file)
    print("最小音量是：", min_volume)

    # 調整音量
    for file in tqdm(files, desc="调整音量並儲存"):
        adjusted_audio = adjust_volume(file, min_volume)
        relative_path = os.path.relpath(file, orig_folder)
        new_file_path = os.path.join(new_folder, relative_path)
        os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
        adjusted_audio.export(new_file_path, format='mp3')
        print(f"已调整音量并保存到: {new_file_path}", adjusted_audio.dBFS)
