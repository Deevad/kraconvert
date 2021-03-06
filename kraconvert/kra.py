import zipfile
import os
#import PIL
from lxml import etree as ET


__author__ = 'pierre'


class Kra(object):

    maindoc_xml = None
    merged_image = None
    basename = None
    icc = None

    def __init__(self, krafile):

        kra = zipfile.ZipFile(krafile)


        self.filename = os.path.basename(krafile)

        self.basename, _ = self.filename.split('.')


        self.merged_image = kra.read('mergedimage.png')
        self.xml = ET.fromstring(kra.read('maindoc.xml'))
        self.icc = kra.read('{basename}/annotations/icc'.format(basename=self.basename))

    def get_basename(self):
        return self.basename

    def get_merged_image(self):
        return self.merged_image

    def get_icc(self):
        ns = {'kra': 'http://www.calligra.org/DTD/krita'}
        x = self.xml.find('.//kra:IMAGE', ns)
        icc_name = x.attrib['profile']
        return {'name': icc_name, 'data': self.icc}