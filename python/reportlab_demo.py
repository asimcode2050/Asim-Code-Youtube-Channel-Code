from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF
d = Drawing(100,100)
s = String(50,50,'Asim , Code',textAnchor='middle')
d.add(s)
renderPDF.drawToFile(d,'demo.pdf', 'Simple PDF demo')