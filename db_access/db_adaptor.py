from signup.models import User, Referral

class DBAdapter:
    DATABASE='default'

    def __init__(self):
        pass

    def get_user(self, email, phone_number):
        try:
            return User.objects.using(self.DATABASE).filter(email=email, phone=phone_number).get()
        except Exception as e:
            return None

    def create_user(self, name, email, phone_number, location, description, type):
        try:
            return User.objects.using(self.DATABASE).create(email=email, phone=phone_number, name=name,
                                                            location=location, description=description, user_type=type)
        except Exception as e:
            return None

    def get_referral_by_id(self, ref_id):
        try:
            return Referral.objects.using(self.DATABASE).filter(referral_id=ref_id).get()
        except Exception as e:
            return None

    def update_referral(self, ref_id, status):
        try:
            Referral.objects.using(self.DATABASE).filter(referral_id=ref_id).update(status=status)
        except Exception as e:
            pass

    def create_referral(self, user, ref_id):
        try:
            Referral.objects.using(self.DATABASE).create(user=user, referral_id=ref_id)
        except Exception as e:
            pass