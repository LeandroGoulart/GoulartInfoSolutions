import math
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

D='node_modules/@fontsource/chakra-petch/files/'
bold_i=TTFont(D+'chakra-petch-latin-700-italic.woff')
med_i=TTFont(D+'chakra-petch-latin-500-italic.woff')

def glyph_d(font,ch,x=0,y=0,s=1.0):
    gs=font.getGlyphSet(); n=font.getBestCmap()[ord(ch)]
    pen=SVGPathPen(gs, ntos=lambda v: ('%.1f'%v).rstrip('0').rstrip('.'))
    gs[n].draw(TransformPen(pen,(s,0,0,s,x,y)))
    return pen.getCommands(), gs[n].width*s

def text_d(font,text,x,y,s,track):
    out=[];cx=x
    for ch in text:
        d,w=glyph_d(font,ch,cx,y,s); out.append(d); cx+=w+track*s
    return ' '.join(out), cx-x-track*s

TAN=math.tan(math.radians(10))
BAR_H=820; BAR_W=150
def bar_d(x0,w=BAR_W,h=BAR_H):
    k=TAN*h
    return f"M{x0} 0L{x0+w} 0L{x0+w+k:.1f} {h}L{x0+k:.1f} {h}Z"

g_d,g_adv=glyph_d(bold_i,'G')
BAR_X=g_adv+10
mark_right=BAR_X+BAR_W+TAN*BAR_H   # ~ right edge at top
MARK_L=33

# wordmark
GS=0.54            # GOULART scale  (cap ~378)
gou_d,gou_w=text_d(bold_i,'GOULART',0,0,GS,40)
# fit INFOSOLUTIONS to same width with tracking 90
n=len('INFOSOLUTIONS')
gs=med_i.getGlyphSet(); cm=med_i.getBestCmap()
adv=sum(gs[cm[ord(c)]].width for c in 'INFOSOLUTIONS')
tr=90
IS=gou_w/(adv+(n-1)*tr)
inf_d,inf_w=text_d(med_i,'INFOSOLUTIONS',0,0,IS,tr)
GOU_CAP=700*GS; INF_CAP=700*IS
print('GOU cap',GOU_CAP,'INFO cap',INF_CAP,'widths',gou_w,inf_w)

def svg(w,h,body,title,bg=None,extra=''):
    b=f'<rect width="{w:.0f}" height="{h:.0f}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" role="img" aria-labelledby="t">'
            f'<title id="t">{title}</title>{b}{body}</svg>\n')

def mark_group(cG,cB):
    return f'<path d="{g_d}" fill="{cG}"/><path d="{bar_d(BAR_X)}" fill="{cB}"/>'

PAD=90
mark_w=mark_right-MARK_L
def mark_only(cG,cB,bg=None):
    w=mark_w+2*PAD; h=BAR_H+2*PAD
    body=f'<g transform="matrix(1 0 0 -1 {PAD-MARK_L} {PAD+BAR_H})">{mark_group(cG,cB)}</g>'
    return svg(w,h,body,'Goulart InfoSolutions — marca',bg)

def horizontal(cG,cB,cName,cSub,cLine,bg=None):
    gap=150
    tx=mark_right+gap
    line_x=mark_right+gap/2
    total_w=tx+gou_w-MARK_L+2*PAD
    h=BAR_H+2*PAD
    # text block: GOULART top at 700 (cap), INFO baseline 0
    gou_base=700-GOU_CAP
    body=(f'<g transform="matrix(1 0 0 -1 {PAD-MARK_L} {PAD+BAR_H})">'
          f'{mark_group(cG,cB)}'
          f'<rect x="{line_x:.0f}" y="0" width="6" height="700" fill="{cLine}"/>'
          f'<g transform="translate({tx:.0f} {gou_base:.1f})"><path d="{gou_d}" fill="{cName}"/></g>'
          f'<g transform="translate({tx:.0f} 0)"><path d="{inf_d}" fill="{cSub}"/></g>'
          f'</g>')
    return svg(total_w,h,body,'Goulart InfoSolutions',bg)

DARK=dict(cG='#00A0EC',cB='#FF3B4E',cName='#E6EEF8',cSub='#00A0EC',cLine='#2B4666')
LIGHT=dict(cG='#0072B8',cB='#E0182D',cName='#0A1626',cSub='#0072B8',cLine='#B7C7DC')
MONOW=dict(cG='#E6EEF8',cB='#E6EEF8',cName='#E6EEF8',cSub='#E6EEF8',cLine='#E6EEF8')
MONOD=dict(cG='#0A1626',cB='#0A1626',cName='#0A1626',cSub='#0A1626',cLine='#0A1626')

o='../brand/logo/'
def w(name,s): open(o+name,'w').write(s)
w('goulart-infosolutions-horizontal.svg',horizontal(**DARK))
w('goulart-infosolutions-horizontal-light.svg',horizontal(**LIGHT))
w('goulart-infosolutions-horizontal-mono-white.svg',horizontal(**MONOW))
w('goulart-infosolutions-horizontal-mono-dark.svg',horizontal(**MONOD))
w('goulart-infosolutions-marca.svg',mark_only('#00A0EC','#FF3B4E'))
w('goulart-infosolutions-marca-light.svg',mark_only('#0072B8','#E0182D'))
w('goulart-infosolutions-marca-mono-white.svg',mark_only('#E6EEF8','#E6EEF8'))
w('goulart-infosolutions-marca-mono-dark.svg',mark_only('#0A1626','#0A1626'))

# favicon: rounded square, mark centered
S=512
sc=0.40*S/ BAR_H*1.0
mw=mark_w*sc; mh=BAR_H*sc
fx=(S-mw)/2; fy=(S-mh)/2
fav=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}"><title>Goulart InfoSolutions</title>'
     f'<rect width="{S}" height="{S}" rx="96" fill="#070E18"/>'
     f'<g transform="translate({fx-MARK_L*sc:.1f} {fy+mh:.1f}) scale({sc:.4f} {-sc:.4f})">{mark_group("#00A0EC","#FF3B4E")}</g></svg>\n')
open('../brand/logo/favicon.svg','w').write(fav)
print('mark_w',mark_w,'ratio',(mark_w+2*PAD)/(BAR_H+2*PAD))
