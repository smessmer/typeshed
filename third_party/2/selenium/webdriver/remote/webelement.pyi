from selenium.webdriver.remote.webdriver import WebDriver
from typing import Any, Optional, Dict, List

SizeDict = Dict[str, int]  # containing "height", "width"
PointDict = Dict[str, int]  # containing "x", "y"

class WebElement:
    def __init__(self, parent: WebDriver, id_: Optional[basestring], w3c: bool=False) -> None: ...
    @property
    def tag_name(self) -> basestring: ...
    @property
    def text(self) -> Optional[basestring]: ...
    def click(self) -> None: ...
    def submit(self) -> None: ...
    def clear(self) -> None: ...
    def get_attribute(self, name: basestring) -> Optional[basestring]: ...
    def is_selected(self) -> bool: ...
    def is_enabled(self) -> bool: ...

    def find_element_by_id(self, id_: basestring) -> WebElement: ...
    def find_elements_by_id(self, id_: basestring) -> List[WebElement]: ...
    def find_element_by_name(self, name: basestring) -> WebElement: ...
    def find_elements_by_name(self, name: basestring) -> List[WebElement]: ...
    def find_element_by_link_text(self, link_text: basestring) -> WebElement: ...
    def find_elements_by_link_text(self, link_text: basestring) -> List[WebElement]: ...
    def find_element_by_partial_link_text(self, link_text: basestring) -> WebElement: ...
    def find_elements_by_partial_link_text(self, link_text: basestring) -> List[WebElement]: ...
    def find_element_by_tag_name(self, name: basestring) -> WebElement: ...
    def find_elements_by_tag_name(self, name: basestring) -> List[WebElement]: ...
    def find_element_by_xpath(self, xpath: basestring) -> WebElement: ...
    def find_elements_by_xpath(self, xpath: basestring) -> List[WebElement]: ...
    def find_element_by_class_name(self, name: basestring) -> WebElement: ...
    def find_elements_by_class_name(self, name: basestring) -> List[WebElement]: ...
    def find_element_by_css_selector(self, css_selector: basestring) -> WebElement: ...
    def find_elements_by_css_selector(self, css_selector: basestring) -> List[WebElement]: ...

    def send_keys(self, *value: basestring) -> None: ...
    def is_displayed(self) -> bool: ...
    @property
    def location_once_scrolled_into_view(self): ...
    @property
    def size(self) -> SizeDict: ...
    def value_of_css_property(self, property_name): ...
    @property
    def location(self) -> PointDict: ...
    @property
    def rect(self): ...
    @property
    def screenshot_as_base64(self): ...
    @property
    def screenshot_as_png(self): ...
    def screenshot(self, filename: basestring): ...
    @property
    def parent(self) -> WebDriver: ...
    @property
    def id(self) -> Optional[basestring]: ...
    def __eq__(self, element: object) -> bool: ...
    def __ne__(self, element: object) -> bool: ...
    def find_element(self, by: basestring=..., value: basestring=None) -> WebElement: ...
    def find_elements(self, by: basestring=..., value: basestring=None) -> List[WebElement]: ...
    def __hash__(self) -> int: ...
