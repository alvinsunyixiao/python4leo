def assert_integer(number, err_msg='not integer'):
    if not isinstance(number, int):
        raise ValueError(err_msg)

def assert_positive(number, err_msg='not positive'):
    if number <= 0:
        raise ValueError(err_msg)

def assert_leq(number, threshold):
    if number > threshold:
        raise ValueError("淘气的你!不要输太大的数要不然就爆炸啦!")

def draw_stars(num_stars, star='*'):
    assert_integer(num_stars, "星星数只能是整数!")
    assert_positive(num_stars, "星星数只能是正数!")
    assert_leq(num_stars, 3000)
    print((star + ' ') * num_stars)

def draw_square(length, star='*'):
    draw_rectangle(length, length, star)

def draw_rectangle(height, width, star='*'):
    assert_integer(height, "高度只能是整数!")
    assert_integer(width, "宽度只能是整数!")
    assert_leq(height, 50)
    assert_leq(width, 50)
    for i in range(height):
        if i == 0 or i == height - 1:
            print((star + ' ') * width)
        else:
            print(star + ' ' * (2 * width - 3) + star)

def draw_triangle(height, star='*'):
    assert_integer(height, "高度只能是整数!")
    assert_positive(height, "高度只能是正数!")
    assert_leq(height, 30)
    for i in range(height):
        print('  ' * (height - i - 1) + (star + ' ') * (2 * i + 1))
