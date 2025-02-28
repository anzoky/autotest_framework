
class SortablePageLocators:

    TAB_LIST = ('xpath', '//a[@id="demo-tab-list"]')
    LIST_ITEM = ('xpath', '//div[@id="demo-tabpane-list"] //div[@class="list-group-item list-group-item-action"]')
    TAB_GRID = ('xpath', '//a[@id="demo-tab-grid"]')
    GRID_ITEM = ('xpath', '//div[@id="demo-tabpane-grid"] //div[@class="list-group-item list-group-item-action"]')


class SelectablePageLocators:

    TAB_LIST = ('xpath', '//a[@id="demo-tab-list"]')
    LIST_ITEM = ('xpath', '//li[@class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = ('xpath', '//ul[@id="verticalListContainer"] '
                                 '//li[@class="mt-2 list-group-item active list-group-item-action"]')
    TAB_GRID = ('xpath', '//a[@id="demo-tab-grid"]')
    GRID_ITEM = ('xpath', '//li[@class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = ('xpath', '//div[@id="demo-tabpane-grid"] '
                                 '//li[@class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:

    CONSTRAINT_AREA = ('xpath', '//div[@class="constraint-area"]')
    RESIZABLE_BOX_HANDLE = ('xpath', '//div[@id="resizableBoxWithRestriction"]'
                                     ' //span[@class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE_BOX = ('xpath', '//div[@id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = ('xpath', '//div[@id="resizable"]'
                                 ' //span[@class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = ('xpath', '//div[@id="resizable"]')


class DroppablePageLocators:

    # Simple
    SIMPLE_TAB = ('xpath', '//a[@id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = ('xpath', '//div[@id="draggable"]')
    DROP_HERE_SIMPLE = ('css selector', 'div[class="simple-drop-container"] #droppable')

    # Accept
    ACCEPT_TAB = ('xpath', '//a[@id="droppableExample-tab-accept"]')
    ACCEPTABLE = ('xpath', '//div[@id="acceptable"]')
    NOT_ACCEPTABLE = ('xpath', '//div[@id="notAcceptable"]')
    DROP_HERE_ACCEPT = ('css selector', 'div[class="accept-drop-container"] #droppable')

    # Prevent Propagation
    PREVENT_TAB = ('xpath', '//a[@id="droppableExample-tab-preventPropogation"]')
    NOT_GREEDY_DROP_BOX_TEXT = ('css selector', 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY_INNER_BOX = ('xpath', '//div[@id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = ('css selector', 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY_INNER_BOX = ('xpath', '//div[@id="greedyDropBoxInner"]')
    DRAG_ME_PREVENT = ('xpath', '//div[@id="dragBox"]')

    # Revert Draggable
    REVERT_TAB = ('xpath', '//a[@id="droppableExample-tab-revertable"]')
    WILL_REVERT = ('xpath', '//div[@id="revertable"]')
    NOT_REVERT = ('xpath', '//div[@id="notRevertable"]')
    DROP_HERE_REVERT = ('css selector', 'div[class="revertable-drop-container"] #droppable')