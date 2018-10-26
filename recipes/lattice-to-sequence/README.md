Recipes: Lattice-to-Sequence Speech Translation Model
=====================================================
This trains a Spanish-to-English speech translation model using the LatticeLSTM encoder as described here:
Sperber et al.: Neural Lattice-to-Sequence Models for Uncertain Inputs (EMNLP 2017).

Training is performed on Spanish-to-English Fisher data.

How to run

    # Train model
    xnmt --dynet-gpu ./recipe.yaml

Results can be found in the paper.
