from django.db import models
from common.models import User
from owners_api.models import OwnerProfile
from stylists_api.models import StylistProfile


class JobStylist(models.Model):
    job_id: models.ForeignKey(OwnerProfile, on_delete=models.CASCADE)
    stylist_id: models.ForeignKey(StylistProfile, on_delete=models.CASCADE)

    

