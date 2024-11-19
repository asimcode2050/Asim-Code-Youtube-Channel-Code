class CookieJar:
    def __init__(self):
        self.cookies = []

    def add_cookie(self, cookie_type):
        self.cookies.append(cookie_type)

    def count_cookies(self):
        return len(self.cookies)

    def eat_cookie(self):
        if self.cookies:
            return self.cookies.pop()
        else:
            return "No cookies left to eat!"


my_jar = CookieJar()
my_jar.add_cookie("chocolate chip")
my_jar.add_cookie("oatmeal raisin")
my_jar.add_cookie("peanut butter")
print(f"Cookies in the jar: {my_jar.count_cookies()}")  # Outputs: 3
cookie_eaten = my_jar.eat_cookie()
print(f"Eating a {cookie_eaten} cookie!")
print(f"Cookies left in the jar: {my_jar.count_cookies()}")  # Outputs: 2
