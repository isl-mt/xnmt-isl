Recipes: Noisy Input Sequences
==============================
This adds noise to the training data of an MT system in order to make it robust against ASR errors.
Sperber et al.: Toward Robust Neural Machine Translation for Noisy Input Sequences (IWSLT 2017).

This can be done as a preprocessing step by calling the following script on the source-side training texts:

    xnmt --dynet-gpu ./recipe.yaml

Results can be found in the paper.
