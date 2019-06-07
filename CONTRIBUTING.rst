============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

Bug reports
===========

When `reporting a bug <https://datadriver.myjetbrains.com/youtrack/issues>`_ please include:

    * Your operating system name and version.
    * Any details about your local setup that might be helpful in troubleshooting.
    * Detailed steps to reproduce the bug.

Documentation improvements
==========================

bdacore could always use more documentation, whether as part of the
official bdacore docs, in docstrings, or even on the web in blog posts,
articles, and such.

Feature requests and feedback
=============================

The best way to send feedback is to file an issue at `<https://datadriver.myjetbrains.com/youtrack/issues.>`_

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that code contributions are welcome :)

Development
===========

To set up ``bdacore`` for local development:

#. Clone your fork locally::

    git clone git@gitlab.octo.com:dd/bdacore.git

#. Create a conda environment that contains the required package to run bdacore code and tests::

    make develop_env

   You may want to override the default package name (bdacore) and Python version (3.6). This can be done by overriding the *ENV_NAME* and *ENV_PY_VERSION* as follows::

    make develop_env ENV_NAME=bdacore_py2 ENV_PY_VERSION=2.7

#. Create a branch for local development::

    git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.


#. When you are done developping your feature and adding corresponding tests, make sure you did not break previous tests::

    make test-all

   A good practice is to create two environments, one in python 2.7 and one in python 3.6. This way you can locally check that tests run for both versions.

#. Commit your changes and push your branch to GitLab::

    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature

   Make sure the `CI builds for your branch <http://ec2-52-212-162-0.eu-west-1.compute.amazonaws.com:8080/job/bdacore/>`_ run successfully until the end.

#. Submit a pull request through the GitLab website.

#. If your PR is accepted, then follow the next steps::

    git checkout master
    git pull --rebase
    git checkout name-of-your-bugfix-or-feature
    git rebase master

   You may have conflicts at this point. Solve them by fixing the relevant
   files, then::
   
    git add [list of fixed files]
    git rebase --continue

   Make sure steps 4 and 6 still run smoothly. Then::

    git push --force origin name-of-your-bugfix-or-feature

#. Now, check that the `build <http://ec2-52-212-162-0.eu-west-1.compute.amazonaws.com:8080/job/bdacore/>`_ still passes. If not, fix your code first. Then::

    git checkout master
    git rebase name-of-your-bugfix-or-feature
    git push origin master

#. The branch ``master`` is now up-to-date with your changes. You may delete your old branch::

    git branch -d name-of-your-bugfix-or-feature
    git push -d origin name-of-your-bugfix-or-feature


Pull Request Guidelines
-----------------------

If you need some code review or feedback while you're developing the code just make the pull request.

For merging, you should:

1. Make sure you did not break anything by running the tests (run steps 4 and 6 listed above)

2. Double-check your commit messages (see this `wonderful post <https://chris.beams.io/posts/git-commit/>`_)

3. Update documentation when there's new API, functionality etc.

4. Add a note to ``CHANGELOG.rst`` about the changes.

5. Add yourself to ``AUTHORS.rst``.
