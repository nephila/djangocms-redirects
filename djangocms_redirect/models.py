## -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib.sites.models import Site
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


RESPONSE_CODES = (
    ('301', '301'),
    ('302', '302',),
)

@python_2_unicode_compatible
class Redirect(models.Model):
    site = models.ForeignKey(Site, models.CASCADE, verbose_name=_('site'))
    old_path = models.CharField(_('redirect from'), max_length=200, db_index=True,
        help_text=_("This should be an absolute path, excluding the domain name. Example: '/events/search/'."))
    new_path = models.CharField(_('redirect to'), max_length=200, blank=True,
        help_text=_("This can be either an absolute path (as above) or a full URL starting with 'http://'."))
    response_code = models.CharField(_('response code'), max_length=3, choices=RESPONSE_CODES, default=RESPONSE_CODES[0][0],
        help_text=_("This is the http response code returned if a destination is specified. If no destination is specified the response code will be 410."))

    class Meta:
        verbose_name = _('redirect')
        verbose_name_plural = _('redirects')
        db_table = 'django_redirect'
        unique_together = (('site', 'old_path'),)
        ordering = ('old_path',)

    def __str__(self):
        return "%s ---> %s" % (self.old_path, self.new_path)
