from selene import browser, command
from selene import be, have
import os
import time




def test_reg_form(browser_management):
    browser.open('/')
    browser.element('#firstName').should(be.blank).type('John')
    browser.element('[id="lastName"]').should(be.blank).type('Smith')
    browser.element('[id="userEmail"]').should(be.blank).type('john_smith_980yt304gy@gmail.com')
    browser.element('[for = "gender-radio-1"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('9079079079')
    #time.sleep(3)
    browser.element('[id="dateOfBirthInput"]').send_keys()
    browser.element('[class="react-datepicker__year-select"]').click()
    #time.sleep(3)
    browser.element('[value="1986"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="5"]').click()
    browser.element('[aria-label="Choose Sunday, June 15th, 1986"]').click()
    #time.sleep(3)
    browser.driver.execute_script('window.scrollBy(0, 800)')
    browser.element('[id="subjectsInput"]').should(be.blank).type('m')
    #time.sleep(3)
    browser.element('[tabindex="-1"]').click()
    #time.sleep(3)

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.getcwd()+'/picture1.jpg')
    #time.sleep(3)
    browser.element('[id="currentAddress"]').should(be.blank).type('1478 Custer Street')
    time.sleep(5)
    browser.element('[id="adplus-anchor"]').execute_script('element.remove()') #Удаляет рекламный баннер
    time.sleep(5)
    browser.element('[id="state"]').click() #открыть список для выбора штата
    browser.element('[id="react-select-3-option-1"]').click() #выбрать штат
    browser.element('[id="city"]').click()
    browser.element('[id="react-select-4-option-0"]').click()
    time.sleep(3)

    #Проверка того, что форма заполнена корректно
    browser.element('#firstName').should(have.text('John'))
    browser.element('[id="lastName"]').hould(have.text('Smith'))


