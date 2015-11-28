====================
 git-release-tagger
====================
-----------------------------------------------
 by `Swing Development <http://swingdev.io/>`_
-----------------------------------------------

.. image:: https://img.shields.io/pypi/v/git-release-tagger.svg
    :target: https://pypi.python.org/pypi/git-release-tagger

.. image:: https://img.shields.io/pypi/dm/git-release-tagger.svg
        :target: https://pypi.python.org/pypi/git-release-tagger


Small CLI utility to enable the CI environment to communicate the deployment progress through the use of git tags.

Installation
=============

.. code-block:: bash

    $ pip install git-release-tagger

Usage
=============

.. code-block:: bash

  $ tag-release [-h] [-t TRIGGER] [-v] [-m MESSAGE]
                 prefix {pending,deploying,failed,success}

Prefix is self explanatory.

If the release was triggered by a tag (like '*release*') - use the **--trigger** option to have the tagger remove it automatically.
This enables the user to retry a failed deployment just by tagging the same commit again.

Use **-m** to add a message to the commit. For example - a link to the build status on Jenkins / TeamCity / other CI.

Examples
=============

.. code-block:: bash

  $ tag-release production pending

will remove tags:
 - 'production_pending',
 - 'production_deploying',
 - 'production_failed',
 - 'production_success'

will add tags:
 - 'production_pending'


.. code-block:: bash

  $ tag-release production success

will remove tags:
 - 'production_pending',
 - 'production_deploying',
 - 'production_failed',
 - 'production_success'

will add tags:
 - 'production_success'
 - 'production_success_2015-11-02_16_34_26'


.. code-block:: bash

  $ tag-release -t production production success

will remove tags:
 - 'production'
 - 'production_pending',
 - 'production_deploying',
 - 'production_failed',
 - 'production_success'

will add tags:
 - 'production_success'
 - 'production_success_2015-11-02_16_34_26'
