import random
import time

import allure

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):

    locators = SortablePageLocators()

    @allure.step('Get items from Sortable')
    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    @allure.step('Change list order')
    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        return order_before, order_after

    @allure.step('Change grid order')
    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):

    locators = SelectablePageLocators()

    @allure.step('Click random item on Selectable')
    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    @allure.step('Select list item and get active and inactive element')
    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        inactive_element = self.elements_are_present(self.locators.LIST_ITEM)
        return active_element.text, [item.text for item in inactive_element]

    @allure.step('Select grid item and get active and inactive element')
    def select_grid_item(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        inactive_element = self.elements_are_present(self.locators.GRID_ITEM)
        return active_element.text, [item.text for item in inactive_element]


class ResizablePage(BasePage):

    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step('Get size of element')
    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    @allure.step('Change size of resizable box')
    def change_size_resizable_box(self):
        self.element_is_visible(self.locators.CONSTRAINT_AREA)
        with allure.step('Resize box and get maximum size and minimum size'):
            self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE),
                                                400, 200)
            max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
            self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE),
                                                -400, -200)
            min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step('Change size of resizable')
    def change_size_resizable(self):
        self.element_is_visible(self.locators.RESIZABLE)
        with allure.step('Resize box and get maximum size and minimum size'):
            self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE),
                                                random.randint(1, 300), random.randint(1, 300))
            max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
            self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE),
                                                random.randint(-200, -1), random.randint(-200, -1))
            min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):

    locators = DroppablePageLocators()

    @allure.step('Drop simple draggable element')
    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        with allure.step('Drag element to the box'):
            self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    @allure.step('Drop acceptable or not acceptable elements')
    def drop_acceptable(self, element):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        accept = {'acceptable': self.element_is_visible(self.locators.ACCEPTABLE),
                  'not_acceptable': self.element_is_visible(self.locators.NOT_ACCEPTABLE)}
        with allure.step('Drag element to the box'):
            self.action_drag_and_drop_to_element(accept[element], drop_div)
        with allure.step('Get text from the box'):
            drop_text_accept = drop_div.text
        return drop_text_accept

    @allure.step('Drop draggable element in prevent propagation page')
    def drop_prevent_propagation(self, inner_element, outer_element):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)

        inner_boxes = {'not_greedy_inner': self.element_is_present(self.locators.NOT_GREEDY_INNER_BOX),
                       'greedy_inner': self.element_is_present(self.locators.GREEDY_INNER_BOX)}

        outer_boxes = {'not_greedy_outer': self.element_is_present(self.locators.NOT_GREEDY_DROP_BOX_TEXT),
                       'greedy_outer': self.element_is_present(self.locators.GREEDY_DROP_BOX_TEXT)}
        time.sleep(1)
        with allure.step('Drag element to the box'):
            self.action_drag_and_drop_to_element(drag_div, inner_boxes[inner_element])
        with allure.step('Get text from the outer box'):
            text_box = outer_boxes[outer_element].text
        with allure.step('Get text from the inner box'):
            inner_text_box = inner_boxes[inner_element].text
        return text_box, inner_text_box

    @allure.step('Drop revert or not revert draggable elements')
    def drop_revert_draggable(self, element):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        reverts = {'will_revert': self.element_is_visible(self.locators.WILL_REVERT),
                  'not_revert': self.element_is_visible(self.locators.NOT_REVERT)}
        with allure.step('Drag element to the box'):
            self.action_drag_and_drop_to_element(reverts[element], drop_div)
        position_after_move = reverts[element].get_attribute('style')
        time.sleep(1)
        position_after_revert = reverts[element].get_attribute('style')
        return position_after_move, position_after_revert