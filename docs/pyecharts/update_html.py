import os
import re


def update_file(file_):
    add_html = """
<link rel="icon" href="https://cdn.jsdelivr.net/gh/wfy-belief/PicGo-images/img/favicon.png">
<script>
        try {
            top.location.hostname;
            if (top.location.hostname != window.location.hostname) {
                top.location.href = window.location.href;
            }
        } catch (e) {
            top.location.href = window.location.href;
        }
    </script>
"""
    with open(file_, 'r+', encoding='UTF-8') as fp:
        # 原文件内容
        r_str = fp.read()
        # 回到开头
        fp.seek(0)
        result_str = re.sub(r'(<head>)([\s\S]*?)(<meta)', rf'\1\n{add_html}\3', r_str)
        fp.write(result_str)
        fp.close()


if __name__ == '__main__':
    PATH = os.getcwd()
    for root, dirs, files in os.walk('./'):
        if root == './':
            continue
        # 筛选.py 文件
        files = list(filter(lambda f: f.endswith('.html'), files))
        # print(files)
        # 切换目录
        dir_name = os.path.join(PATH, root)
        os.chdir(dir_name)
        print(dir_name)
        for file in files:
            update_file(file)
            exec_status_code = os.popen(f'python {file}').readlines()
        os.chdir(PATH)
