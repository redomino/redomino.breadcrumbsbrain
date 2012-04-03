redomino.breadcrumbsbrain
=========================

redomino.breadcrumbsbrain is a new plugin for Plone CMS that will make it much easier
to search for specific objects in a Plone-based portal or intranet by showing the 
breadcrumbs paths along with Titles and Descriptions in the search results.

We all know that common users do not provide objects with proper titles and descriptions 
(sometimes they just do not provide them at all), which makes it hard to figure out 
if what you found is actually what you were looking for. Then you open every link in
the search results to find it out, which may take you quite a time. What you actually need 
in a situation like this is CONTEXT.

And context is what you get!
redomino.breadcrumbsbrain displays the breadcrumbs of each object in the search results,
helping you in figuring out what those objects are about: are they from 2010 or 2011?
are they in the 'Notices' archive or in the 'News' archive? and so on.


BE CAREFUL!
This is not a standalone package. If you want you can call the breadcrumbs_renderer
view provided by this package (for example you can insert this code into the
search.pt template)::

    <tal:block tal:replace="structure result/@@breadcrumbs_renderer|nothing" />

This way you will be able to display where your search results items are placed.

Many thanks to AUSL Bologna.

Technical details
-----------------

- redomino.breadcrumbsbrain.interfaces.IBrain
  This is a marker interface applied to all brains

- @@breadcrumbs_view
  This is a browser view with a method named breadcrumbs.
  Once called it will return the breadcrumbs info for a 
  particular brain. No getObject is needed, just a
  catalog call for each brain.
  Note well: if you want to use this browser view intensively you should
  STRONGLY consider to add a cache policy (it is not provided by default).

  Data format returned::

      [
       {'Title': 'News'),
        'absolute_url': 'http://localhost:8080/Plone/news'
       },
       {'Title': '2011'),
        'absolute_url': 'http://localhost:8080/Plone/news/2011'
       },
      ]

- @@breadcrumbs_renderer
  This is a browser view that let you show the breadcrumbs info
  of a particular brain.

  Data format displayed::

      News -> 2011

Authors
-------

- Davide Moro <davide.moro AT redomino.com>

