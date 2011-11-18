# zope imports
from zope.interface import Interface
from zope.interface import implements
from zope.interface import alsoProvides, directlyProvides
from DateTime import DateTime
import string

# Five imports
from Products.Five.browser import BrowserView

# CMFCore imports
from Products.CMFCore.utils import getToolByName

        

class IPloneGalleryView(Interface):    
    """
    PloneGalleryView presents images in an slideshow gallery
    """
    def getPGVProperties(self):
        """
        Returns all PloneGalleryViewProperties from portal_properties
        """
    def genPGVSmoothGalleryJSCode(self):
        """
        Generate the SmoothGalleryJavaScriptCode with specific configuration
        """        



class PloneGalleryView(BrowserView):
    """
    """
    implements(IPloneGalleryView)



    def getPGVProperties(self):
        """
        """
        propSheet = getToolByName(self.context, "portal_properties")
        prop = 'plonegalleryview_properties'
        
        pgvProperties   = {}
        if hasattr(propSheet, prop):
            pgvProperties.update(dict(propSheet[prop].propertyItems()))
            
        return pgvProperties        



    def genPGVSmoothGalleryJSCode(self, **kw):
        """
        """
        
        JSCode="""
        <script type="text/javascript">
        	function startGallery() {
        		var myGallery = new gallery($('myGallery'), {
        			showArrows: %s,
        			showCarousel: %s,
        			showInfopane: %s,
        			timed: %s,
        			embedLinks: %s,
        			delay: %s,
        			thumbHeight: %i,
        			thumbWidth: %i,
        			thumbSpacing: %i,
        			fadeDuration: %s,
        			thumbIdleOpacity: %s,
        			textShowCarousel: %s
        		});
        		%s
        	}
        	window.onDomReady(startGallery);
        </script>
        """
        
        # get PloneGalleryProperties from portal_properties
        pgvProperties = self.context.getPGVProperties()
        
        if 'showArrows' in kw:
            showArrows = kw['showArrows']
        else:
            showArrows = 'true'

        if 'showCarousel' in kw:
            showCarousel = kw['showCarousel']
            startGallery = "myGallery.showCarousel();"
        else:
            startGallery = ""
            showCarousel = 'false'
                        

        if 'showInfopane' in kw:
            showInfopane = kw['showInfopane']
        else:
            showInfopane = 'true'     

        if 'timed' in kw:
            timed = kw['timed']
        else:
            timed = 'true'                             

        if 'embedLinks' in kw:
            embedLinks = kw['embedLinks']
        else:
            if pgvProperties.get('pgv_sg_embedLinks', True):
                embedLinks = 'true'
            else:
                embedLinks = 'false' 

        if 'delay' in kw:
            delay = kw['delay']
        else:
            delay = pgvProperties.get('pgv_sg_delay', 7000)     

        if 'fadeDuration' in kw:
            fadeDuration = kw['fadeDuration']
        else:
            fadeDuration = pgvProperties.get('pgv_sg_fadeDuration', 700)
 
        if 'thumbIdleOpacity' in kw:
            thumbIdleOpacity = kw['thumbIdleOpacity']
        else:
            thumbIdleOpacity = pgvProperties.get('pgv_sg_thumbIdleOpacity', 0.6)
            
        if 'textShowCarousel' in kw:
            textShowCarousel = "'" + kw['textShowCarousel'] + "'"
        else:
            textShowCarousel = "'" + pgvProperties.get('pgv_sg_textShowCarousel', "'show carousel'") + "'"  

        

        thumbHeight = 128 
        thumbWidth = 128
        thumbSpacing = 10
        
        JSCode = JSCode % (showArrows, showCarousel, showInfopane, timed, embedLinks, delay, thumbHeight, thumbWidth, thumbSpacing,fadeDuration, thumbIdleOpacity, textShowCarousel, startGallery)
        
        return JSCode       
        
