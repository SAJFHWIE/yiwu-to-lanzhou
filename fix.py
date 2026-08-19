import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove custom pane creation line
c = c.replace("map.createPane('routePane');map.getPane('routePane').style.zIndex=650;\n", "")

# Fix polyline options - remove pane:'routePane' and add bringToFront
old1 = "const l=L.polyline(d.co,{color:c,weight:4,opacity:.85,pane:'routePane'}).addTo(map);"
new1 = "const l=L.polyline(d.co,{color:c,weight:4,opacity:.85}).addTo(map);\n  l.bringToFront();"
c = c.replace(old1, new1)

old2 = "const hl=L.polyline(d.co,{color:dayColor,weight:4,opacity:.9,pane:'routePane'}).addTo(map);hlLines.push(hl)"
new2 = "const hl=L.polyline(d.co,{color:dayColor,weight:4,opacity:.9}).addTo(map);hl.bringToFront();hlLines.push(hl)"
c = c.replace(old2, new2)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done')
