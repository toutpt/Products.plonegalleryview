from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes, install_subskin
from Products.plonegalleryview.Extensions.utils import *
from Products.plonegalleryview.config import *
from Products.CMFPlone.migrations.migration_util import safeEditProperty
from StringIO import StringIO





def plonegalleryview_properties(self, out):
    # install Plone Gallery View global properties
    plonegalleryview_properties = (
        ('pgv_sg_delay', 'string', '7000'),
        ('pgv_sg_fadeDuration', 'string', '700'),
        ('pgv_sg_thumbIdleOpacity', 'string', '0.6'),
        ('pgv_sg_textShowCarousel', 'string', 'show carousel'),
        ('pgv_sg_embedLinks', 'boolean', 'true'),                    
    )
 
    plonegalleryview_old_properties = ('delay', 'fadeDuration','textShowCarousel')
    
    
    if not hasattr(self.portal_properties, 'plonegalleryview_properties'):
        self.portal_properties.addPropertySheet(
            'plonegalleryview_properties', 'Plone Gallery View properties')
        print >> out, "add propertysheet for plonegalleryview."

    props = self.portal_properties.plonegalleryview_properties
    
    for oldProp in plonegalleryview_old_properties:
        if props.hasProperty(oldProp):
            props.manage_delProperties((oldProp,))
                
           
    props = self.portal_properties.plonegalleryview_properties
    for prop, tp, val in plonegalleryview_properties:
        if not props.hasProperty(prop):
            props._setProperty(prop, val, tp)
    print >> out, "Successfully installed Plone Gallery View properties."



def install(self):
    out = StringIO()

    installTypes(self, out, listTypes(PROJECTNAME), PROJECTNAME)
    install_subskin(self, out, GLOBALS)
    registerStylesheets(self, out, STYLESHEETS)
    registerScripts(self, out, JAVASCRIPTS)
    plonegalleryview_properties(self,out)

    propsTool = getToolByName(self, 'portal_properties')
    siteProperties = getattr(propsTool, 'site_properties')
    navtreeProperties = getattr(propsTool, 'navtree_properties')

    # add the gallery views to folder/large folder and topics
    typesTool = getToolByName(self, 'portal_types')

    # for folder
    typefolder = typesTool['Folder']
    viewlist = typefolder.getProperty('view_methods', d=None)
    for galleryview in GALLERYVIEWS:
      if galleryview not in viewlist:
        viewlist = viewlist + (galleryview,)
    typefolder.manage_changeProperties(view_methods = viewlist)

    
    # for topics
    typetopic = typesTool['Topic']
    viewlist = typetopic.getProperty('view_methods', d=None)
    for galleryview in GALLERYVIEWS:
      if galleryview not in viewlist:
        viewlist = viewlist + (galleryview,)
    typetopic.manage_changeProperties(view_methods = viewlist)
    print >>out, "Successfully added gallery views: %s" % ', '.join(GALLERYVIEWS)
    
    out.write("Successfully installed %s. :-)" % PROJECTNAME)

    return out.getvalue()




    
    
def uninstall(self):
    out = StringIO()

    # remove the gallery views from folder and topics
    typesTool = getToolByName(self, 'portal_types')


    # for folder
    newviewlist = ()    
    typefolder = typesTool['Folder']
    viewlist = typefolder.getProperty('view_methods', d=None)
    for viewitem in viewlist:  
      if viewitem not in GALLERYVIEWS:
        newviewlist = newviewlist + (viewitem,)
    typefolder.manage_changeProperties(view_methods = newviewlist)

    # for topics
    newviewlist = ()    
    typetopic = typesTool['Topic']
    viewlist = typetopic.getProperty('view_methods', d=None)
    for viewitem in viewlist:   
      if viewitem not in GALLERYVIEWS:
        newviewlist = newviewlist + (viewitem,)
    typetopic.manage_changeProperties(view_methods = newviewlist)
    
    
    print >>out, "Successfully remove gallery views: %s" % ', '.join(GALLERYVIEWS)
    print >>out, "We leave plonegalleryview_properties there, please remove it manualy!"
    
    out.write("Successfully uninstalled %s. bye bye  ;-)" % PROJECTNAME)

    return out.getvalue()

