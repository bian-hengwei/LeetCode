import os
import re

# 自动生成目录页
if __name__ == '__main__':
    # languages names dictionary
    LANGUAGES = {'cpp': 'C++', 'java': 'Java', 'py': 'Python', 'js': 'JavaScript'}

    # markdown file names (sorted)
    all_markdowns = os.listdir('./docs')
    all_markdowns.sort(key=lambda _: int(re.search('^(\d+)\..*\.md$', _)[1]))
    # solution file names
    all_solutions = os.listdir('./codes')
    
    # README.md
    content = '# LeetCode\n已完成{}题  \n|序号|标题|代码|\n|:-:|:-:|:-:|\n'.format(len(all_markdowns))

    # loop in order
    for file in all_markdowns:

        # get link from markdown files
        with open('./docs/' + file, 'r', encoding='utf-8') as f:
            link = f.readlines()[7]
        if 'https://' not in link: print('ERROR: LeetCode link not found in line 8 of', file)
        link = link[link.find('https://')::].strip()
        print(link)

        ord_title = file.split('.')
        title = ord_title[1]
        if (len(title) > 10):
            title = title[:9] + '...'
        sols = sorted([sol for sol in all_solutions if sol.split('.')[0] == ord_title[0]])
        print(sols)
        for i, sol in enumerate(sols):
            content += '|-|-|' if i != 0 else '|[{}]({})|[{}](./docs/{})|'.format(ord_title[0], link, title, file)
            content += '[{}](./codes/{})|\n'.format(LANGUAGES[sol.split('.')[2]], sol)
    content += '  \n[:trollface:](./REWRITE.md)\n'

    with open('./README.md', 'w', encoding='utf-8') as f:
        f.write(content)