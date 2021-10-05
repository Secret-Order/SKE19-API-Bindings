class Student:
    """A class for storing information of a student.
    """
    def __init__(self, id, first_en, last_en, nick_en,
                 first_th, last_th, nick_th, email, ig):
        self._id = id
        self._first_en = first_en
        self._last_en = last_en
        self._nick_en = nick_en
        self._first_th = first_th
        self._last_th = last_th
        self._nick_th = nick_th
        self._email = email
        self._ig = ig

    def get_id(self):
        """Gets an ID of the student.

        :return: ID of student
        :rtype: str
        """
        return self._id

    def get_name_english(self):
        """Gets the first, last and nick name in English of the student.

        :return: Dictionary of first, last and nick name.
        :rtype: dict
        """
        return {
            "first_name": self._first_en,
            "last_name": self._last_en,
            "nick_name": self._nick_en
        }

    def get_name_thai(self):
        """Gets the first, last and nick name in Thai of the student.

        :return: Dictionary of first, last and nick name.
        :rtype: dict
        """
        return {
            "first_name": self._first_th,
            "last_name": self._last_th,
            "nick_name": self._nick_th
        }

    def get_email(self):
        """Gets the email of the student.

        :return: Email string
        :rtype: str
        """
        return self._email

    def get_instagram(self):
        """Gets the instagram ID of the student.

        :return: Instagram ID string
        :rtype: str
        """
        return self._ig

    def __repr__(self):
        return f"Student {self._id}"
