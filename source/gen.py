#!/usr/bin/env python
# coding:utf-8:
import os

PAGES = [
    ('Principal', 'index'),
    ('Programa y bibliografía', 'programa-y-bibliografia'),
    ('Cronograma', 'cronograma'),
    ('Instancias de evaluación', 'instancias-de-evaluacion'),
    ('Clases teóricas', 'clases'),
    ('Prácticas', 'practicas'),
]

def menu():
    html = []
    for title, page in PAGES:
        html.append(
          '<p><a href="{page}.html">{title}</a></p>'.format(
            title=title,
            page=page,
          )
        )
    return ''.join(html)

def generate(title, page):
    print('Generando {title} ({page})'.format(title=title, page=page))

    f = open('template.html', 'r')
    html = f.read()
    f.close()

    content = os.popen('pandoc {page}.md'.format(page=page)).read()

    html = html.replace('$MENU$', menu())
    html = html.replace('$CONTENT$', content)

    f = open('../{page}.html'.format(page=page), 'w')
    f.write(html)
    f.close()

if __name__ == '__main__':
    for title, page in PAGES:
        generate(title, page)

