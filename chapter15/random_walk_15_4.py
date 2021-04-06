from random import choice


class RandomWalk():
    """一个生成随机漫步的数据类"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # 所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表到达指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前几方向以及沿这个方向前几的距离
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_distance * x_direction

            y_direction = choice([1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x y值
            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)
