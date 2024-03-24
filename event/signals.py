# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import EventApply
# from django.conf import settings
# from django.core.mail import send_mail

# @receiver(post_save, sender=EventApply)
# def send_mail_to_applied_user(sender, instance, created, **kwargs):
#     if created:
#         event_apply = instance
#         event = event_apply.event
#         name = event_apply.name
#         title = event.title
#         subtitle = event.subtitle or ''
#         date = event.date.strftime('%Y.%m.%d')
#         time = event.date.strftime('%H:%M')
#         location = event.location_name
#         phone = event.phone
#         message = event.email_template.format(
#             title=title, subtitle=subtitle, name=name, date=date, 
#             time=time, location=location, phone=phone, event_url=event.get_absolute_url()
#         )
#         send_mail(
#             subject=f'{title} Seminarı',
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[event_apply.email]
#         )