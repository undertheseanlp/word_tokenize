# -*- coding: utf-8 -*-
from pipelines.model_evaluation.analysis_error import error_analysis
from pipelines.model_evaluation.get_score import get_score


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
    if OPTIONS["Error Analysis"]:
        error_analysis()
