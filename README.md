# Content-based Video Relevance Prediction Challenge
### @ICME 2019, Shanghai, China
![](hulu_logo.png)

**(This challenge is fully sponsored by Hulu.)**

## Motivation

Video relevance computation is one of the most important tasks for personalized online streaming service. Given the relevance of videos and viewer feedbacks, the system can provide personalized recommendations, which will help the viewer discover more content of interest. In most online service, the computation of video relevance table is based on the viewers' implicit feedback, e.g. watch and search history. The system analyzes the viewer-to-video preference and computes the video-to-video relevance scores using collaborative filtering based methods. However, this kind of method performs poorly for “cold-start” problem - when a new video is added to the library, the recommendation system needs to bootstrap the video relevance score with very little historical viewer feedbacks. One promising approach to solve the “cold-start” problem of new item is analyzing video content itself to predict the relevance score, i.e. predicting the video-to-video relevance by analyzing the keyframes, audio, subtitles and metadata. With the relevance score, we can provide better recommendations for our viewers. 

## Background

We have held CBVRP challenge during the last two years (ICIP2017 and ACM Multimedia 2018). More than 160 participants registered, and 10 teams submitted the result and 5 paper submission in the CBVRP challenge 2018, (https://github.com/cbvrp-acmmm-2018/cbvrp-acmmm-2018). A big advancement on this task has been made by the winner teams.

## Task and Data

The main task of this challenge is to solve the “cold-start” problem of new item. According to the viewer behavior history and the video content, the participants need to predict the viewer click-through behavior on new TV series or new movies. The viewer feedbacks have been cleaned to avoid any privacy issues. Instead of delivering original video content, audio and visual features are extracted from the video and delivered as the representation of the video content. Specifically, there are two separated tracks for TV series and movies respectively.

For each track, the data is composed of two parts. One part is viewer records, i.e. a data sample is a viewer record. For example, a record “*Movie<sub>1</sub> , Movie<sub>2</sub> , ... , Movie<sub>N</sub>  ->  Movie<sub>N+1</sub>*” means a viewer has watched *N* movies in a time sequence and then we recommend *Movie<sub>N+1</sub>* to the viewer. If the viewer clicked *Movie<sub>N+1</sub>*, we consider this record as a positive sample, otherwise it is a negative sample. The other part is visual and audio features extracted from the TV series/movie trailers. The visual feature includes both frame-level feature and clip-level feature. All the features are extracted using pre-trained CNN models. For each track, there are respectively a training set, a validation set and a test set. In the test set, we will give a bunch of viewer records. The participants need to calculate a probability score indicating how much probably the viewer will click the TV series/movie we recommend. The training set and validation set will be released to participants after registration. The details of the dataset are given as follows.

#### Track 1: TV series

Pre-extracted features derived from nearly 3,570 TV-series video trailers. The whole set is divided into 3 subsets: training set, validation set, and testing set.

|           |  TV series |   Records   |
| --------- |:---------: |:-----------:|
|   Train   |   2,839    |  5,221,221  |
|   Val     |    357     |   931,820   |
|   Test    |    374     |   794,120   |


#### Track 2: Movies

Pre-extracted features derived from over 9,574 movie video trailers. The whole set is divided into 3 subsets: training set, validation set, and testing set.

|           |   Movie   |   Records   |
| --------- |:---------:|:-----------:|
|   Train   |   7,303   |  1,123,786  |
|   Val     |   1,254   |   552,577   |
|   Test    |   1,017   |   822,343   |


## Evaluation

AUC (Area Under Curve) will be used as evaluation metric. An example of evaluation will be given.

## Registration

The registration will be open on Dec 15, 2018.

## Submission

After the test data is released, participants can submit the results **twice a week**. 

The participants should send the results to cbvrp-icme-2019@hulu.com. After receiving the submission, we will evaluate the results and send the feedback to the participants by email.

## Schedule

|        Date       |                  Event               |
| ----------------- |:------------------------------------:|
|   Dec 15, 2018    | Registration open                    |
|   Jan 1, 2019     | Release train and validation data    | 
|   Feb 18, 2019    | Release test data                    |
|   Mar 15, 2019    | Deadline for result submission       |
|   Apr 1, 2019     | Notification of winners              |
|   Apr 8, 2019     | Deadline for paper submission        |
|   Apr 22, 2019    | Notification of paper acceptance     |
|   Apr 29, 2019    | Deadline for camera-ready papers     |

## Prizes

The total reward is $2,000 USD for each track including the taxable amount, which will be fully sponsored by Hulu LLC. The number of winners will depend on the number of participants and the quality of the results. The organizers reserve the complete right in the final judgement and decision.

The winners of the challenge are required to provide a technique report describing the details of the winning algorithms, and to give a presentation during the conference.

## Organizers

Peng Wang (peng.wang@hulu.com) Hulu LLC.\
Yan Bai (ryann.bai@hulu.com) Hulu LLC.\
Chunxu Xu (chunxu.xu@hulu.com) Hulu LLC.\
Saboya Yang (saboya.yang@hulu.com) Hulu LLC.\
Wei Feng (wei.feng@hulu.com) Hulu LLC.\
Xiaohui Xie (xiaohui.xie@hulu.com) Hulu LLC.

## Contact

If you have any question, please send email to cbvrp-icme-2019@hulu.com.
