import csv
import numpy as np
from sklearn import metrics


def read_pred(predFile):
    with open(predFile, 'r') as csvFile:
        reader = csv.reader(csvFile)
        pred = []
        for row in reader:
            data = row[0].split(',')
            pred.append(float(data[0]))
    return np.array(pred)


def read_gt(gtFile):
    with open(gtFile, 'r') as csvFile:
        reader = csv.reader(csvFile)
        gt = []
        for row in reader:
            data = row[0].split(',')
            gt.append(int(data[0])+1)
    return np.array(gt)


def cal_auc(gt, pred):
    fpr, tpr, thresholds = metrics.roc_curve(gt, pred, pos_label=2)
    return metrics.auc(fpr, tpr)


def final_eval(track_1_predFile=None, track_2_predFile=None):
    track_1_gtFile = '/path/to/series_test_gt.csv'
    track_2_gtFile = '/path/to/movie_test_gt.csv'

    # track_1: series
    if track_1_predFile:
        track_1_gt = read_gt(track_1_gtFile)
        track_1_pred = read_pred(track_1_predFile)
        print('Track_1_series: {} records.'.format(len(track_1_gt)))
        assert len(track_1_pred) == len(track_1_gt), 'Error, track 1 prediction samples: %s'%(len(track_1_pred))
        track_1_auc = cal_auc(track_1_gt, track_1_pred)
    else:
        track_1_auc = None
    
    # track_2: movies
    if track_2_predFile:
        track_2_gt = read_gt(track_2_gtFile)
        track_2_pred = read_pred(track_2_predFile)
        print('Track_2_movie: {} records.'.format(len(track_2_gt)))
        assert len(track_2_pred) == len(track_2_gt), 'Error, track 2 prediction samples: %s'%(len(track_2_pred))
        track_2_auc = cal_auc(track_2_gt, track_2_pred)
    else:
        track_2_auc = None
    
    # display the evaluation results
    print('') 
    print('Track_1_series AUC: {:.6}'.format(track_1_auc))
    print('Track_2_movies AUC: {:.6}'.format(track_2_auc))
    
    

track1_series_predFile = '/path/to/series_test_prediction.csv'
track2_movies_predFile = '/path/to/movie_test_prediction.csv'

final_eval(track1_series_predFile, track2_movies_predFile)
