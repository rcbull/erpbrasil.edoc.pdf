========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/erpbrasil.edoc2.pdf/badge/?style=flat
    :target: https://readthedocs.org/projects/erpbrasiledocpdf
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/erpbrasil/erpbrasil.edoc2.pdf.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/erpbrasil/erpbrasil.edoc2.pdf

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/erpbrasil/erpbrasil.edoc2.pdf?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/erpbrasil/erpbrasil.edoc2.pdf

.. |requires| image:: https://requires.io/github/erpbrasil/erpbrasil.edoc2.pdf/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/erpbrasil/erpbrasil.edoc2.pdf/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/erpbrasil/erpbrasil.edoc2.pdf/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/erpbrasil/erpbrasil.edoc2.pdf

.. |codecov| image:: https://codecov.io/github/erpbrasil/erpbrasil.edoc2.pdf/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/erpbrasil/erpbrasil.edoc2.pdf

.. |version| image:: https://img.shields.io/pypi/v/erpbrasil.edoc2.pdf.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/erpbrasil.edoc2.pdf

.. |wheel| image:: https://img.shields.io/pypi/wheel/erpbrasil.edoc2.pdf.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/erpbrasil.edoc2.pdf

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/erpbrasil.edoc2.pdf.svg
    :alt: Supported versions
    :target: https://pypi.org/project/erpbrasil.edoc2.pdf

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/erpbrasil.edoc2.pdf.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/erpbrasil.edoc2.pdf

.. |commits-since| image:: https://img.shields.io/github/commits-since/erpbrasil/erpbrasil.edoc2.pdf/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/erpbrasil/erpbrasil.edoc2.pdf/compare/v0.0.0...master



.. end-badges

Impressão de documentos fiscais a partir do XML: NF-E, NFC-E, CT-E, MDF-E, GNRE e etc.

* Free software: MIT license

Installation
============

::

    pip install erpbrasil.edoc2.pdf

You can also install the in-development version with::

    pip install https://github.com/erpbrasil/erpbrasil.edoc2.pdf/archive/master.zip


Documentation
=============


https://erpbrasiledocpdf.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
