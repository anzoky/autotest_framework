import pytest

from conftest import driver
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


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

    class TestDroppablePage:

        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'The element has not been dropped'

        @pytest.mark.parametrize(
            'accept, expected_text', [
                ('acceptable', 'Dropped!'),
                ('not_acceptable', 'Drop here')
            ]
        )
        def test_accept(self, driver, accept, expected_text):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_acceptable(accept)
            assert text == expected_text, f'The expected result is {expected_text}, but not {text}'

        @pytest.mark.parametrize(
            'inner, outer, expected_text_inner, expected_text_outer', [
                ('not_greedy_inner', 'not_greedy_outer', 'Dropped!', 'Dropped!'),
                ('greedy_inner', 'greedy_outer', 'Dropped!', 'Outer droppable')
            ]
        )
        def test_prevent_propagation_droppable(self, driver, inner, outer, expected_text_inner, expected_text_outer):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            box_text, inner_box_text = droppable_page.drop_prevent_propagation(inner, outer)
            assert box_text == expected_text_outer, f'Expected outer box text: "{expected_text_outer}", but got: "{box_text}"'
            assert inner_box_text == expected_text_inner, f'Expected inner box text: "{expected_text_inner}", but got: "{inner_box_text}"'

        @pytest.mark.parametrize('param_name', ['will_revert', 'not_revert'])
        def test_revert_draggable_revert_droppable(self, driver, param_name):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            before_move, after_move = droppable_page.drop_revert_draggable(param_name)
            if param_name == 'will_revert':
                assert before_move != after_move, (
                    'The element has not reverted!'
                )
            else:
                assert before_move == after_move, (
                    'The element has reverted!'
                )