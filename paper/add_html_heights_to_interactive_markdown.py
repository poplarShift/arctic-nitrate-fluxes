#!/bin/python
import sys
if len(sys.argv)<=1:
    print('Specify a file name')
else:
    from selenium import webdriver
    driver = webdriver.PhantomJS()

    import re, os
    fname = sys.argv[1]

    with open(fname) as f:
        paper = f.read()

    def get_max_html_height(fname_html):
        if fname_html.split('.')[-1] != 'html':
            print(f'Does not look like an html file, skipping: "{fname_html}"')
        else:
            path = os.path.join('file://', os.getcwd(), fname_html)
            if os.path.exists(path):
                print(f'Reading file "{path}"...')
                driver.get(path)
                return max([
                    e.size['height']
                    for e in driver.find_elements_by_class_name('bk')
                ])
            else:
                print(f'Could not find file "{path}"')

    def add_height_to_markdown(m):
        return '![' + m.group(1) + '](' + m.group(2) + '){' + m.group(3) + ' width=100% height=' + str(get_max_html_height(m.group(2))) + '}'

    paper_sub = re.sub(r'\!\[(.*)\]\((.*)\)\{(.*)\}', add_height_to_markdown, paper)

    with open(fname, 'w') as f:
        f.write(paper_sub)
