import os
import sox


class Sox:
    tfm = sox.Transformer()

    def __init__(self, path):
        self.root_path = path

    def convert_to_wav(self):
        if os.path.isdir(self.root_path):
            files = os.listdir(self.root_path)
            for file in files:
                file_name = os.path.splitext(file)[0]
                self.tfm.build_file(
                    f'{self.root_path}/{file}', f'./{file_name}.wav')


# 変換したい音声ファイルのルートパスを指定
ROOT_PATH = ''
instance = Sox(ROOT_PATH)
instance.convert_to_wav()
