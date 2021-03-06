[ISL] Recipes
=============

This contains several recipes that allow training and testing various real-sized models with a few simple commands.

Basic recipes:
- [kftt](kftt/): An English-Japanese text-to-text translation model.
- [standford-iwslt](standford-iwslt/): A small-data Vietnamese-English text-to-text translation model.
- [las-tedlium](las-tedlium/): An LSTM-based attentional ASR on English TEDLIUM data.

Advanced recipes:
- [self-att-acoustic-models](self-att-acoustic-models/): English ASR using self-attentional acoustic models, trained on TEDLIUM.
- [lattice-to-sequence](lattice-to-sequence/): Lattice-to-Sequence model on Spanish-English Fisher data, using the LatticeLSTM as encoder
- [noisy-inputs](noisy-inputs/): Add noise to textual MT training data to improve robustness against ASR errors.
- [e2e-speech-translation](e2e-speech-translation/): End-to-end models for speech translation that directly produce translations from audio inputs. 