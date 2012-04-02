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


import unittest

#from zope.testing import doctestunit
#from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()

import redomino.breadcrumbsbrain


class TestCase(ptc.PloneTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            ztc.installPackage(redomino.breadcrumbsbrain)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='redomino.breadcrumbsbrain',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='redomino.breadcrumbsbrain.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        #ztc.ZopeDocFileSuite(
        #    'README.txt', package='redomino.breadcrumbsbrain',
        #    test_class=TestCase),

        #ztc.FunctionalDocFileSuite(
        #    'browser.txt', package='redomino.breadcrumbsbrain',
        #    test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
