"""Re-theme legacy dark pages into the FOX PT palette (#590907 / #e8d2b5 / #a5a79b) with gradients.
Usage: python3 retheme.py <in_root> <out_root>
"""
import re, sys, os, colorsys

MAROON = (89, 9, 7)

def hx(c): return '#%02x%02x%02x' % tuple(max(0, min(255, round(v))) for v in c)
def mix(a, b, t): return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))
def parse_hex(h):
    h = h.lstrip('#')
    if len(h) in (3, 4): h = ''.join(ch * 2 for ch in h)
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
    return (r, g, b), a
def P(h): return parse_hex(h)[0]

# ---- palette ramps ----
BG_RAMP = [(0.00, P('#e6cfb0')), (0.06, P('#ecdcc4')), (0.10, P('#f6ede0')), (0.15, P('#faf3e9')),
           (0.22, P('#efe2cf')), (0.35, P('#dcc5a6')), (0.55, P('#b9a68c')), (0.75, P('#7d1a14')), (1.0, P('#590907'))]
TEXT_RAMP = [(0.0, P('#f8eedf')), (0.22, P('#efe0ca')), (0.30, P('#a5a79b')), (0.45, P('#7c7e71')),
             (0.60, P('#5d5f54')), (0.75, P('#3f2421')), (0.9, P('#2a0504')), (1.0, P('#2a0504'))]

def ramp(R, t):
    for (t0, c0), (t1, c1) in zip(R, R[1:]):
        if t <= t1: return mix(c0, c1, (t - t0) / (t1 - t0) if t1 > t0 else 0)
    return R[-1][1]

ACCENTS = [  # (hue_from, hue_to, base)
    (0, 15, P('#9b2a1f')),     # red -> brick
    (15, 40, P('#8a3b12')),    # orange -> burnt
    (40, 70, P('#8a6326')),    # amber -> caramel
    (70, 165, P('#4d5a34')),   # green -> olive (sage family)
    (165, 200, P('#5b6356')),  # cyan/teal -> deep sage
    (200, 265, P('#590907')),  # blue/indigo -> maroon (primary)
    (265, 300, P('#6a2b45')),  # purple -> plum
    (300, 345, P('#8e2f45')),  # pink -> rose wine
    (345, 361, P('#9b2a1f')),
]
def accent_base(h):
    for a, b, c in ACCENTS:
        if a <= h < b: return c
    return ACCENTS[0][2]

def classify(rgb):
    r, g, b = [v / 255 for v in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    neutral = s < 0.30 or l < 0.17 or l > 0.95 or (l < 0.32 and s < 0.5)
    return neutral, h * 360, l, s

def fmt(c, a):
    if a >= 0.999: return hx(c)
    return 'rgba(%d,%d,%d,%s)' % (*[round(v) for v in c], ('%.3f' % a).rstrip('0').rstrip('.'))

def map_color(rgb, a, ctx):
    neutral, h, l, s = classify(rgb)
    if ctx == 'generic':
        ctx = 'text' if (neutral and l >= 0.5) else 'bg'
    if neutral:
        if ctx == 'text':
            if a < 1 and l > 0.85: return fmt(P('#2a0504'), max(a, 0.5))
            return fmt(ramp(TEXT_RAMP, l), a)
        if ctx in ('border',):
            if a < 1 and l > 0.85: return fmt(MAROON, min(0.32, max(0.10, a * 2.2)))
            if l < 0.12: return fmt(MAROON, 0.10 if a >= 1 else max(0.06, a * 0.25))
            return fmt(MAROON, min(0.40, 0.08 + l * 0.6) * (a if a < 1 else 1) if a < 1 else min(0.40, 0.08 + l * 0.6))
        if ctx == 'shadow':
            return fmt(MAROON, min(0.28, a * 0.35) if l < 0.3 else min(0.25, a * 0.6))
        # bg
        if a < 1:
            if l > 0.85: return fmt(P('#fffaf2'), min(0.9, 0.35 + a * 2))
            if max(rgb) < 10: return fmt(MAROON, min(0.35, a * 0.4))  # pure-black backdrops
            if l < 0.12: return fmt(P('#fbf4ea'), min(0.94, max(0.7, a)))  # dark glass panels -> cream glass
            return fmt(ramp(BG_RAMP, l), min(0.95, a + 0.15))
        return fmt(ramp(BG_RAMP, l), a)
    base = accent_base(h)
    if ctx == 'text':
        return fmt(base if l > 0.35 else mix(base, P('#f8eedf'), 0.0), a)
    if ctx == 'shadow':
        return fmt(base, min(0.3, a * 0.6))
    if ctx == 'border':
        return fmt(base, a if a < 1 else 0.85)
    # bg
    if a >= 1 and l > 0.72:  # pastel solid background -> soft tint
        return fmt(base, 0.16)
    return fmt(base, a)

def shade(css):
    """darker partner for gradient"""
    m = re.match(r'#([0-9a-f]{6})$', css)
    if m:
        c = P(css); return hx(mix(c, (0, 0, 0), 0.22)) if sum(c) < 420 else hx(mix(c, P('#d9bf9b'), 0.45))
    m = re.match(r'rgba\((\d+),(\d+),(\d+),([\d.]+)\)', css)
    if m:
        c = tuple(int(x) for x in m.groups()[:3]); a = float(m.group(4))
        return fmt(mix(c, (0, 0, 0), 0.2) if sum(c) < 420 else mix(c, P('#d9bf9b'), 0.45), a)
    return css
def light(css):
    m = re.match(r'#([0-9a-f]{6})$', css)
    if m:
        c = P(css); return hx(mix(c, P('#c4483b'), 0.28)) if sum(c) < 420 else hx(mix(c, (255, 252, 246), 0.35))
    return css

COL_RE = re.compile(r'(?<![\w&])#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b(?!-)|rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*(?:,\s*[\d.]+%?\s*)?\)|\b(?:white|black)\b(?![-\w])')

def tok_to_rgb(t):
    t2 = t.strip()
    if t2 == 'white': return (255, 255, 255), 1.0
    if t2 == 'black': return (0, 0, 0), 1.0
    if t2.startswith('#'): return parse_hex(t2)
    nums = re.findall(r'[\d.]+%?', t2)
    r, g, b = (int(nums[0]), int(nums[1]), int(nums[2]))
    a = 1.0
    if len(nums) > 3: a = float(nums[3].rstrip('%')) / (100 if nums[3].endswith('%') else 1)
    return (r, g, b), a

def recolor_value(val, ctx):
    return COL_RE.sub(lambda m: map_color(*tok_to_rgb(m.group(0)), ctx), val)

def prop_ctx(prop, varctx=None):
    p = prop.lower().strip()
    if p.startswith('--'):
        if varctx and p in varctx: return varctx[p]
        n = p
        if re.search(r'bg|card|panel|glass|surface|overlay|back', n): return 'bg'
        if re.search(r'border|line|divider|outline', n): return 'border'
        if re.search(r'text|muted|dim|fg|subtle|font', n): return 'text'
        if re.search(r'shadow|glow', n): return 'shadow'
        return 'generic'
    if p in ('color', '-webkit-text-fill-color', 'caret-color', 'fill', 'stroke', 'text-decoration-color', 'column-rule-color', 'accent-color'): return 'text'
    if p.startswith('background'): return 'bg'
    if p.startswith('border') or p.startswith('outline'): return 'border'
    if 'shadow' in p: return 'shadow'
    return 'generic'

DECL_RE = re.compile(r'(?P<prop>--[\w-]+|[a-zA-Z-]+)\s*:\s*(?P<val>[^;{}]+)')

def var_usage(css):
    """for each --var, which contexts use it"""
    use = {}
    for m in DECL_RE.finditer(css):
        prop = m.group('prop')
        for v in re.findall(r'var\(\s*(--[\w-]+)', m.group('val')):
            use.setdefault(v.lower(), set()).add(prop_ctx(prop) if not prop.startswith('--') else 'var')
    return use

SINGLE_RE = re.compile(r'^\s*(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\))\s*(!important)?\s*$')

def gradientize(val, kind):
    m = SINGLE_RE.match(val)
    if not m: return val
    c = m.group(1)
    if c.startswith('rgba') and float(re.findall(r'[\d.]+', c)[-1]) < 0.5:
        return val  # translucent tint: keep
    imp = ' !important' if m.group(2) else ''
    if kind == 'page':
        return 'linear-gradient(160deg, #f1e3cf 0%%, #e8d2b5 45%%, #dcc19c 100%%)%s' % imp
    return 'linear-gradient(135deg, %s 0%%, %s 100%%)%s' % (light(c), shade(c), imp)

def process_css(css, varctx=None, is_root_style=True):
    use = var_usage(css) if is_root_style else {}
    # vars used only as backgrounds can become gradients
    grad_vars = {v for v, ctxs in use.items() if ctxs and ctxs <= {'bg'}}
    out = []
    pos = 0
    for m in DECL_RE.finditer(css):
        prop, val = m.group('prop'), m.group('val')
        ctx = prop_ctx(prop, varctx)
        if prop.startswith('--') and prop.lower() in use:
            cs = use[prop.lower()]
            if cs == {'text'}: ctx = 'text'
            elif cs <= {'bg'}: ctx = 'bg'
            elif cs <= {'border'}: ctx = 'border'
            elif 'text' in cs and ctx == 'generic': ctx = 'text'
        # rgb triplet vars like --theme-rgb: 16, 185, 129
        if prop.startswith('--') and re.fullmatch(r'\s*\d+\s*,\s*\d+\s*,\s*\d+\s*', val):
            r, g, b = [int(x) for x in val.split(',')]
            mc = map_color((r, g, b), 1.0, 'border')
            c = P(mc) if mc.startswith('#') else MAROON
            newval = ' %d, %d, %d' % tuple(round(x) for x in c)
        else:
            newval = recolor_value(val, ctx)
            pl = prop.lower()
            if pl in ('background', 'background-color') and ctx == 'bg':
                kind = 'card'
                newval = gradientize(newval, kind)
                if newval.strip().startswith('linear-gradient') and pl == 'background-color':
                    prop = 'background'
            if prop.startswith('--') and prop.lower() in grad_vars:
                kind = 'page' if re.fullmatch(r'--(bg|bg-color|bg-primary|background)', prop.lower()) else 'card'
                newval = gradientize(newval, kind)
        out.append(css[pos:m.start()]); out.append(prop + ':' + newval); pos = m.end()
    out.append(css[pos:])
    res = ''.join(out)
    def textgrad(m):
        body = m.group(2)
        if re.search(r'background-clip\s*:\s*text', body) or re.search(r'text-fill-color\s*:\s*transparent', body):
            body = re.sub(r'(?<![\w-])background(-image)?\s*:[^;{}]*', 'background:linear-gradient(120deg,#590907 0%,#8c2a1d 50%,#6b6e5f 100%)', body)
        return m.group(1) + '{' + body + '}'
    res = re.sub(r'([^{}]+)\{([^{}]*)\}', textgrad, res)
    # background-color: var(--gradvar) -> background:
    for v in grad_vars:
        res = re.sub(r'background-color\s*:\s*var\(\s*%s\s*\)' % re.escape(v), 'background:var(%s)' % v, res, flags=re.I)
    return res

def process_html(html):
    # style blocks
    html = re.sub(r'(<style[^>]*>)(.*?)(</style>)', lambda m: m.group(1) + process_css(m.group(2)) + m.group(3), html, flags=re.S | re.I)
    # inline style attributes
    html = re.sub(r'(style\s*=\s*")([^"]*)(")', lambda m: m.group(1) + process_css(m.group(2), is_root_style=False) + m.group(3), html, flags=re.I)
    html = re.sub(r"(style\s*=\s*')([^']*)(')", lambda m: m.group(1) + process_css(m.group(2), is_root_style=False) + m.group(3), html, flags=re.I)
    # svg fill/stroke attrs
    html = re.sub(r'((?:fill|stroke|stop-color)\s*=\s*")(#[0-9a-fA-F]{3,8}|rgba?\([^)]*\))(")', lambda m: m.group(1) + recolor_value(m.group(2), 'text') + m.group(3), html)
    # scripts: recolor literals; css-like strings inside get decl handling first
    def scr(m):
        body = m.group(2)
        body = re.sub(r'((?:color|background|border[\w-]*|box-shadow|fill|stroke)\s*[:=]\s*[\'"`]?)([^;\'"`]*?#[0-9a-fA-F]{3,8}|[^;\'"`]*?rgba?\([^)]*\))', lambda k: k.group(1) + recolor_value(k.group(2), prop_ctx(re.match(r'[\w-]+', k.group(1)).group(0))), body)
        body = COL_RE.sub(lambda k: map_color(*tok_to_rgb(k.group(0)), 'generic') if not k.group(0) in ('white', 'black') else k.group(0), body)
        return m.group(1) + body + m.group(3)
    html = re.sub(r'(<script(?![^>]*src)[^>]*>)(.*?)(</script>)', scr, html, flags=re.S | re.I)
    return html

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    for root, _, files in os.walk(src):
        for f in files:
            if not f.endswith('.html'): continue
            p = os.path.join(root, f); rel = os.path.relpath(p, src)
            if rel in ('index.html',) or 'immunology' in rel: continue
            o = os.path.join(dst, rel); os.makedirs(os.path.dirname(o), exist_ok=True)
            open(o, 'w', encoding='utf8').write(process_html(open(p, encoding='utf8').read()))
            print('ok', rel)
