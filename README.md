[ISL] eXtensible Neural Machine Translation
===========================================

This is a repository for various speech translation models developed at [Interactive Systems Labs](http://isl.anthropomatik.kit.edu/) and based on the `xnmt` toolkit.
It is coded in Python based on [DyNet](http://github.com/clab/dynet).

Installation and Usage
----------------------

Requires Python 3.6.

Before running *xnmt*, install the required packages, including [DyNet](<http://github.com/clab/dynet>),
by running ``pip install -r requirements.txt``.

Next, install *xnmt* by running ``python setup.py develop``.

Available command line interfaces:

* ``xnmt`` runs experiments from a configuration file::

    xnmt --dynet-gpu my-training.yaml

* ``xnmt_decode`` performs inference::

    xnmt_decode --src src.txt --hyp out.txt --mod saved-model.mod

* ``xnmt_evaluate`` computes evaluation metrics::

    xnmt_evaluate --hyp out.txt --ref ref.txt --metric bleu


Example and Recipes
-------------------

* The [examples/](examples/README.md) subfolder contains basic example configurations.
* The [recipes/](recipes/README.md) subfolder contains full-size model trainings on common benchmark data.
* Unit tests can be run from the main directory: ``python -m unittest``

More information can be found in the [documentation](http://xnmt.readthedocs.io).
