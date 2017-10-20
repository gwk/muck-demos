from muck import *
from xml.etree.ElementTree import Element, ElementTree
from sys import stdout, stderr
from chart_data import rows


def add_el(parent, tag, **kwargs):
  try: text = kwargs.pop('text')
  except KeyError: text = None
  e = Element(tag, **dict((k.replace('_', '-'), str(v)) for k, v in kwargs.items()))
  if text is not None:
    e.text = text
  if parent is not None:
    parent.append(e)
  return e

w = 600
h = 600

svg = add_el(None, 'svg', xmlns='http://www.w3.org/2000/svg', display='block', width=f'100%', height=f'auto',
  viewBox=f'0 0 {w} {h}')

add_el(svg, 'rect', x=0, y=0, width=w, height=h, fill='none', stroke_width='1px', stroke='#808080')

inset_l = 100
inset_r = 60
inset_y = 10

vis_w = w - (inset_l + inset_r)
vis_h = h - 2 * inset_y

max_private_cost = max(r[1] for r in rows)

min_expectancy = min(r[3] for r in rows)
max_expectancy = max(r[3] for r in rows)
rng_expectancy = max_expectancy - min_expectancy

add_el(svg, 'text', x=10, y=h*0.5, alignment_baseline='middle', font_size=12, text_anchor='middle',
  text='PRIVATE HEALTH SPENDING PER PERSON IN 2016 (US$)', transform=f'rotate(-90 10 {h*0.5})')

add_el(svg, 'text', x=w-10, y=h*0.5, alignment_baseline='middle', font_size=12, text_anchor='middle',
  text='AVERAGE LIFE EXPECTANCY AT BIRTH', transform=f'rotate(90 {w-10} {h*0.5})')


g = add_el(svg, 'g', transform=f'translate({inset_l}, {inset_y})')

labeled_countries = {
  'United States',
  'Switzerland',
  'Australia',
  'Canada',
  'Ireland',
  'United Kingdom',
  'Turkey',
}

for r in sorted(rows, key=lambda r: r.private_cost):
  y1 = vis_h * (1 - r.private_cost / max_private_cost)
  y2 = vis_h * (1 - (r.expectancy - min_expectancy) / rng_expectancy)
  labeled = r.country in labeled_countries
  color = ('#FF6000' if r.country == 'United States' else ('#4040E0' if labeled else '#404040'))
  add_el(g, 'line', x1='0', y1=y1, x2=vis_w, y2=y2, stroke=color, stroke_width=2)

  if labeled:
    add_el(g, 'text', x=-2, y=y1, alignment_baseline='middle', font_size=8, text_anchor='end',
      text=f'{r.country} ${round(r.private_cost)}', fill=color)
    add_el(g, 'text', x=vis_w+2, y=y2, alignment_baseline='middle', font_size=8, text_anchor='start',
      text=f'{r.expectancy:0.1f} years', fill=color)

ElementTree(svg).write(stdout.buffer)
