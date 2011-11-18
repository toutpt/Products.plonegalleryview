from Products.CMFCore.permissions import AddPortalContent
from Products.CMFCore.utils import getToolByName

try:
  from Products.LinguaPlone.public import DisplayList
except ImportError:
  #no multilingual support!
  from Products.Archetypes.public import DisplayList


GLOBALS                 = globals()

PROJECTNAME             = "plonegalleryview"
SKINS_DIR               = 'skins'
STYLESHEETS             = (
                           {'id':           'pgv_sg_jd.gallery.css',
                            'media':        'all',
                            'rendering':    'import'},
#                           {'id':           'pgv_sg_slightbox.css',
#                            'media':        'all',
#                            'rendering':    'import'}, 
                           {'id':           'pgv_sg_styles.css',
                            'media':        'all',
                            'rendering':    'import'},                           
                          )
                          
JAVASCRIPTS             = (
                           {'id':           'pgv_sg_mootools.js',
                           'expression':   "python: here.meta_type in ['ATFolder','ATTopic']"},                           
                           {'id':           'pgv_sg_jd.gallery.js',
                           'expression':   "python: here.meta_type in ['ATFolder','ATTopic']"},                           
#                           {'id':           'pgv_sg_slightbox.js',                           
#                           'expression':   "python: here.meta_type in ['ATFolder','ATTopic']"},                       
                        )
                        
EXTERNAL_METHODS        = None


GALLERYVIEWS = ('pgv_sg_simpletimed_view',
                'pgv_sg_carouseltimed_view',
                'pgv_sg_carousel_view',                    
                'pgv_sg_simpletimed_big_view',
                'pgv_sg_carouseltimed_big_view',
                'pgv_sg_carousel_big_view',)