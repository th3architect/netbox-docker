from django.contrib.contenttypes.models import ContentType
from extras.models import CF_TYPE_TEXT, CustomField

from dcim.models import Device
from dcim.models import DeviceType

device      = ContentType.objects.get_for_model(Device)
device_type = ContentType.objects.get_for_model(DeviceType)

nine_urn, created = CustomField.objects.get_or_create(
    type=CF_TYPE_TEXT,
    name='nine_urn',
    description='Nine URN'
)

nine_urn.obj_type.add(device)
nine_urn.obj_type.add(device_type)
