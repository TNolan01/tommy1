from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


# Updates the total of the lineitem for item update/create situation
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()
    
    
# Updates the total of the lineitem on the deletion of a lineitem
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    instance.order.update_total()
    