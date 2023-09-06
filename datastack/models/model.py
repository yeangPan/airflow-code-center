#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    : model.py
@Time    : 2023/09/06 23:23:30
@Author  : yangp
@Contact : yangp@wanyantech.com
@Version : 0.1
@License : Apache License Version 2.0, 2023 yangp
@Desc    : None
'''

from __future__ import annotations


from pydantic import BaseModel,Field


class Project(BaseModel):
    id: int = Field(..., title="项目id")
    url: str = Field(..., title="项目url")
    branch: str = Field(..., title="项目分支")
    name: str = Field(..., title="项目名称")
    submit: str = Field(..., title="项目提交id")
    mtype: str = Field(..., title="项目类型，基础数据/特征/因子及衍生因子等")
    status: str = Field(..., title="项目状态")
    onsubmit: str = Field(..., title="项目提交时间")





