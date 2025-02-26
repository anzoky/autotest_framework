from conftest import driver
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


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

    class TestSelectablePage:

        def test_selectable_list(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active_elem, inactive_elem = selectable_page.select_list_item()
            assert active_elem not in inactive_elem, 'Element was not selected'
            assert active_elem, 'Active element is empty or None'

        def test_selectable_grid(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active_elem, inactive_elem = selectable_page.select_grid_item()
            assert active_elem not in inactive_elem, 'TElement was not selected'
            assert active_elem, 'Active element is empty or None'

    class TestResizablePage:

        def test_resizable_box(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            assert ('500px', '300px') == max_box, 'Maximum size not equal to 500px, 300px'
            assert ('150px', '150px') == min_box, 'Minimum size not equal to 150px, 150px'

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_size, min_size = resizable_page.change_size_resizable()
            assert min_size != max_size, 'Resizable has not been changed'
