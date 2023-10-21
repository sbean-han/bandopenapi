class Profile:
    def __init__(self, name, profile_image_url, user_key,
                 message_allowed, is_app_member):
        self.name = name
        self.profile_image_url = profile_image_url
        self.user_key = user_key
        self.message_allowed = message_allowed
        self.is_app_member = is_app_member

    def __str__(self):
        return str(self.__dict__)