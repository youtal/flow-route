import requests


def get_room_info(room_name, shard):
    response = requests.get(f'https://screeps.com/api/game/room-terrain?room={room_name}&shard={shard}&encoded=1')
    res = response.json()
    # 获取res所有的key
    # print(res.keys())
    return res['terrain'][0]['terrain']
