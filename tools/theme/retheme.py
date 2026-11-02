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

# ---- palette: deep olive pages, charcoal cards, off-white text, maroon accents ----
BG_RAMP = [(0.00, P('#55574d')), (0.06, P('#5c5e54')), (0.08, P('#33342d')), (0.12, P('#2b2c26')), (0.17, P('#36372f')),
           (0.25, P('#43443b')), (0.40, P('#5d5f54')), (0.60, P('#8b8d81')), (0.80, P('#cdb99c')), (1.0, P('#e8d2b5'))]
TEXT_RAMP = [(0.0, P('#22231e')), (0.18, P('#2b2c26')), (0.30, P('#7f8176')), (0.45, P('#a5a79b')),
             (0.60, P('#c7bfae')), (0.75, P('#e3cfb3')), (0.9, P('#f4e7d4')), (1.0, P('#f7ecdc'))]
OFF = P('#e8d2b5')

def ramp(R, t):
    for (t0, c0), (t1, c1) in zip(R, R[1:]):
        if t <= t1: return mix(c0, c1, (t - t0) / (t1 - t0) if t1 > t0 else 0)
    return R[-1][1]

#            hue range      light (text/tint)    deep (solid bg)
ACCENTS = [(0, 15,   P('#f0937f'), P('#7a140e')),   # red -> coral / brick
           (15, 40,  P('#e6ab7c'), P('#7a3510')),   # orange
           (40, 70,  P('#e6c88f'), P('#6e5320')),   # amber -> restrained gold
           (70, 165, P('#c2d09f'), P('#4d5a34')),   # green -> light sage / olive
           (165, 200, P('#bcc8b6'), P('#4a5649')),  # cyan
           (200, 265, P('#ecbda6'), P('#590907')),  # blue/indigo -> peach / maroon (primary)
           (265, 300, P('#d9adbd'), P('#5a2340')),  # purple
           (300, 345, P('#eaa1b0'), P('#74203a')),  # pink
           (345, 361, P('#f0937f'), P('#7a140e'))]
def accent(h):
    for a, b, lt, dp in ACCENTS:
        if a <= h < b: return lt, dp
    return ACCENTS[0][2], ACCENTS[0][3]

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
            return fmt(ramp(TEXT_RAMP, l), a)
        if ctx == 'border':
            if l < 0.12: return fmt(OFF, 0.07 if a >= 1 else max(0.05, a * 0.5))
            return fmt(OFF, min(0.35, (0.04 + l * 0.5) * (a if a < 1 else 1)))
        if ctx == 'shadow':
            return fmt(P('#141410'), min(0.6, a))
        if a < 1:
            if l > 0.85: return fmt(OFF, min(0.22, a * 1.6))       # white glass -> off-white glass
            if max(rgb) < 10: return fmt(P('#141410'), a)            # backdrops
            return fmt(ramp(BG_RAMP, l), max(a, 0.82))
        return fmt(ramp(BG_RAMP, l), a)
    lt, dp = accent(h)
    if ctx == 'text': return fmt(lt, a)
    if ctx == 'shadow': return fmt(dp, min(0.45, a * 0.8))
    if ctx == 'border': return fmt(lt, min(0.6, a if a < 1 else 0.55))
    if a < 0.5: return fmt(lt, min(0.22, a * 1.4))                    # tints
    if l > 0.72: return fmt(lt, 0.16)
    return fmt(dp, a)

def shade(css):
    m = re.match(r'#([0-9a-f]{6})$', css)
    if m: return hx(mix(P(css), (10, 10, 8), 0.28))
    m = re.match(r'rgba\((\d+),(\d+),(\d+),([\d.]+)\)', css)
    if m:
        c = tuple(int(x) for x in m.groups()[:3]); return fmt(mix(c, (10, 10, 8), 0.25), float(m.group(4)))
    return css
def light(css):
    m = re.match(r'#([0-9a-f]{6})$', css)
    if m:
        c = P(css); return hx(mix(c, (255, 245, 230), 0.10)) if sum(c) < 300 else hx(mix(c, (255, 250, 242), 0.25))
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
        return 'linear-gradient(160deg, #6b6d62 0%%, #5a5c52 45%%, #45473e 100%%)%s' % imp
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
            body = re.sub(r'(?<![\w-])background(-image)?\s*:[^;{}]*', 'background:linear-gradient(170deg,#fbf3e7 0%,#e8d2b5 55%,#c9a87e 100%)', body)
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
