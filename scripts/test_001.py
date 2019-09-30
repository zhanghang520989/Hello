import allure

class Test_001():

    @allure.severity('critical')
    @allure.step(title="我是测试001")
    def test_001(self):
        allure.attach("我在测试001里面","描述")
        assert True