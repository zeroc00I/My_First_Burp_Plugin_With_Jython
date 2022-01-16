##
#
# It is my very first plugin attempt =)
# and doesn't do anything at all
# by @zeroc00I
##

from burp import IBurpExtender,ITab
from javax.swing import JScrollPane;

class BurpExtender(IBurpExtender, ITab):

    def	registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self.scrollpane = JScrollPane()
        callbacks.setExtensionName("Description Name")
        callbacks.customizeUiComponent(self.getUiComponent())
        callbacks.addSuiteTab(self)     
        return

    def getTabCaption(self):
        return 'Plugin Tab Name'

    def getUiComponent(self):
        return self.scrollpane
