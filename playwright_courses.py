from playwright.sync_api import sync_playwright, expect

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

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    title_page_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_page_courses).to_be_visible()
    expect(title_page_courses).to_have_text('Courses')

    icon_courses_list = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_courses_list).to_be_visible()

    title_courses_list_empty = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(title_courses_list_empty).to_be_visible()
    expect(title_courses_list_empty).to_have_text('There is no results')

    description_courses_list_empty = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(description_courses_list_empty).to_be_visible()
    expect(description_courses_list_empty).to_have_text('Results from the load test pipeline will be displayed here')
