import os
from robot.api import logger
from robot.api.deco import keyword
import git

class GitOperations:
    def __init__(self):
        # Fallback safely if SCRIPTS isn't set
        self._project_name = os.environ.get("SCRIPTS", "")
        self._project_path = os.getcwd()

        # Adjust path if needed (avoid hardcoded paths unless necessary)
        if self._project_name and "suite" not in self._project_path:
            self._project_path = os.path.join(self._project_path, self._project_name)

        logger.console(f"Project Path: {self._project_path}")
        self._data_path = os.path.join(self._project_path, "data")
        logger.console(f"Data Path: {self._data_path}")

    @keyword(name="Commit And Push")
    def commit_and_push(self, file_name, git_branch):
        try:
            path_to_file = os.path.join(self._data_path, file_name)
            my_repo = git.Repo(self._project_path)

            logger.console("\n" + my_repo.git.status() + "\n")

            my_repo.index.add([path_to_file])
            my_repo.index.commit(f"Robot committing changes to {file_name}")
            my_repo.git.push("origin", git_branch)

            logger.console("✅ Git push successful.")
        except Exception as e:
            logger.console(f"❌ Git push failed: {str(e)}")
            raise
