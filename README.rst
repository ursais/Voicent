======================
Voicent Python Library
======================

.. |badge1| image:: https://img.shields.io/badge/Maturity-Stable-green.png
    :target: https://pypi.org/classifiers/
    :alt: Production/Stable
.. |badge2| image:: https://img.shields.io/badge/Licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/Github-Voicent-lightgray.png?logo=github
    :target: https://github.com/ursais/Voicent
    :alt: ursais/Voicent

|badge1| |badge2| |badge3|

The Voicent Python Simple Interface class contains the following functions:

.. code-block:: python

    callText
    callAudio
    callStatus
    callRemove
    callTillConfirm
    importCampaign
    runCampaign
    importAndRunCampaign
    checkStatus
    exportResult

These functions are used to invoke telephone calls from your Python program.
For example, callText is used to call a specified number and automatically play
your text message using text-to-speech engine.

In order for this class to work, you’ll need to have Voicent Gateway installed
somewhere in your network. This class simply sends HTTP request for telephone
calls to the gateway. Voicent has a free edition for the gateway.
You can download it from http://www.voicent.com.

More information can be found at: http://www.voicent.com/devnet/docs/pyapi.htm


**Table of contents**

.. contents::
   :local:

Installation
============

Install from PyPi using pip, a package manager for Python.

 pip install voicent-python

Don't have pip installed? Try installing it, by running this from the command line:

 $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

Or, you can download the source code (ZIP) for voicent, and then run:

 python setup.py install

You may need to run the above commands with sudo.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/ursais/Voicent/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/ursais/Voicent/issues/new?body=Voicent%0Aversion:%202.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
=======

Authors
~~~~~~~

* Voicent
* Open Source Integrators

Contributors
~~~~~~~~~~~~

* Voicent
* Maxime Chambreuil <mchambreuil@opensourceintegrators.com>

Maintainers
~~~~~~~~~~~

This module is maintained by Open Source Integrators.

.. image:: https://github.com/ursais.png
   :alt: Open Source Integrators
   :target: https://www.opensourceintegrators.com

Open Source Integrators™ (OSI) provides customers a unique combination of
open source business process consulting and implementations.

.. |maintainer-max3903| image:: https://github.com/max3903.png?size=40px
    :target: https://github.com/max3903
    :alt: max3903

Current maintainer:

|maintainer-max3903|

You are welcome to contribute. Please create an issue on Github to discuss how.