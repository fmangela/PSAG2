

def split_list_evenly(lst, n):
    """
    尽可能均分一个列表
    :param lst: 被分割的列表
    :param n: 分割份数
    :return: 一个被分割好的列表
    """
    # 计算每个小列表的最小元素数量
    min_size = len(lst) // n
    # 计算剩余的元素数量
    remainder = len(lst) % n
    # 初始化结果列表
    result = []
    start = 0
    for i in range(n):
        # 计算当前小列表的大小
        end = start + min_size + (1 if i < remainder else 0)
        # 切片并添加到结果列表中
        result.append(lst[start:end])
        # 更新起始位置
        start = end
    return result
