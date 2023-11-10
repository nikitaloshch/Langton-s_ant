import numpy as np
from PIL import Image


def ant_path(size):
    ant_pos = np.array([size // 2, size // 2])  # начальная позиция в центре поля
    ant_direction = 0  # 0: вверх, 1: вправо, 2: вниз, 3: влево
    directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])  # Изменения координат в зависимости от направления
    image_data = np.ones((size, size), dtype=np.uint8) * 255  # белый фон
    black_cell_count = 0  # Счетчик черных клеток

    while all(0 <= pos < size for pos in ant_pos):
        is_white_cell = image_data[tuple(ant_pos)] == 255
        ant_direction = (ant_direction + 1) % 4 if is_white_cell else (ant_direction - 1) % 4
        # Инвертирование пикселя
        image_data[tuple(ant_pos)] ^= 255
        black_cell_count += not is_white_cell
        # Перемещение в соответствии с текущим направлением
        ant_pos = (ant_pos + directions[ant_direction])

    return image_data, black_cell_count


def save_image(image_data, filename):
    # Создаем изображение с глубиной цвета 1 бит
    img = Image.new('1', (image_data.shape[1], image_data.shape[0]))
    # Устанавливаем пиксели
    img.putdata(image_data.flatten())
    # Сохраняем изображение
    img.save(filename, format='PNG')


def main():
    size = 1024

    image_data, black_cell_count = ant_path(size)
    save_image(image_data, 'ant_path.png')

    print(f'Количество черных клеток: {black_cell_count}')


if __name__ == '__main__':
    main()