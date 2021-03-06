"""Tests for ``celery upgrade`` command."""

import pytest

from celery.bin.celery import upgrade
from celery.five import WhateverIO


class test_upgrade:
    """Test upgrade command class."""

    def test_run(self):
        out = WhateverIO()
        a = upgrade(app=self.app, stdout=out)

        with pytest.raises(a.UsageError, match=r'missing upgrade type'):
            a.run()

        with pytest.raises(a.UsageError, match=r'missing settings filename'):
            a.run('settings')
