# from peewee import Model, BigIntegerField, TextField, BooleanField, IntegerField, PostgresqlDatabase
#
# datab = PostgresqlDatabase('infinityuc_bot', user='postgres', password='2001', host='localhost')
#
#
# class Users(Model):
#     chat_id = BigIntegerField(primary_key=True)
#     username = TextField(null=True)
#     active = BooleanField(default=1)
#     referral = IntegerField(null=True)
#     count_referrals = IntegerField(default=0)
#
#     class Meta:
#         database = datab
#
#
# datab.connect()
# datab.create_tables([Users])
