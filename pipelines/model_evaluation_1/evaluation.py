# -*- coding: utf-8 -*-

from pipelines.model_evaluation.get_score import get_score
from analysis_error import error_analysis

def count_token(documents):
    count = 0
    for document in documents:
        for sentences in document.sentences:
            for word in sentences.split(' '):
                count += 1
    return count


if __name__ == '__main__':
    OPTIONS = {
        "F1_Score": True,
        "Confusion matrix": False,
        "Error Analysis": True,
        "Time Speed": False
    }
    if OPTIONS["F1_Score"]:
        get_score()
     # if OPTIONS["Confusion matrix"]:
    #     f = open(join(dirname(__file__), 'logs', 'crf', 'result.txt'), 'r+')
    #     confusion_matrix = confusion_matrix(actual_label, predict_label, labels=["BW", "IW", "O"])
    #     x = f.read().split('\n')
    #     x[6] = "BW\t" + str(confusion_matrix[0][0]) + "\t" + str(confusion_matrix[0][1]) + "\t\t" + str(
    #         confusion_matrix[0][2])
    #     x[7] = "IW\t" + str(confusion_matrix[1][0]) + "\t" + str(confusion_matrix[1][1]) + "\t" + str(
    #         confusion_matrix[1][2])
    #     x[8] = "O\t" + str(confusion_matrix[2][0]) + "\t\t" + str(confusion_matrix[2][1]) + "\t\t" + str(
    #         confusion_matrix[2][2])
    #     plt.figure()
    #     class_name = ["BW", "IW", "O"]
    #     Confution_Matrix.plot_confusion_matrix(confusion_matrix, classes=class_name, title='Confusion matrix')
    #     plt.savefig('confusion matrix.png')
    #     plt.show()
    #     x = x[:-1]
    #     f.close()
    if OPTIONS["Error Analysis"]:
        error_analysis()
    # if OPTIONS["Time Speed"]:
    #     f = open(join(dirname(__file__), 'logs', 'crf', 'result.txt'), 'r+')
    #     x = f.read().split("\n")
    #     time_stop = time.time()
    #     time_per_token = (time_stop - time_start) / float(count_token(actual_corpus.documents))
    #     time_per_token = 1.00 / time_per_token
    #     x[17] = "Time speed: %0.6f token per second" % time_per_token
    #     x = x[:-1]
    #     f.close()
