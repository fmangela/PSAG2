

def write_txt_file(filename, data):
    # 创建一个对象
    f = open(filename, 'w')
    # 写入数据
    for i in data:
        f.write(f"{i}\n")
    # 关闭文件
    f.close()
