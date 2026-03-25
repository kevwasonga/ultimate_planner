from django.utils import timezone

class TimeStampedMixin:
    def get_time_diff(self):
        return timezone.now() - self.created_at
