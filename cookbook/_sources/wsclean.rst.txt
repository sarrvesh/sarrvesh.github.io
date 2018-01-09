The WSClean Imager [#f1]_
==========================

WSClean is a command-line imager that is tailered for wide-field imaging. It supports several deconvolution methods, including multi-scale and multi-frequency deconvolution and an "RM-synthesis"-deconvolution mode. It also supports correcting images for the LOFAR beam.

To use WSClean on one of the CEP clusters, first include the WSClean environment::

   module load Wsclean

A list of command line options can be acquired by running **wsclean** without parameters::

   $ wsclean
   WSClean version 2.4 (2017-05-28)
   This software package is released under the GPL version 3.
   ...

An extensive manual for WSClean is available on-line, at `wsclean homepage <https://sourceforge.net/p/wsclean/wiki/Home/>`_. It includes a chapter about LOFAR beam correction. WSClean has also been described in the following article: `http://arxiv.org/abs/1407.1943 <http://arxiv.org/abs/1407.1943>`_.

.. rubric:: Footnotes

.. [#f1] The author of this chapter is `Andre Offringa <mailto:offringa@astron.nl>`_.
