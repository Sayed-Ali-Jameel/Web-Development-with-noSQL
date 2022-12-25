from django.contrib.auth.models import User

admin=User.objects.create_user('admin', password='admin', email='admin@admin.com')
admin.is_superuser = True
admin.is_staff = True
admin.save()

User.objects.create_user('Ali', password='123', email='ali@ali.com').save()

User.objects.create_user('Hassan', password='abc', email='hassan@hassan.com').save()

User.objects.create_user('Mohammed', password='Mohammed', email='mohammed@mohammed.com').save()

User.objects.create_user('Nasser', password='asdASD123', email='nasser@nasser.com').save()

User.objects.create_user('Restaurant', password='123', email='Restaurant@Restaurant.com').save()

User.objects.create_user('DesignCo', password='asdASD123', email='DesignCo@DesignCo.com').save()

User.objects.create_user('aCompany', password='321', email='aCompany@aCompany.com').save()