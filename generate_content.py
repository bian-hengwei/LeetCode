import os
import re

# 自动生成目录页
if __name__ == '__main__':
    # languages names and counts dictionary
    LANGUAGES = {'cpp': 'C++', 'java': 'Java', 'py': 'Python', 'js': 'JavaScript'}
    counts = {'cpp': [0, 0], 'java': [0, 0], 'py': [0, 0], 'js': [0, 0]}

    # URL for searching
    URLBASE = 'https://github.com/bian-hengwei/LeetCode/search?l='

    # markdown file names (sorted)
    all_markdowns = os.listdir('./docs')
    all_markdowns.sort(key=lambda _: int(re.search('^(\d+)\..*\.md$', _)[1]))
    # solution file names
    all_solutions = os.listdir('./codes')
    
    # README.md
    readme = '# LeetCode\n已完成{}题\n[:trollface:](./REWRITE.md)\n|序号|标题|代码|\n|:-:|:-:|:-:|\n'.format(len(all_markdowns))
    rewrite = '# Rewrite\n[返回目录](./README.md)\n|序号|标题|代码|\n|:-:|:-:|:-:|\n'

    # loop in order
    for file in all_markdowns:

        # get link from markdown files
        with open('./docs/' + file, 'r', encoding='utf-8') as f:
            md = f.readlines()
        link = md[7]
        if 'https://' not in link: print('ERROR: LeetCode link not found in line 8 of', file)
        link = link[link.find('https://')::].strip()
        print(link)

        # whether this file is included in REWRITE.md
        rewrite_flag = '[返回文件](../REWRITE.md)' in md[1]

        # get title
        ord_title = file.split('.')
        title = ord_title[1]
        # trim title
        if (len(title) > 10): title = title[:9] + '...'

        # get solution sorted according to solution index
        sols = sorted([sol for sol in all_solutions if sol.split('.')[0] == ord_title[0]])
        print(sols)

        # add lines
        for i, sol in enumerate(sols):
            counts[sol.split('.')[2]][1] += 1
            if i == 0: counts[sol.split('.')[2]][0] += 1
            readme += '|-|-|' if i != 0 else '|[{}]({})|[{}](./docs/{})|'.format(ord_title[0], link, title, file)
            readme += '[{}](./codes/{})|\n'.format(LANGUAGES[sol.split('.')[2]], sol)
            if rewrite_flag:
                rewrite += '|-|-|' if i != 0 else '|[{}]({})|[{}](./docs/{})|'.format(ord_title[0], link, title, file)
                rewrite += '[{}](./codes/{})|\n'.format(LANGUAGES[sol.split('.')[2]], sol)
    
    # languages stats table
    readme += '## 语言统计\n|语言|题解|总数|\n|:-:|:-:|:-:|\n'
    for lang in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(lang)
        if (lang[0] == 'py'): readme += '|[{}]({})|{}|{}|\n'.format(LANGUAGES[lang[0]], URLBASE + 'python', lang[1][0], lang[1][1])
        else: readme += '|[{}]({})|{}|{}|\n'.format(LANGUAGES[lang[0]], URLBASE + lang[0], lang[1][0], lang[1][1])

    # write to README.md
    with open('./README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    # write to REWRITE.md
    with open('./REWRITE.md', 'w', encoding='utf-8') as f:
        f.write(rewrite)