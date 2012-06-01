domain=redomino.breadcrumbsbrain
/opt/buildout.python/python-2.6/bin/i18ndude rebuild-pot --pot $domain.pot --create $domain ../
/opt/buildout.python/python-2.6/bin/i18ndude sync --pot $domain.pot */LC_MESSAGES/$domain.po
