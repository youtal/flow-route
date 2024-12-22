import requests
import os
import itertools


def get_room_info(room_name, shard):
    response = requests.get(f'https://screeps.com/api/game/room-terrain?room={room_name}&shard={shard}&encoded=1')
    res = response.json()
    # 获取res所有的key
    # print(res.keys())
    return res['terrain'][0]['terrain']


def fetch_all_room_info():
    base_url = "https://screeps.com/api/game/room-terrain"
    directions = {'c2': ['N', 'S'], 'c1': ['W', 'E']}
    n1_range = range(0, 2)
    n2_range = range(0, 2)
    n3_range = range(0, 2)
    file_path = 'output/db.txt'
    # 检查output文件夹下是否存在db.txt文件,存在则删除
    # if os.path.exists(file_path):
    # os.remove(file_path)
    # 创建db.txt文件
    # os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w') as file:
        for n1, n2, n3, c1, c2 in itertools.product(n1_range, n2_range, n3_range, directions['c1'], directions['c2']):
            room = f'{c1}{n1}{c2}{n2}'
            shard = f'shard{n3}'
            params = {
                'room': room,
                'shard': shard,
                'encoded': 1
            }
            try:
                response = requests.get(base_url, params=params)
                res = response.json()
                file.write(f'{room} {shard} {res["terrain"][0]["terrain"]}\n')
                print(f'Fetch {room} {shard} successfully')
            except Exception as e:
                print(f'Error: {e} when fetching {room} {shard}')
                continue

    print('Fetch all room info successfully')


def test():
    # 指定文件路径
    file_path = "path/to/your/asdfghjkl.txt"

    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 创建文件
        with open(file_path, 'w') as file:
            file.write("这是一个新创建的文件。\n")

        print(f"文件已成功创建：{os.path.abspath(file_path)}")
    except Exception as e:
        print(f"发生错误：{e}")
