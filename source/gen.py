#!/usr/bin/env python
# coding:utf-8:
import os

PAGES = [
    ('Principal', 'index'),
    ('Programa y bibliografía', 'programa-y-bibliografia'),
    ('Instancias de evaluación', 'instancias-de-evaluacion'),
    ('Clases teóricas', 'clases'),
    ('Prácticas', 'practicas'),
    ('Trabajos prácticos', 'tps'),
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

    with open('template.html', 'r') as f:
        html = f.read()

    with open('{page}.html'.format(page=page)) as f:
        content = f.read()

    html = html.replace('$MENU$', menu())
    html = html.replace('$CONTENT$', content)

    with open('../{page}.html'.format(page=page), 'w') as f:
        f.write(html)

if __name__ == '__main__':
    for title, page in PAGES:
        generate(title, page)

