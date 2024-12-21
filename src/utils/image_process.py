from PIL import Image
import os


def generate_image_from_dir(array, save_path, gx, gy):
    image_size = (1000, 1000)
    block_size = (20, 20)
    file_name = ['up_left', 'up', 'up_right', 'left', 'center', 'right', 'down_left', 'down', 'down_right', 'none']
    goal_img = Image.open(f'./assets/star.png').convert('RGBA').resize(block_size)
    # 打开图片，存放到arrow_list中
    arrow_list = []
    for name in file_name:
        try:
            arrow_list.append(Image.open(f'./assets/{name}.png').convert('RGBA'))
        except FileNotFoundError:
            print(f'Error: File ./assets/{name}.png not found')
            return
    for i in range(len(arrow_list)):
        arrow_list[i] = arrow_list[i].resize(block_size)
    # 生成一个空白的图片
    image = Image.new('RGB', image_size)
    # 将图片填充为白色
    image.paste((43, 43, 43), (0, 0, image_size[0], image_size[1]))
    # 遍历array，根据array的值，将对应的箭头放入image中
    for y in range(len(array)):
        for x in range(len(array[y])):
            arrow = array[y][x]
            if arrow < 0 or arrow >= len(arrow_list):
                print(f'Error: Invalid arrow index {arrow} at position ({x}, {y})')
                return
            # print(f'x: {x}, y: {y}, arrow: {arrow}')
            # 将箭头放入image中,处理透明色
            image.paste(arrow_list[arrow], (x * block_size[0], y * block_size[1]), mask=arrow_list[arrow])
    # 将goal放入image中
    image.paste(goal_img, (gx * block_size[0], gy * block_size[1]), mask=goal_img)
    # 确保保存路径中的目录存在
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    # 保存图片
    image.save(save_path)
