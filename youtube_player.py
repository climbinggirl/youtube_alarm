# youtube random video player
import json
import requests
import string
import random
import webbrowser


COUNT = 50
API_KEY = 'AIzaSyCPVY2z2uKhrgRYUZ-s-D408LYhpqv1jq0'

# getting a link to random YouTube Video
def main():
    search_str = ''.join(random.choice(string.ascii_uppercase + string.digits)
                   for _ in range(3))
    search_url = "https://www.googleapis.com/youtube/v3/search" \
              "?key={}&maxResults={}&part=snippet&type=video&q={}" \
        .format(API_KEY, COUNT, search_str)
    response = requests.get(search_url)
    if response.status_code != 200:
        raise Exception("url {} returns {} code expect 200".format(search_url, response.status_code))

    data = response.json()
    encoding = json.dumps(data)
    results = json.loads(encoding)

    video_id = ''
    if len(results['items']) > 0:
        video_id = results['items'][0]['id']['videoId']

    if not video_id:
        raise Exception("no video founds in {}".format(search_url))

    # play video
    yt_url = "https://www.youtube.com/watch?v={}".format(video_id)
    webbrowser.open(yt_url)


if __name__ == '__main__':
    main()

