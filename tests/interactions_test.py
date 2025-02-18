from conftest import driver
from pages.interactions_page import SortablePage


class TestInteractions:

    class TestSortablePage:

        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            assert list_before != list_after, 'The order of list has not been changed'

        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert grid_before != grid_after, 'The order of list has not been changed'

