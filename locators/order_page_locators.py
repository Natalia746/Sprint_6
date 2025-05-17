from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_HEADER = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_FOOTER = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "img[alt='Scooter']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "img[alt='Yandex']")
    ELEMENT = (By.XPATH,"//*[@class='Home_SubHeader__zwi_E'and contains (text(),'Вопросы о важном')]")

class OrderPageLocators:
    # Поля ввода
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[contains(@class, 'select-search__input') and @placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Выпадающие списки
    METRO_STATION = (By.XPATH, "//li[@data-value='3']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_OPTION = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child(2)")
    COLOR_CHECKBOX_BLACK = (By.ID, "black")
    COLOR_CHECKBOX_GREY = (By.ID, "grey")
    RENTAL_OPTION_BOTTOM = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child(6)")

    # Кнопки
    NEXT_BUTTON = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Order_Content')]//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons__1xGrp')]//button[text()='Да']")

    # Модальные окна
    MODAL_WINDOW = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    SUCCESS_TITLE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    CALENDAR = (By.CLASS_NAME, "react-datepicker")

