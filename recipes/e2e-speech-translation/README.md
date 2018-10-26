Recipes: End-to-End Speech Translation
======================================
Recipes for several models that perform end-to-end speech translation.

- Direct single-task model: A single encoder-decoder model, does not yield good results but is included as a baseline:
  - 68
- Multi-task direct model: A direct encoder-decoder model trained in a multi-task fashion, yields good results when enough data is available:
  - 39
- Two-stage model: A two-stage end-to-end model, needed to pretrained to following, stronger model:
  - 4
- Improved two-stage model: A two-stage end-to-end model with improvements that address error propagation issues, yields strongest results both when lots of data is available and is also okay with training on less end-to-end data (e.g. >30k sentences):
  - 34

