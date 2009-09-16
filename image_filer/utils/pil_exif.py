try:
    import Image
    import ExifTags
except ImportError:
    try:
        from PIL import Image
        from PIL import ExifTags
    except ImportError:
        raise ImportError("The Python Imaging Library was not found.")
from image_filer.utils import pexif
def get_exif(im):
    try:
        exif_raw = im._getexif() or {}
    except:
        return {}
    ret={}
    for tag, value in exif_raw.items():
        decoded = ExifTags.TAGS.get(tag, tag)
        ret[decoded] = value
    return ret
def get_exif_for_file(file):
    im = Image.open(file,'r')
    return get_exif(im)
def get_subject_location(exif_data):
    try:
        r = ( int(exif_data['SubjectLocation'][0]), int(exif_data['SubjectLocation'][1]), )
    except:
        r = None
    return r


def set_exif_subject_location(xy, in_path, out_path):
    #img = pexif.JpegFile.fromFile(in_path)
    img = pexif.JpegFile.fromString(in_path)
    #img = pexif.JpegFile(in_path, "fd", mode='rw')
    img.exif.primary.ExtendedEXIF.SubjectLocation = xy 
    return img.writeFile(out_path)