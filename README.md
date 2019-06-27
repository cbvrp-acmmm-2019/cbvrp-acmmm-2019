# Content-based Video Relevance Prediction Challenge
### @ACM Multimedia 2019, Nice, France
![](hulu_logo.png)

**(This challenge is fully sponsored by Hulu.)**

## Motivation

Video relevance computation is one of the most important tasks for personalized online streaming service. Given the relevance of videos and viewer feedbacks, the system can provide personalized recommendations, which will help the viewer discover more content of interest. In most online service, the computation of video relevance table is based on the viewers' implicit feedback, e.g. watch and search history. The system analyzes the viewer-to-video preference and computes the video-to-video relevance scores using collaborative filtering based methods. However, this kind of method performs poorly for “cold-start” problem - when a new video is added to the library, the recommendation system needs to bootstrap the video relevance score with very little historical viewer feedbacks. One promising approach to solve the “cold-start” problem of new items is analyzing video content itself to predict the relevance score, i.e. predicting the video-to-video relevance by analyzing the metadata of video such as keyframes, audio, subtitles. With the relevance score, we can provide better recommendations for our viewers. 

## Background

Hulu LLC. have held CBVRP challenge during the last two years (ICIP 2017 and ACM Multimedia 2018). More than 160 participants registered, 10 teams submitted the result and 5 papers were recieved in the CBVRP challenge 2018, (https://github.com/cbvrp-acmmm-2018/cbvrp-acmmm-2018). A big advancement on this task has been made by the winner teams.

In order to support sustained and substantial progress in the state of the art on video recommendation, CBVRP challenge is continuously held in ACM Multimedia 2019 with the release of more diverse and more abundant data.  

## Task and Data

The main task of this challenge is to solve the “cold-start” problem of new items. According to the viewer behavior history and the video content, participants need to predict the viewer click-through behavior on new TV series or new movies. The viewer feedbacks have been cleaned to avoid any privacy issues. Instead of delivering original video content, audio and visual features are extracted from the video and are delivered as the representation of the video content. Specifically, there are two separate tracks for TV series and movies respectively.

For each track, the data is composed of two parts, viewer records and metadata of video content. As for viewer records, a data sample is a viewer record. For example, a record “*Movie<sub>1</sub> , Movie<sub>2</sub> , ... , Movie<sub>N</sub>  ->  Movie<sub>N+1</sub>*” means a viewer has watched *N* movies in a time sequence and then we recommend *Movie<sub>N+1</sub>* to the viewer. If the viewer clicked *Movie<sub>N+1</sub>*, we consider this record as a positive sample, otherwise it is a negative sample. Besides, visual and audio features extracted from TV series/movie trailers are offered. The visual feature includes both frame-level feature and clip-level feature. All the features are extracted using pre-trained CNN models. For each track, there are respectively a training set, a validation set and a test set. In the test set, we will give a bunch of viewer records. Participants need to calculate a probability score indicating how much probably the viewer will click the TV series/movie we recommend. The training set and validation set will be released to participants after registration. The details of the dataset are given as follows.

#### Track 1: TV series

Pre-extracted features are derived from nearly 3,570 TV-series video trailers. The whole set is divided into 3 subsets: training set, validation set, and testing set.

|           |  TV series |   Records   |
| --------- |:---------: |:-----------:|
|   Train   |   2,652    |  5,221,221  |
|   Val     |    347     |   931,820   |
|   Test    |    571     |   794,120   |


#### Track 2: Movies

Pre-extracted features are derived from over 9,574 movie video trailers. The whole set is divided into 3 subsets: training set, validation set, and testing set.

|           |   Movie   |   Records   |
| --------- |:---------:|:-----------:|
|   Train   |   6,173   |  1,123,786  |
|   Val     |   1,273   |   552,577   |
|   Test    |   2,128   |   822,343   |


## Evaluation

AUC (Area Under Curve) will be used as evaluation metric. See the example of [evaluation code](./evaluation_code.py)

## Registration

To register for the challenge and get access to the dataset, please complete the [Online Agreement Form](https://freeonlinesurveys.com/s/DjOillyA). We will send you the download instructions by email after the challenge data available date (Apr. 1, 2019).

## Submission

After the test data is released, participants can submit the results **twice a week**. Each time the participants need to submit two `csv` files:

- "series_test_prediction.csv", which should have 794,120 lines. Each line is the probability score for the record in the corresponding line of "series_test.csv". 

- "movie_test_prediction.csv", which should have 822,343 lines. Each line is the probability score for the record in the corresponding line of "movie_test.csv".

Example of series_test_prediction.csv / movie_test_prediction.csv: 
  > 0.123456  
  > 0.234567  
  > 0.876543  
  > ...

The participants should send the results to cbvrp-acmmm-2019@hulu.com. After receiving the submission, we will evaluate the results and send the feedback to the participants by email.

## Leaderboard

#### Track 1: TV Series

| Team      | AUC       |
| --------- |:---------:|
| potato | 0.650996 |
| ZJGSU | 0.599168 |
| GrandRookie | 0.586481 |
| USTC_I_Know_U | 0.565589 |
| Distinc | 0.531248 |
| UESTC_cfm | 0.529325 |
| Oases | 0.524569 |
| MIDAS@CBVRP | 0.518106 |
| MAGUS.Embedding is Power | 0.500000 |

#### Track 2: Movies

| Team      | AUC       |
| --------- |:---------:|
| MAGUS.Embedding is Power | 0.652002 |
| GrandRookie | 0.604653 |
| ZJGSU | 0.602680 |
| USTC_I_Know_U | 0.601199 |
| potato | 0.593027 |
| UESTC_cfm | 0.585820 |
| Oases | 0.583843 |
| Distinc | 0.566727 |
| MIDAS@CBVRP | 0.533669 |

## Schedule

|        Date       |                  Event                  |
| ----------------- |:---------------------------------------:|
|   Mar. 15, 2019   | Registration open                       |
|   Apr. 1, 2019    | Release training and validation data    | 
|   Jun. 1, 2019    | Release test data                       |
|   Jul. 1, 2019    | Deadline for final result submission    |
|   Jul. 8, 2019    | Deadline for paper submission           |

The registration is open until Jul. 1, 2019 (the deadline for final result submission).

## Prizes

The total reward is $2,000 USD for each track including the taxable amount, which will be fully sponsored by Hulu LLC. The number of winners will depend on the number of participants and the quality of the results. The organizers reserve the complete right in the final judgement and decision.

## Organizers

Peng Wang (peng.wang@hulu.com) Hulu LLC.\
Yan Bai (ryann.bai@hulu.com) Hulu LLC.\
Chunxu Xu (chunxu.xu@hulu.com) Hulu LLC.\
Yunsheng Jiang (yunsheng.jiang@hulu.com) Hulu LLC.\
Wei Feng (wei.feng@hulu.com) Hulu LLC.\
Xiaohui Xie (xiaohui.xie@hulu.com) Hulu LLC.

## Contact

If you have any question, please send an email to cbvrp-acmmm-2019@hulu.com.
