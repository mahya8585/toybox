from PIL import Image, ImageFilter
import os
import requests


"""
顔にモザイクをかける処理 with faceAPI
"""

def create_blur_img(src_img, face_rectangle, blur_ratio):
    """
    ブラー効果を付与した画像を作成します
    :param src_img: 元画像
    :param face_rectangle: ブラー効果をかけたいエリアのtop, left, width, height のディクショナリ
    :param blur_ratio: blur率(float)
    :return:
    """
    top = face_rectangle['top']
    left = face_rectangle['left']

    # ブラー効果させたい部分を切り抜く
    src_crop = src_img.crop((
        left,
        top,
        left + face_rectangle['width'],
        top + face_rectangle['height']
    ))

    # 切り抜いた画像をブラー化する
    crop_blur = src_crop.filter(ImageFilter.GaussianBlur(blur_ratio))
    # 元画像にブラー化した画像を張り付ける
    src_img.paste(crop_blur, (left, top))

    return src_img


def get_face_rectangle(img):
    """
    Azure Cognitive Service face APIを呼び出し、顔の位置を取得する
    :param img:
    :return:
    """
    url = 'https://japaneast.api.cognitive.microsoft.com/face/v1.0/detect'
    header = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': 'xxxxx'
    }

    res = requests.post(url, headers=header, data=open(img, 'rb'))
    res_json = res.json()

    return res_json


def main():
    """
    ディレクトリ内すべての画像に処理をします
    :return:
    """
    # 作業ベースディレクトリ
    base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)))
    # モザイクをかけたい画像が入っているディレクトリ
    img_dir = os.path.join(base_dir, 'target')
    # モザイク加工済み画像が出力されるディレクトリ
    output_dir = os.path.join(base_dir, 'result')

    for image in os.listdir(img_dir):
        if image == '__init__.py':
            continue

        # imageの取得
        img_path = os.path.join(img_dir, image)
        im = Image.open(img_path)

        # TODO 顔位置の特定
        rectangles = get_face_rectangle(img_path)

        # blur処理
        blur_img = im
        for rectangle in rectangles:
            ratio = 15.0
            blur_img = create_blur_img(blur_img, rectangle['faceRectangle'], ratio)

        # ファイルの書き出し
        blur_img.save(os.path.join(output_dir, image), quality=100)


if __name__ == "__main__":
    main()