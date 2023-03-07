from selene import browser, command
from selene import be, have
import os





def test_reg_form(browser_management):
    '''
        Заполнение формы, удаление рекламы
    '''
    browser.open('/')
    browser.element('#firstName').should(be.blank).type('John')
    browser.element('[id="lastName"]').should(be.blank).type('Smith')
    browser.element('[id="userEmail"]').should(be.blank).type('john_smith_980yt304gy@gmail.com')
    browser.element('[for = "gender-radio-1"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('9079079079')
    browser.element('[id="dateOfBirthInput"]').send_keys()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1986"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="5"]').click()
    browser.element('[aria-label="Choose Sunday, June 15th, 1986"]').click()
    browser.driver.execute_script('window.scrollBy(0, 800)')
    browser.element('[id="subjectsInput"]').should(be.blank).type('m')
    browser.element('[tabindex="-1"]').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.getcwd()+'/picture1.jpg')
    browser.element('[id="currentAddress"]').should(be.blank).type('1478 Custer Street')
    browser.element('[id="adplus-anchor"]').execute_script('element.remove()') #Удалить рекламный баннер
    browser.element('[id="state"]').click() #открыть список для выбора штата
    browser.element('[id="react-select-3-option-1"]').click() #выбрать штат
    browser.element('[id="city"]').click()
    browser.element('[id="react-select-4-option-0"]').click()
    browser.element('#submit').perform(command.js.click) #Нажать кнопку Submit
    '''
    Проверка того, что форма заполнена корректно
    '''
    browser.element('//tbody/tr[1]/td[2]').should(have.text('John Smith'))
    browser.element('//tbody/tr[2]/td[2]').should(have.text('john_smith_980yt304gy@gmail.com'))
    browser.element('//tbody/tr[3]/td[2]').should(have.text('Male'))
    browser.element('//tbody/tr[4]/td[2]').should(have.text('9079079079'))
    browser.element('//tbody/tr[5]/td[2]').should(have.text('15 June,1986'))
    browser.element('//tbody/tr[6]/td[2]').should(have.text('Maths'))
    browser.element('//tbody/tr[7]/td[2]').should(have.text('Sports, Reading'))
    browser.element('//tbody/tr[8]/td[2]').should(have.text('picture1.jpg'))
    browser.element('//tbody/tr[9]/td[2]').should(have.text('1478 Custer Street'))
    browser.element('//tbody/tr[10]/td[2]').should(have.text('Uttar Pradesh Agra'))
    browser.element('[id="closeLargeModal"]').perform(command.js.click)  # Нажать кнопку Close





