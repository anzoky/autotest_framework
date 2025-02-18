
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