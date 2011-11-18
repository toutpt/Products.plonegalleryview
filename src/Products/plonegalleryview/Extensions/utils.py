from Globals import package_home
from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.CMFCore.utils import getToolByName
import os, string



def registerStylesheets(self, out, stylesheets):
    # register additional CSS stylesheets with portal_css
    csstool = getToolByName(self, 'portal_css')
    for css in stylesheets:
        csstool.registerStylesheet(**css)
    print >> out, "installed the Plone additional stylesheets."


def registerScripts(self, out, scripts):
    # register additional JS Scripts with portal_javascripts
    jstool = getToolByName(self, 'portal_javascripts')
    for js in scripts:
        jstool.registerScript(**js)
    print >> out, "installed the Plone additional javascripts."

def registerExternalMethods(self, out, ext_methods):
    """ register external methods """
    if ext_methods is not None:
        installedIDs    = []            # list of installed ext. method IDs
        for extMethod in ext_methods:
            try:
                if not hasattr(self, extMethod['id']):
                    self.manage_addProduct['ExternalMethod'].manage_addExternalMethod(**extMethod)
                    installedIDs.append(extMethod['function'])
                else:
                    out.write('Ext. method "' + extMethod['id'] + '" already exists \n')

            except:
                raise AssertionError('the external method called "' + extMethod['id'] + '" was not found.')

    if len(installedIDs):
        out.write(str(len(installedIDs)) + ' External Methods registered \n')

#----------------------------

