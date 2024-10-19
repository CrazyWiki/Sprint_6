from selenium.webdriver.common.by import By


class HomePageLocators:
    #third part
    hp_capture_text_element = [By.CLASS_NAME, 'Home_SubHeader__zwi_E']
    #fourth part
    hp_questions_text_element = [By.CLASS_NAME, 'Home_SubHeader__zwi_E']
    hp_question_test=[By.XPATH, ".//div[@id='accordion__heading-0']/parent::div"]
    hp_order_button_locator=[By.XPATH,".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]
    hp_questions = {
        1: [By.XPATH, ".//div[@id='accordion__heading-0']/parent::div"],
        2: [By.XPATH, ".//div[@id='accordion__heading-1']/parent::div"],
        3: [By.XPATH, ".//div[@id='accordion__heading-2']/parent::div"],
        4: [By.XPATH, ".//div[@id='accordion__heading-3']/parent::div"],
        5: [By.XPATH, ".//div[@id='accordion__heading-4']/parent::div"],
        6: [By.XPATH, ".//div[@id='accordion__heading-5']/parent::div"],
        7: [By.XPATH, ".//div[@id='accordion__heading-6']/parent::div"],
        8: [By.XPATH, ".//div[@id='accordion__heading-7']/parent::div"],
    }
    hp_answers = {
        1: [By.ID, 'accordion__panel-0'],
        2: [By.ID, 'accordion__panel-1'],
        3: [By.ID, 'accordion__panel-2'],
        4: [By.ID, 'accordion__panel-3'],
        5: [By.ID, 'accordion__panel-4'],
        6: [By.ID, 'accordion__panel-5'],
        7: [By.ID, 'accordion__panel-6'],
        8: [By.ID, 'accordion__panel-7'],
    }
