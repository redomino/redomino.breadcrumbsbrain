redomino.breadcrumbsbrain
=========================

A useful set of browser views that let you add breadcrumbs to catalog brains.

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

