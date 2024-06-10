from pydub import AudioSegment
import os
from VolumeBalancer import balancer


def generate_testing_data(orig_file_path):
    # 讀取音樂檔案
    print("正在讀取音樂檔案...")
    input_file = orig_file_path
    audio = AudioSegment.from_file(input_file)
    print("音樂檔案讀取完成")

    # 调整音量
    print("正在調整音量...")
    quieter_audio = audio - 10  # 减小音量
    louder_audio = audio + 10   # 增大音量
    print("音量調整完成")

    base, ext = os.path.splitext(input_file)

    # 保存调整后的音频文件
    quieter_output_file = base + "_quieter" + ext
    louder_output_file = base + "_louder" + ext

    print("正在保存调整后的音频文件...")
    quieter_audio.export(quieter_output_file, format=ext[1:])
    louder_audio.export(louder_output_file, format=ext[1:])
    print("调整后的音频文件已保存")

    print("较小声和较大声的音频文件已生成。")


def main():
    folder_path = "D:\音樂\mmm"
    # folder_path = "aaa"
    balancer(folder_path)
    pass


if __name__ == '__main__':
    # generate_testing_data("testdata\Operation Pine Soot-危機合約-Arknights.mp3")
    main()
    pass
