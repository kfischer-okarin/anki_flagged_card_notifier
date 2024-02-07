from anki.collection import SearchNode
from aqt import mw, gui_hooks, dialogs
from aqt.utils import showInfo
from aqt.qt import *


ANY_FLAG_SEARCH_STRING = '-flag:0'
ANY_FLAG_SEARCH_NODE = SearchNode(flag=SearchNode.Flag.FLAG_ANY)


closing = False


def notify_about_flagged_cards() -> None:
    global closing
    flagged_cards = mw.col.find_cards(ANY_FLAG_SEARCH_STRING)
    if len(flagged_cards) > 0 and not closing:
        showInfo('You have flagged cards')
        dialogs.open("Browser", mw, search=[ANY_FLAG_SEARCH_NODE])


def set_closing() -> None:
    global closing
    closing = True


gui_hooks.sync_did_finish.append(notify_about_flagged_cards)
gui_hooks.profile_will_close.append(set_closing)
