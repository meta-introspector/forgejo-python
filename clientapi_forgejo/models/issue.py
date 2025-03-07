# coding: utf-8

"""
    Forgejo API.

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 1.20.5+0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
from datetime import date, datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from clientapi_forgejo.models.attachment import Attachment
from clientapi_forgejo.models.label import Label
from clientapi_forgejo.models.milestone import Milestone
from clientapi_forgejo.models.pull_request_meta import PullRequestMeta
from clientapi_forgejo.models.repository_meta import RepositoryMeta
from clientapi_forgejo.models.user import User

class Issue(BaseModel):
    """
    Issue represents an issue in a repository  # noqa: E501
    """
    assets: Optional[conlist(Attachment)] = None
    assignee: Optional[User] = None
    assignees: Optional[conlist(User)] = None
    body: Optional[StrictStr] = None
    closed_at: Optional[datetime] = None
    comments: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    due_date: Optional[datetime] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    is_locked: Optional[StrictBool] = None
    labels: Optional[conlist(Label)] = None
    milestone: Optional[Milestone] = None
    number: Optional[StrictInt] = None
    original_author: Optional[StrictStr] = None
    original_author_id: Optional[StrictInt] = None
    pin_order: Optional[StrictInt] = None
    pull_request: Optional[PullRequestMeta] = None
    ref: Optional[StrictStr] = None
    repository: Optional[RepositoryMeta] = None
    state: Optional[StrictStr] = Field(None, description="StateType issue state type")
    title: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    user: Optional[User] = None
    __properties = ["assets", "assignee", "assignees", "body", "closed_at", "comments", "created_at", "due_date", "html_url", "id", "is_locked", "labels", "milestone", "number", "original_author", "original_author_id", "pin_order", "pull_request", "ref", "repository", "state", "title", "updated_at", "url", "user"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict(),default=json_serial)

    @classmethod
    def from_json(cls, json_str: str) -> Issue:
        """Create an instance of Issue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in assets (list)
        _items = []
        if self.assets:
            for _item in self.assets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assets'] = _items
        # override the default output from pydantic by calling `to_dict()` of assignee
        if self.assignee:
            _dict['assignee'] = self.assignee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in assignees (list)
        _items = []
        if self.assignees:
            for _item in self.assignees:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assignees'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item in self.labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['labels'] = _items
        # override the default output from pydantic by calling `to_dict()` of milestone
        if self.milestone:
            _dict['milestone'] = self.milestone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pull_request
        if self.pull_request:
            _dict['pull_request'] = self.pull_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Issue:
        """Create an instance of Issue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Issue.parse_obj(obj)

        _obj = Issue.parse_obj({
            "assets": [Attachment.from_dict(_item) for _item in obj.get("assets")] if obj.get("assets") is not None else None,
            "assignee": User.from_dict(obj.get("assignee")) if obj.get("assignee") is not None else None,
            "assignees": [User.from_dict(_item) for _item in obj.get("assignees")] if obj.get("assignees") is not None else None,
            "body": obj.get("body"),
            "closed_at": obj.get("closed_at"),
            "comments": obj.get("comments"),
            "created_at": obj.get("created_at"),
            "due_date": obj.get("due_date"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "is_locked": obj.get("is_locked"),
            "labels": [Label.from_dict(_item) for _item in obj.get("labels")] if obj.get("labels") is not None else None,
            "milestone": Milestone.from_dict(obj.get("milestone")) if obj.get("milestone") is not None else None,
            "number": obj.get("number"),
            "original_author": obj.get("original_author"),
            "original_author_id": obj.get("original_author_id"),
            "pin_order": obj.get("pin_order"),
            "pull_request": PullRequestMeta.from_dict(obj.get("pull_request")) if obj.get("pull_request") is not None else None,
            "ref": obj.get("ref"),
            "repository": RepositoryMeta.from_dict(obj.get("repository")) if obj.get("repository") is not None else None,
            "state": obj.get("state"),
            "title": obj.get("title"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "user": User.from_dict(obj.get("user")) if obj.get("user") is not None else None
        })
        return _obj


