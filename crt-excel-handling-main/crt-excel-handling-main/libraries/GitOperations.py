# File: GitOperations.py

import os
import git
from robot.api import logger
from robot.api.deco import keyword


class GitOperations:
    
    def __init__(self):
        self._project_path = os.getcwd()
        self._data_path = os.path.join(self._project_path, "data")
        logger.console(f"[INIT] Project Path: {self._project_path}")
        logger.console(f"[INIT] Data Path: {self._data_path}")

    @keyword("Commit And Push")
    def commit_and_push(self, file_name, git_branch):
        path_to_file = os.path.join(self._data_path, file_name)
        logger.console(f"[INFO] File to commit: {path_to_file}")

        repo = git.Repo(self._project_path)

        logger.console(f"[GIT STATUS BEFORE]\n{repo.git.status()}")
        
        repo.index.add([path_to_file])
        repo.index.commit(f"Robot Framework: Updated {file_name}")
        repo.git.push("origin", git_branch)

        logger.console("[SUCCESS] Commit and push completed.")
