#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-31 16:26:53
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: api_problem.py


from qa_models.models import Problem, ProblemTag


def list_problem_by_id(problem_ids=[], page_num=1, page_size=20):
    """
    """
    problem_query = Problem.objects
    if problem_ids:
        problem_obj_list = problem_query.filter(pk__in=problem_ids).all()
    else:
        problem_obj_list = problem_query.all()
    problem_list = [i.to_dict() for i in problem_obj_list]

    return problem_list

def list_problem_tag():
    """
    """
    tag_obj_list = ProblemTag.objects.all()
    tag_list = [
        {
            "id": i.id,
            "tag_name": i.tag_name,
        } for i in tag_obj_list
    ]

    return tag_list
