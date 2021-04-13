import os
import gettext
from Components.Language import language

PLUGIN_NAME = "QuadPiP"
PLUGIN_VERSION = "1.2"	# python 3
PLUGIN_PATH = os.path.dirname( __file__ )

def localeInit():
	os.environ["LANGUAGE"] = language.getLanguage()[:2]
	gettext.bindtextdomain(PLUGIN_NAME, "%s/locale"%(PLUGIN_PATH))

def _(txt):
	t = gettext.dgettext(PLUGIN_NAME, txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t

localeInit()
language.addCallback(localeInit)
