# -*- coding: utf-8 -*-
import time

import yaml

import bandopenapi.client as client


def main():
    test_band_key = None
    test_post_key = None
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        test_band_key = config['testBandKey']
        test_post_key = config['testPostKey']
    api = client.BandOpenApi()

    print('# 1. 사용자 정보 조회')
    print(api.get_profile())
    time.sleep(1)

    print('# 2. 밴드 목록 조회')
    bands = api.get_bands()
    print(bands)
    time.sleep(1)

    print('# 3. 글 목록 조회')
    posts = api.get_posts(band_key=test_band_key, locale='ko_KR')
    print(posts)
    time.sleep(1)

    print('# 4. 글 상세 조회')
    band_key = posts['items'][0]['band_key']
    post_key = posts['items'][0]['post_key']
    post = api.get_post(band_key=band_key, post_key=post_key)
    print(post)
    time.sleep(1)

    print('# 5. 글쓰기')
    post = api.create_post(band_key=test_band_key, content='test')
    print(post)
    time.sleep(1)

    print('# 6. 글 삭제')
    post_key = post['post_key']
    post = api.delete_post(band_key=test_band_key, post_key=post_key)
    print(post)
    time.sleep(1)

    print('# 7. 댓글 목록 조회')
    comments = api.get_post_comments(band_key=test_band_key, post_key=test_post_key)
    print(comments)
    time.sleep(1)

    print('# 8. 댓글 작성')
    create_post_comment_result = api.create_post_comments(band_key=test_band_key, post_key=test_post_key, body='body')
    print('create_post_comment_result', create_post_comment_result)
    time.sleep(1)

    print('# 9. 댓글 삭제')
    test_comment_key = comments['items'][0]['comment_key']
    delete_comment_result = api.delete_post_comments(band_key=test_band_key, post_key=test_post_key,
                                                     comment_key=test_comment_key)
    print(delete_comment_result)
    time.sleep(1)

    print('# 10. 앨범 목록 조회')
    albums = api.get_albums(band_key=test_band_key)
    print(albums)
    time.sleep(1)

    print('# 11. 사진 목록 조회')
    photo_album_key = albums['items'][0]['photo_album_key']
    photos = api.get_album_photos(band_key=test_band_key, photo_album_key=photo_album_key)
    print(photos)


if __name__ == "__main__":
    main()
