# The Face of Populism

Python code repository for the paper: "The Face of Populism: Examining Differences in Facial Emotional Expressions of Political Leaders Using Machine Learning"

ArXiv Preprint: :eyes:

---

Contents:

1. Emotion detection notebook `notebook/`
2. CVSs with processed data  `data-clean`
3. Analysis scripts `scripts/`
4. Analysis results `results/`
5. Figures `figures/`

`output` folder in this repository is empty, but after running the notebook it should contain folders with annotated images of each processed frame and each processed video. Figure 1 in the paper is made from two such frames.

## Notebook: `notebook/emotion_detection.ipynb`

Notebook has been tested on Google Colab and GH Codespaces environments. A separate repository will be created, adjusted for cloning the Codespace and running the notebook will be created. This will be the most simple, free option to run the notebook and process YT videos even on low-end machines without graphic card.

Right now notebook is cumbersome, with lot of dependencies. In the future, we will try to simplify the process with minimal dependencies and without the need to have a GPU on local machine.

## Analysis scripts: `scripts/`

Run order:

1. `scripts/analyze-emotions.py` (caution: this script has a manual review step in the middle, see commented code for details)
2. `scripts/results-t300.py` Main analysis script. Produces Table 1 and Figures 2-4.
3. `scripts/results-f50.py` Supplementary analysis script. Produces Table 2 and Figures 5-7.
4. `scripts/dominant-emotion.py` Supplementary analysis script. Produces Table 3.
5. `scripts/misc.py` Calculates total length of all videos and mean number of frames. This doesn't count two videos which have been removed from YouTube since the time we first ran the analysis.




