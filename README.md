# The Face of Populism

Python code repository for the paper: "The Face of Populism: Examining Differences in Facial Emotional Expressions of Political Leaders Using Machine Learning"

ArXiv Preprint: [https://arxiv.org/abs/2304.09914](https://arxiv.org/abs/2304.09914)

![image](https://user-images.githubusercontent.com/39856297/233164118-1531efa5-2b61-40d5-a6dd-98dce713c7f3.png)

## Overview

This repository contains code and data for analyzing facial emotional expressions of political leaders using machine learning techniques. The analysis compares populist and pluralist leaders to identify significant differences in their emotional expressions during public appearances.

## Contents

1. Emotion detection notebook: `notebook/`
2. CSVs with processed data: `data-clean/`
3. Analysis scripts: `scripts/`
4. Analysis results: `results/`
5. Figures: `figures/`
6. Raw data: `data-raw/`
   - `yt-urls.csv`: YouTube URLs for all analyzed videos
   - `gps.csv`: Global Party Survey data with populism scores

The repository uses a structured organization where raw data is processed through the pipeline, with intermediate and final results stored in appropriate directories.

The `output` folder in this repository is empty by default, but after running the notebook it will contain folders with annotated images of each processed frame and each processed video. Figure 1 in the paper is made from two such frames.
## Statistical Approach

The statistical analysis in this project follows these key steps:

1. **Video-level aggregation**: For each video, we calculate:
   - Mean scores for each of the 7 emotion categories
   - A composite "negative" emotion score (sum of anger, disgust, fear, and sadness)

2. **Classification by political characteristics**:
   - Populism scores from the Global Party Survey (1-4 scale)
   - Binary classification: Pluralist (scores 1-2) vs. Populist (scores 3-4)
   - Additional variables: country, party size, ideology

3. **Hypothesis testing**: We test whether populist leaders display:
   - Higher levels of negative emotions
   - Lower levels of neutral expressions

4. **Statistical methods**:
   - Independent samples t-tests (for binary comparisons)
   - ANOVA with post-hoc Tukey HSD (for multi-category comparisons)
   - Effect size measurements (Cohen's d, Eta-squared)
   - Visualizations to examine distributions and potential outliers
## Implementation Details

The emotion detection pipeline uses the following implementation approach:

1. **Video Download**: Videos are downloaded from YouTube using the `pytube` library
2. **Video Preprocessing**:
   - For videos requiring cropping, the `moviepy` library is used to create subclips
   - A temporary directory (`temp/`) stores videos during processing
3. **Frame Extraction and Analysis**:
   - OpenCV (`cv2`) is used to extract video metadata (fps, frame count, duration)
   - The `fer` library handles face detection (MTCNN) and emotion recognition
   - Annotated frames are saved as images and zipped for later review
4. **Output Organization**:
   - CSV files with emotion scores are saved to `data-clean/` directory
   - Annotated images are saved to `output/` directory
   - File naming convention: `[video_index]-[method_code].csv` (e.g., `0-t300.csv`)

## Technical Pipeline

### Video Processing

We use two approaches to extract frames from the videos:

1. **Main approach (t300)**: Extract 300 frames uniformly distributed over the length of each video
   - Implementation calculates optimal frame frequency based on total video frames
   - Formula: `frame_frequency = floor(total_frames/300)`

2. **Alternative approach (f50)**: Extract every 50th frame from each video (approximately one frame every 1.67-2.00 seconds)
   - Fixed sampling rate regardless of video length

### Face Detection

The face detection pipeline consists of the following steps:

1. **Face Detection**: We use the Multi-task Cascaded Convolutional Networks (MTCNN) approach implemented in the `fer` Python library. This framework uses three-stage cascaded CNNs for simultaneous face detection and alignment.
   - Parameters:
     - Scale factor: 0.709
     - Minimum face size: 40 pixels
     - Thresholds: [0.6, 0.7, 0.7] for the three stages

2. **Manual Verification**: For videos with multiple detected faces, we manually verify which face corresponds to the political leader of interest.
   - The `analyze-emotions.py` script marks videos with multiple faces (when a second face appears in >5% of frames)
   - During manual review, videos where consistent face detection isn't possible are discarded
   - For some videos, we specify frame ranges to use only portions with consistent face detection

### Emotion Detection

After face detection, we apply emotion recognition using the mini-Xception CNN architecture:

1. **Model Architecture**: mini-Xception CNN implementation from the `fer` library
   - 4 residual depth-wise separable convolutions
   - Input shape: 64x64 pixels (grayscale)
   - Output: 7 emotion scores (anger, disgust, fear, happiness, sadness, surprise, neutral)
   - Implementation: `detector = FER(mtcnn=True)` initializes the detector with MTCNN enabled

2. **Model Training**: The model was pre-trained on the FER2013 dataset
   - 30,000 48x48 pixel grayscale images of facial expressions
   - Benchmark accuracy: 66% (comparable to human accuracy of 65±5%)

3. **Processing Pipeline**:
   - Videos are processed one at a time to manage memory usage
   - For each video, temporary files are created and cleaned between processing steps
   - The `Video` class from the `fer` library handles frame extraction and emotion detection
   - Multiple faces are preserved in the output (`first_face_only = False`) for manual verification later

3. **Output Processing**:
   - Each frame produces 7 scores that sum to 1 (compositional data)
   - We aggregate negative emotions (anger, disgust, fear, sadness) to minimize false positive issues

4. **Validation**:
   - Human annotation study with 5 coders reviewing 514 randomly selected frames
   - Inter-coder agreement: Fleiss' Kappa of 0.231 (fair agreement)
   - Machine-human agreement: 55.2% (Cohen's Kappa of 0.311, F1 score of 0.502)

## Data Analysis

Our statistical analysis includes:

1. **Data Preprocessing**:
   - Calculation of mean scores for each emotion category per video
   - Aggregation of negative emotions (anger, disgust, fear, sadness) into a composite score
   - Handling of missing data and removing videos with inadequate face detection
   - Classification of leaders as populist (Party Populism scores 3-4) or pluralist (Party Populism scores 1-2)

2. **Descriptive Statistics**:
   - Summary statistics (mean, standard deviation, min/max) for each emotion category
   - Distribution analysis using visualization techniques (swarm plots, raincloud plots)
   - Country-level comparisons of emotional expressions

3. **Statistical Testing**:
   - Independent samples t-tests for comparing populist vs. pluralist leaders
   - ANOVA tests to examine differences across populism score categories (1-4)
   - Post-hoc Tukey HSD tests for multiple comparisons
   - Effect size calculations (Cohen's d for t-tests, Eta-squared for ANOVA)

4. **Alternative Analyses**:
   - Comparison of results between two sampling methods (t300 and f50)
   - Analysis of dominant emotions (which emotion has the highest score in each frame)
   - Examination of ideological differences (left-right, liberal-conservative)
   - Country-specific case studies

## Notebook: `notebook/emotion_detection.ipynb`

The emotion detection notebook has been tested on Google Colab and GitHub Codespaces environments. It contains the code for processing YouTube videos, detecting faces, and recognizing emotions.

Requirements:
- Python 3.6+
- GPU with CUDA support (the notebook validates GPU availability)
- fer library (with MTCNN enabled)
- OpenCV (cv2)
- TensorFlow
- pytube (for YouTube video downloading)
- moviepy (for video editing)
- imageio==2.4.1 (specific version requirement)
- matplotlib, numpy, pandas (for data processing and visualization)

## Analysis Scripts: `scripts/`

Run order:

1. `scripts/analyze-emotions.py`: Processes the raw emotion data from videos
   - **Important**: This script includes a manual review step for face detection verification
   - Input: CSVs with raw emotion scores for each frame
   - Output: Marked CSV files for manual review and final results CSV
   - Key functions:
     - `mark_multiple_faces()`: Identifies videos with multiple faces (>5% of frames)
     - `fix_object()`: Handles data type conversion and missing values
     - `create_results_df()`: Aggregates emotion data and merges with political metadata
   - The script includes lists for excluded videos (`trash`) and videos requiring specific frame ranges (`cut_vids`, `cut_from`, `cut_to`)
   - A separate analysis is performed for each sampling method (t300 and f50)

2. `scripts/results-t300.py`: Main analysis script
   - Produces Table 1 and Figures 2-4
   - Analyzes data from the 300 uniformly sampled frames approach
   - Statistical analyses:
     - Descriptive statistics for all emotion categories
     - T-tests comparing pluralists vs. populists
     - Effect size calculations (Cohen's d)
     - ANOVA with post-hoc Tukey HSD tests
     - Eta-squared calculations for effect size
   - Visualization:
     - Swarm plots for group comparisons
     - RainCloud plots showing distributions by populism score
     - Country-level comparisons

3. `scripts/results-f50.py`: Supplementary analysis script
   - Produces Table 2 and Figures 5-7
   - Analyzes data from the every-50th-frame approach
   - Structure and analyses mirror those in `results-t300.py`
   - Serves as a robustness check for the main analysis

4. `scripts/dominant-emotion.py`: Supplementary analysis script
   - Produces Table 3
   - Analyzes which emotions are dominant in different leader groups
   - For each frame, identifies the emotion with the highest score
   - Calculates the proportion of frames where each emotion is dominant
   - Compares distributions between populist and pluralist leaders

5. `scripts/ideology.py`: Additional analysis script
   - Examines the relationship between political ideology and emotional expressions
   - Creates variables for left-right (`left`) and liberal-conservative (`lib`) distinctions
   - Performs t-tests and calculates effect sizes for ideological comparisons
   - Provides a comparison point for the populism-based analysis

6. `scripts/japan.py`: Country-specific analysis
   - Focuses on Japanese political leaders from three parties (LDP, NKP, CDP)
   - Calculates mean emotion scores for each party
   - Performs a detailed case study of emotional expressions in Japanese politics

7. `scripts/misc.py`: Utility script
   - Calculates total length of all videos using the `pytube` library
   - Computes the mean number of frames across all videos
   - Note: This doesn't count videos removed from YouTube since the initial analysis

## Replicating the Analysis

To fully replicate our analysis:

1. Start with the emotion detection notebook (`notebook/emotion_detection.ipynb`) to process YouTube videos:
   - Ensure you have GPU access (the notebook checks for this with `tf.test.gpu_device_name()`)
   - The notebook will download videos from YouTube using the URLs in `data-raw/yt-urls.csv`
   - Two processing methods are implemented:
     - Main method: 300 uniformly distributed frames per video
     - Alternative method: Every 50th frame from each video
   - Output is saved to `data-clean/` (CSV) and `output/` (images) directories

2. Run the analysis scripts in the order listed above
3. For the manual review step in `analyze-emotions.py`:
   - Review the `yt-urls-mark-*.csv` files
   - Replace '999' values with the face number representing the selected leader
   - Mark unusable videos in the 'trash' list in the script
   - For videos needing specific frame ranges, update the 'cut_vids', 'cut_from', and 'cut_to' arrays
