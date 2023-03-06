from selene import browser
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
    time.sleep(3)
    browser.element('[id="dateOfBirthInput"]').send_keys()
    browser.element('[class="react-datepicker__year-select"]').click()
    time.sleep(3)
    browser.element('[value="1986"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="5"]').click()
    browser.element('[aria-label="Choose Sunday, June 15th, 1986"]').click()
    time.sleep(3)
    browser.driver.execute_script('window.scrollBy(0, 500)')
    browser.element('[id="subjectsInput"]').should(be.blank).type('m')
    #time.sleep(3)
    browser.element('[tabindex="-1"]').click()
    time.sleep(3)

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    time.sleep(3)
    #picture_way = os.getcwd()+'/picture1.jpg'
    #return picture_way
    browser.element('[id="uploadPicture"]').double_click()
    browser.element('[id="uploadPicture"]').send_keys(os.getcwd()+'/picture1.jpg')
    time.sleep(3)
    browser.element('[id="currentAddress"]').should(be.blank).type('1478 Custer Street')
    time.sleep(10)

#<textarea placeholder="Current Address" rows="5" cols="20" id="currentAddress"
# class="form-control"></textarea>

#"C:\Users\klima\PycharmProjects\qa_guru_python_4_5\tests\IMG_20230224_164633_1.jpg"



#<div class="subjects-auto-complete__control css-yk16xz-control"><div
#class="subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3"><div
#class="subjects-auto-complete__placeholder css-1wa3eu0-placeholder"></div><div class="css-1g6gooi"><div
#class="subjects-auto-complete__input" style="display: inline-block;"><input autocapitalize="none" autocomplete="off" autocorrect="off"
#id="subjectsInput" spellcheck="false" tabindex="0" type="text" aria-autocomplete="list" value=""
#style="box-sizing: content-box; width: 2px; background: 0px center; border: 0px; font-size: inherit; opacity: 1; outline: 0px; padding: 0px; color: inherit;"><div style="position: absolute; top: 0px; left: 0px; visibility: hidden; height: 0px; overflow: scroll; white-space: pre; font-size: 16px; font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Arial, &quot;Noto Sans&quot;, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;, &quot;Noto Color Emoji&quot;; font-weight: 400; font-style: normal; letter-spacing: normal; text-transform: none;"></div></div></div></div><div class="subjects-auto-complete__indicators css-1wy0on6"><span
#class="subjects-auto-complete__indicator-separator css-1okebmr-indicatorSeparator"></span></div></div>

#<div class="subjects-auto-complete__option subjects-auto-complete__option--is-focused css-1n7v3ny-option"
#id="react-select-2-option-0" tabindex="-1">Maths</div>

# browser.driver.execute_script('window.scrollBy(0, 500)')
