import os
import re

# 自动生成目录页
if __name__ == '__main__':
    # languages names and counts dictionary
    LANGUAGES = {'cpp': 'C++', 'java': 'Java', 'py': 'Python', 'js': 'JavaScript', 'sql': 'SQL'}
    counts = {'cpp': [0, 0], 'java': [0, 0], 'py': [0, 0], 'js': [0, 0], 'sql': [0, 0]}

    # URL for searching
    URLBASE = 'https://github.com/bian-hengwei/LeetCode/search?l='

    # markdown file names (sorted)
    # re for (number).ANYSTRING.md
    all_markdowns = os.listdir('./docs')
    all_markdowns.sort(key=lambda _: int(re.search('^(\d+)\..*\.md$', _)[1]))
    
    # solution file names
    all_solutions = os.listdir('./codes')
    
    # README.md
    readme = f'# LeetCode\n已完成{len(all_markdowns)}题\n[:trollface:](./REWRITE.md)\n|序号|标题|代码|\n|:-:|:-:|:-:|\n'
    rewrite = '# Rewrite\n[返回目录](./README.md)\n|序号|标题|代码|\n|:-:|:-:|:-:|\n'

    # loop in order
    for file_idx, file in enumerate(all_markdowns):

        # get link from markdown files
        with open('./docs/' + file, 'r', encoding='utf-8') as f:
            md = f.readlines()
        link = md[7]
        if 'https://' not in link: print('ERROR: LeetCode link not found in line 8 of', file)
        link = link[link.find('https://')::].strip()

        # whether this file is included in REWRITE.md
        rewrite_flag = '[返回文件](../REWRITE.md)' in md[1]

        # get title
        ord_title = file.split('.')
        title = ord_title[1]

        # trim title
        if (len(title) > 10): title = title[:9] + '...'

        # get solution sorted according to solution index
        sols = sorted([sol for sol in all_solutions if sol.split('.')[0] == ord_title[0]])
        print(file_idx + 1, sols)

        # add lines
        for i, sol in enumerate(sols):
            lang = LANGUAGES[sol.split('.')[2]]
            counts[sol.split('.')[2]][1] += 1
            if i == 0: counts[sol.split('.')[2]][0] += 1
            readme += '|-|-|' if i != 0 else f'|[{ord_title[0]}]({link})|[{title}](./docs/{file})|'
            readme += f'[{lang}](./codes/{sol})|\n'
            if rewrite_flag:
                rewrite += '|-|-|' if i != 0 else f'|[{ord_title[0]}]({link})|[{title}](./docs/{file})|'
                rewrite += f'[{lang}](./codes/{sol})|\n'
    
    # languages stats table
    readme += '## 语言统计\n|语言|题解|总数|\n|:-:|:-:|:-:|\n'
    for lang in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(lang)
        if (lang[0] == 'py'): readme += f'|[{LANGUAGES[lang[0]]}]({URLBASE}python)|{lang[1][0]}|{lang[1][1]}|\n'
        else: readme += f'|[{LANGUAGES[lang[0]]}]({URLBASE}{lang[0]})|{lang[1][0]}|{lang[1][1]}|\n'

    # write to README.md
    with open('./README.md', 'w', encoding='utf-8') as f:
        f.write(readme)

    # write to REWRITE.md
    with open('./REWRITE.md', 'w', encoding='utf-8') as f:
        f.write(rewrite)