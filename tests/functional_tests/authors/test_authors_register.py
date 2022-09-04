from time import sleep
from unittest import skip
from .base import AuthorsBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AuthorsRegisterTest(AuthorsBaseTest):
    def get_by_placeholder(self, web_element, placeholder):
        # Selecionando por full xpath
        return web_element.find_element(
            By.XPATH, f'//input[@placeholder="{placeholder}"]'
        )

    def fill_form_dummy_data(self, form):
        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' ' * 20)

    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form'
        )

    def form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.fill_form_dummy_data(form)
        form.find_element(By.NAME, 'email').send_keys('dummy@email.com')

        callback(form)
        return form 

    @skip('ajustar github actions')
    def test_empty_username_name_error_message(self):
        def callback(form):
            first_name_field = self.get_by_placeholder(form, 'Ex.: John')
            first_name_field.send_keys(' ')
            first_name_field.send_keys(Keys.ENTER)
            form = self.get_form()           
            self.sleep(5)
            self.assertIn('Este campo não pode ser vazio.', form.text)
        self.form_field_test_with_callback(callback)

    @skip('ajustar github actions')
    def test_empty_first_name_error_message(self):
        def callback(form):
            first_name_field = self.get_by_placeholder(form, 'Ex.: John')
            first_name_field.send_keys(' ')
            first_name_field.send_keys(Keys.ENTER)
            form = self.get_form()           
            self.sleep(5)
            self.assertIn('Este campo não pode ser vazio.', form.text)
        self.form_field_test_with_callback(callback)

    @skip('ajustar github actions')
    def test_invalid_email_erro_message(self):
        def callback(form):
            email_field = self.get_by_placeholder(form, 'Seu email')
            email_field.send_keys('email@inválido ')
            email_field.send_keys(Keys.ENTER)
            form = self.get_form()           
            self.sleep(5)
            self.assertIn('O email deve ser válido', form.text)
        self.form_field_test_with_callback(callback)

    @skip('ajustar github actions')
    def test_passwords_do_not_match(self):
        def callback(form):
            password1 = self.get_by_placeholder(form, 'Digite sua senha')
            password2 = self.get_by_placeholder(form, 'Repita sua senha')
            password1.send_keys('P@ssw0rd')
            password2.send_keys('P@ssw0rd_Diferente')
            password2.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Password and password2 devem ser iguais', form.text)
        self.form_field_test_with_callback(callback)

    @skip('ajustar github actions')
    def test_user_valid_data_register_successfully(self):
        """Verifica se o usário foi criado"""
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()
        self.get_by_placeholder(form, 'Ex.: John').send_keys('First Name')
        self.get_by_placeholder(form, 'Ex.: Doe').send_keys('Last Name')
        self.get_by_placeholder(form, 'Seu nome de usuário').send_keys('my_username')
        self.get_by_placeholder(
            form, 'Seu email').send_keys('email@valid.com')
        self.get_by_placeholder(
            form, 'Digite sua senha').send_keys('P@ssw0rd1')
        self.get_by_placeholder(
            form, 'Repita sua senha').send_keys('P@ssw0rd1')
        sleep(5)
        form.submit()

        self.assertIn(
            'Seu usuário foi criado, por favor realize o login.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
