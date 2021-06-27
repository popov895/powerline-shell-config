from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    HOME_SPECIAL_DISPLAY = False
    PATH_BG = 12
    CWD_FG = 16

    REPO_CLEAN_BG = 35
    REPO_CLEAN_FG = 16
    REPO_DIRTY_BG = 11
    REPO_DIRTY_FG = 16

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    CMD_FAILED_BG = 9
    CMD_FAILED_FG = 15
