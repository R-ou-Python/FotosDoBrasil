# Extract images from PDF

import fitz
filename = "fabio_matos_dissertacao.pdf"
doc = fitz.open(filename)
for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:       # this is GRAY or RGB
            pix.writePNG(filename + " p%s-%s.png" % (i, xref))
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG(filename + " p%s-%s.png" % (i, xref))
            pix1 = None
        pix = None

