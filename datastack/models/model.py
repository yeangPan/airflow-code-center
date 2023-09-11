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
    id: int = Field(..., title="id")
    url: str = Field(None, title="项目url")
    name: str = Field(None, title="项目名称")
    mtype: str = Field(None, title="项目类型，基础数据/特征/因子及衍生因子等")
    owner: str = Field(None, title='所有人')
    status: str = Field(None, title="项目状态")
    tags: str = Field(None, title="项目标签")
    comments: str = Field(None, title="项目说明")

class ProjectTimeRecord(BaseModel):
    id: int =  Field(..., title='id')
    pid: int = Field(None, title='项目id')
    developer: str = Field(None, title='开发人员')
    branch: str = Field(None, title='项目分支')
    commit: str = Field(None, title='项目提交id')
    onsubmit: str = Field(None, title='提交时间')
    fullpath: str = Field(None, title='项目路径')
    status: str = Field(None, title='项目状态')
    comments: str = Field(None, title='项目说明')


class Modular(BaseModel):
    id: int = Field(..., title='id')
    tid: int = Field(None, title='项目记录id')
    
    
 


