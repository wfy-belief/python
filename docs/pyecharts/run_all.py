import os
import re


def update_file(file_: str):
    """
    Args:
        file_: 文件对应的路径

    Returns:
        添加CDN加速链接资源
    """
    with open(file_, 'r+', encoding='UTF-8') as fp:
        file_str = fp.read()
        # 清空内容
        fp.truncate()
        # 回到起点
        fp.seek(0)
        sub_str = '''from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/gh/pyecharts/pyecharts-assets@latest/assets/"
'''
        if sub_str not in file_str:
            fp.write(sub_str)
        fp.write(file_str)
        fp.close()
    with open(file_, 'r+', encoding='UTF-8') as fp:
        result_str = fp.read()
        # print(result_str)
        write_md_file(file_, result_str)
        fp.close()


def write_md_file(file_: str, content: str):
    file_ = file_.replace('.py', '.md')
    with open(file_, 'r+', encoding='UTF-8') as fp:
        # 原文件内容
        r_str = fp.read()
        # 回到开头
        fp.seek(0)
        result_str = re.sub(r'(```python)([\s\S]*?)(```)', rf'\1\n{content}\3', r_str)
        fp.write(result_str)
        fp.close()


if __name__ == '__main__':
    PATH = os.getcwd()
    for root, dirs, files in os.walk('./'):
        if root == './':
            continue
        # 筛选.py 文件
        files = list(filter(lambda f: f.endswith('.py'), files))
        # print(files)
        # 切换目录
        dir_name = os.path.join(PATH, root)
        os.chdir(dir_name)
        print(dir_name)
        for file in files:
            update_file(file)
            exec_status_code = os.popen(f'python {file}').readlines()
        os.chdir(PATH)
