from robot.api import logger
from robot.api.deco import keyword

class GitOperations:
    @keyword
    def test_git_keyword(self):
        logger.console("✅ Git keyword executed!")
