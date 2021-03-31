import os
import re

# 自动生成目录页
if __name__ == '__main__':
    LANGUAGES = {'cpp': 'C++', 'java': 'Java', 'py': 'Python'}
    content = '# LeetCode\n|序号|标题|代码|\n|-|-|-|\n'

    all_files = os.listdir('./docs')
    all_solutions = os.listdir('./codes')
    for file in sorted(all_files, key=lambda _: int(re.search('^(\d+)\..*\.md$', _)[1])):
        ord_title = file.split('.')
        sols = sorted([sol for sol in all_solutions if sol.split('.')[0] == ord_title[0]])
        print(sols)
        for i, sol in enumerate(sols):
            content += '|-|-|'if i != 0 else '|{}|[{}](./docs/{})|'.format(ord_title[0], ord_title[1], file)
            content += '[{}](./codes/{})|\n'.format(LANGUAGES[sol.split('.')[2]], sol)

    with open('./README.md', 'w', encoding='utf-8') as f:
        f.write(content)