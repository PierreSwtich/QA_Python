# EXCEPTIONS

try:
    wait = WebDriverWait(driver, 5)
    wait.untill(ec.visibility_of_element_located((By.Id, 'test')))
    print('iframe found')

except TimeoutException:
    print('There is no iframe')


# This is how we handle error without stopping the whole test when something goes wrong

