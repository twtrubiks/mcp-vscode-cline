import requests
import os
import logging
import argparse

HTTP_ERROR_MSG = 'HTTP error {res.status_code} - {res.reason}'

user_agent_string = "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"

headers = {
    'User-Agent': user_agent_string
}

path = "/ptt" # 改成你自己的路徑

if __name__ == "__main__":
    """
    python app.py "https://xxxxx.jpeg"
    """

    parser = argparse.ArgumentParser(description="根據提供的 URL 下載單張圖片 (簡易版 Demo)")
    parser.add_argument("image_url", help="要下載的圖片的完整 URL。")

    args = parser.parse_args()
    url_to_download = args.image_url

    try:
        res_img = requests.get(url_to_download, stream=True, verify=False, headers=headers)
        logging.debug('download image {} ......'.format(url_to_download))

        res_img.raise_for_status()
    except requests.exceptions.HTTPError as exc:
        logging.warning(HTTP_ERROR_MSG.format(res=exc.response))
        logging.warning(url_to_download)
    except requests.exceptions.ConnectionError:
        logging.error('Connection error')
    else:
        file_name = url_to_download.split('/')[-1]
        file = os.path.join(path, file_name)
        try:
            with open(file, 'wb') as out_file:
                out_file.write(res_img.content)
                print(f"成功: {url_to_download} {file}")
        except Exception as e:
            logging.warning(e)