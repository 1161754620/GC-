# coding:utf-8
import os.path
def get_gc_result():
    gc = 4161  # GC时长
    gc_time = int(gc)
    path = input("输入操作路径：\n")
    os.chdir(path)
    files = os.listdir('.')
    for file in files:
        if file.endswith('.txt'):
            with open(file, 'r',encoding='UTF-8') as fp:
                lines = fp.readlines()
                if 'not found' in lines[0]:
                    print("文件名：" + file + "\nGC失败")
                    continue
                first = lines[1]
                first_no = first[-9:-1]
                first_no = float(first_no)
                last = lines[-1]
                last_no = last[-9:-1]
                last_no = float(last_no)
                g = float((gc_time - last_no + first_no) / gc_time)

                print("文件名：" + file)
                # print("GC值为：%.2f%%" % (g * 100))
                print("%.2f%%" % (g * 100))

if __name__ == '__main__':
    while True:
        get_gc_result()
