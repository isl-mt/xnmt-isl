Recipes: Noisy Input Sequences
==============================
This adds noise to the training data of an MT system in order to make it robust against ASR errors.
Sperber et al.: Toward Robust Neural Machine Translation for Noisy Input Sequences (IWSLT 2017).

This can be done as a preprocessing step by calling the following script on the source-side training texts:

    python script/custom/perturb_seq.py 0.05 examples/data/dev.en

This causes 5% of perturbation which is usually a safe value to use.

