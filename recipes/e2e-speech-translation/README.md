Recipes: End-to-End Speech Translation
======================================
Recipes for several models that perform end-to-end speech translation.

1. Direct single-task model: A single-task encoder-decoder model, does not yield good results but is included as a baseline:
   - ``xnmt --dynet-gpu ./recipe1-direct-singletask.yaml``
2. Multi-task direct model: A direct encoder-decoder model trained in a multi-task fashion, yields good results when enough end-to-end data is available:
   - ``xnmt --dynet-gpu ./recipe2-direct-multitask.yaml``
3. Two-stage model: A two-stage end-to-end model, useful as a baseline and to pretrain the improved two-stage model (4):
   - ``xnmt --dynet-gpu ./recipe3-twostage-basic.yaml``
4. Improved two-stage model: A two-stage end-to-end model with improvements that address error propagation issues, yields strongest results both when lots of end-to-end data is available and works well when trained on less end-to-end data (around >30k end-to-end sentences are needed for good results):
   - ``xnmt --dynet-gpu ./recipe4-twostage-improved.yaml``

