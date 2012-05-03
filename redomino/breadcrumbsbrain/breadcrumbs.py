# Copyright (c) 2010 Redomino srl (http://redomino.com)
# Authors: Davide Moro <davide.moro@redomino.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.

from Acquisition import aq_inner
from zope.interface import implements
from zope.component import getMultiAdapter

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.browser.interfaces import INavigationBreadcrumbs
from Products.CMFPlone.browser.navigation import get_view_url
from Products.CMFPlone.browser.navigation import utils

class BrainBreadcrumbs(BrowserView):
    """ This view let you get a breadcrumbs starting from a brain, no getObject
        is needed.
        As result it returns a list of dictionaries,

        The overhead is proportional to the batch site (number of elements for each page).
        You can reduce the batch size if needed or implement some memoized policy.
    """
    implements(INavigationBreadcrumbs)

    def breadcrumbs(self):

        context = aq_inner(self.context)
        request = self.request
        ct = getMultiAdapter((context, request), name=u'plone_tools').catalog()
        query = {}

        currentPath = context.getPath()

        query['path'] = {'query':currentPath, 'navtree':1, 'depth': 0}
        rawresult = ct(**query)
        dec_result = [(len(r.getPath()),r) for r in rawresult]
        dec_result.sort()

        portal_state = getMultiAdapter((context, request), name=u'plone_portal_state')
        rootPath = portal_state.navigation_root_path()

        # Build result dict
        result = []
        for r_tuple in dec_result:
            item = r_tuple[1]

            # Don't include it if it would be above the navigation root
            itemPath = item.getPath()
            if rootPath.startswith(itemPath):
                continue

            id, item_url = get_view_url(item)
            data = {'Title': utils.pretty_title_or_id(context, item),
                    'absolute_url': item_url}
            result.append(data)
        return result

class BrainBreadcrumbsRenderer(BrowserView):
    """
    Breadcrumbs renderer view
    """
    __call__ = ViewPageTemplateFile('templates/breadcrumbs_renderer.pt')

