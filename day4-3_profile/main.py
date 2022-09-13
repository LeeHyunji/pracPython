# - 사용자들의 프로필을 관리할 수 있는 클래스를 선언해주세요
# - 메소드를 호출해서 사용자의 프로필을 설정할 수 있도록 해주세요
# - 사용자의 정보를 각각 출력할 수 있는 메소드를 만들어주세요

class Profile():
    def __init__(self):
        self.profile = {
            "name": "",
            "gender": "",
            "birthday": "",
            "age": "",
            "phone": "",
            "email": "",
        }

    def set_profile(self, profile):
        self.profile = profile

    def get_profile(self, field="all"):
        if field == "all":
            return self.profile
        else:
            return self.profile[field]

    def modify(self, field, value):
        print(f'{field}의 정보가 {self.profile[field]} -> {value}로 변경되었습니다.')
        self.profile[field] = value

    def delete(self, field):
        print(f'{field}의 정보가 삭제 되었습니다.')
        del self.profile[field]


my_profile = Profile()
my_profile.set_profile({
    "name": "LeeHyunji",
    "gender": "female",
    "birthday": "96/01/13",
    "age": "27",
    "phone": "010-1234-5678",
    "email": "hyunji015@gmail.com",
    "address": "서울특별시 강북구 도봉로 61길 22-5",
})
print(f'이름 : {my_profile.get_profile("name")}')
print(f'성별 : {my_profile.get_profile("gender")}')
print(f'생일 : {my_profile.get_profile("birthday")}')
print(f'나이 : {my_profile.get_profile("age")}')
print(f'핸드폰 : {my_profile.get_profile("phone")}')
print(f'이메일 : {my_profile.get_profile("email")}')

my_profile.modify("phone", "010-3025-9337")
print(f'내프로필 : \n{my_profile.get_profile()}')

my_profile.delete("address")
print(f'내프로필 : \n{my_profile.get_profile()}')
