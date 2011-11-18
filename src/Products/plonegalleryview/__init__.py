from Globals import package_home
from Products.Archetypes.public import process_types, listTypes
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory

from config import SKINS_DIR, GLOBALS, PROJECTNAME

# Register skin directories so they can be added to portal_skins
registerDirectory('skins', GLOBALS)
registerDirectory('skins/plonegalleryview', GLOBALS)





