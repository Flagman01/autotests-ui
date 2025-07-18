from playwright.sync_api import sync_playwright, expect


def test_successful_registration():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_registration_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_registration_input.fill('user.name@gmail.com')

        username_registration_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_registration_input.fill('username')

        password_registration_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_registration_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state.json')

        title_page_dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
        expect(title_page_dashboard).to_be_visible()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')