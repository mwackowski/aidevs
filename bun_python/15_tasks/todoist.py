import requests
import os
import asyncio
from typing import List

from todoist_dt import ITask, ITaskClose, ITaskModify


def apiCall(endpoint="/me", method="GET", body={}):
    response = requests.request(
        method,
        f"https://api.todoist.com/rest/v2{endpoint}",
        headers={
            "Content-Type": "application/json",
            "Authorization": f'Bearer {os.environ["TODOIST_API_KEY"]}',
        },
        json=body if method == "POST" else None,
    )
    return True if response.status_code == 204 else response.json()


async def listUncompleted() -> List[ITask]:
    uncompleted = apiCall("/tasks", "GET")
    return [
        ITask(
            idx=task["id"],
            content=task["content"],
            due=task["due"]["string"] if task["due"] else None,
        )
        for task in uncompleted
    ]


async def addTasks(tasks: List[ITaskModify]) -> List[ITaskModify]:
    promises = [
        apiCall(
            "/tasks",
            "POST",
            {"content": task["content"], "due_string": task["due_string"]},
        )
        for task in tasks
    ]
    addedTasks = await asyncio.gather(*promises)
    return [
        ITaskModify(
            id=addedTask["id"],
            content=addedTask["content"],
            due_string=addedTask["due"]["string"] if addedTask["due"] else None,
        )
        for addedTask in addedTasks
    ]


async def updateTasks(tasks: ITaskModify):
    promises = [
        apiCall(
            f"/tasks/{task['id']}",
            "POST",
            {
                "content": task["content"],
                "due_string": task["due_string"],
                "is_completed": task["is_completed"],
            },
        )
        for task in tasks
    ]
    updatedTasks = await asyncio.gather(*promises)
    return [
        {
            "id": updatedTask["id"],
            "content": updatedTask["content"],
            "due_string": updatedTask["due"]["string"] if updatedTask["due"] else None,
        }
        for updatedTask in updatedTasks
    ]


async def closeTasks(tasks: ITaskClose):
    promises = [apiCall(f"/tasks/{id}/close", "POST") for id in tasks]
    try:
        await asyncio.gather(*promises)
        return [{str(closedTask): "completed"} for closedTask in tasks]
    except Exception as e:
        return "No tasks were closed (maybe they were already closed)"
