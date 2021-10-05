import requests
from student import Student

api_url = "https://ske19-api.herokuapp.com/"


class SKE19:
    """A client to access SKE19 API, must be initialized with a secret key.
    """
    def __init__(self, secret, duration=3600):
        """Create instance to access SKE19 API, must have secret key provided.

        :param secret: Secret key for generating auth token.
        :type secret: str
        :raises: ValueError: Secret key is incorrect.
        """
        res = requests.post(f"{api_url}auth", headers={"secret": secret,
                            "duration": duration})
        if res.status_code == 403:
            raise ValueError('Cannot authorize the SKE19 client.',
                             f"Secret: {secret}")
        self.__token = res.json()["token"]

    def get_student(self, id):
        """Get student information from student ID.

        :param id: Student ID
        :type id: str
        :return: Student object associated with the ID.
        :rtype: Student
        """
        body = {
            "id": id
        }
        headers = {
            "Authorization": f"Bearer {self.__token}",
            "Content-type": "application/json"
        }
        _res = requests.get(f"{api_url}student", json=body, headers=headers)
        res = _res.json()
        if _res.status_code == 404:
            return res["message"]
        print(res)
        return Student(id,
                       res["firstNameEN"], res["lastNameEN"], res["nickEN"],
                       res["firstNameTH"], res["lastNameTH"], res["nickTH"],
                       res["email"],
                       res["instagram"])

    def get_all_students(self):

        headers = {
            "Authorization": f"Bearer {self.__token}",
            "Content-type": "application/json"
        }
        _res = requests.get(f"{api_url}students", headers=headers)
        res = _res.json()["students"]
        students = []
        for std in res:
            students.append(
                Student(std,
                        res[std]["firstNameEN"],
                        res[std]["lastNameEN"],
                        res[std]["nickEN"],
                        res[std]["firstNameTH"],
                        res[std]["lastNameTH"],
                        res[std]["nickTH"],
                        res[std]["email"],
                        res[std]["instagram"],)
            )
        return students
