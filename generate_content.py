import os
import re

# 自动生成目录页
if __name__ == '__main__':
    content = '# 目录  \n  \n'

    all_files = os.listdir('./docs')
    all_files.remove('Content.md')
    for file in sorted(all_files, key=lambda _: int(re.search('^(\d+)\..*\.md$', _)[1])):
        content += '[{}]({})  \n'.format(file[:-3], file)

    with open('./docs/Content.md', 'w', encoding='utf-8') as f:
        f.write(content)