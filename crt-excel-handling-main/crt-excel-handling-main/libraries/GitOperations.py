import os
from robot.api import logger
from robot.api.deco import keyword
import git

class GitOperations:
    def __init__(self):
        self._project_name = str(os.environ.get("SCRIPTS"))
        self._project_path = os.getcwd()

        # Adjust project path based on environment
        if self._project_name != "None":
            if self._project_path == "/home/services/suite/tests":
                self._project_path = "/home/services/suite/"
            else:
                self._project_path = os.path.join(os.getcwd(), self._project_name)

        logger.console(f"Project path: {self._project_path}")
        self._data_path = os.path.join(self._project_path, "data/")
        logger.console(f"Data path: {self._data_path}")

    @keyword
    def commit_and_push(self, file_name, git_branch):
        """
        Adds the specified file to Git, commits the change, and pushes to the given branch.
        """
        path_to_file = os.path.join(self._data_path, file_name)

        try:
            my_repo = git.Repo(self._project_path)
        except git.exc.InvalidGitRepositoryError:
            logger.console("Invalid Git repository at path: " + self._project_path)
            raise

        logger.console("\n" + my_repo.git.status() + "\n")

        try:
            my_repo.index.add([path_to_file])
            my_repo.index.commit(f"CRT robot committing changes to {file_name}")
            my_repo.git.push("origin", git_branch)
            logger.console(f"Successfully pushed {file_name} to {git_branch}")
        except Exception as e:
            logger.console(f"Git operation failed: {e}")
            raise
