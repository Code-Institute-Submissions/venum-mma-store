from django.db import models
from profiles.models import UserProfile
from products.models import Product


class UserReview(models.Model):
    """
    Write reviews for products.
    """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_profile",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_product",
    )
    review_title = models.CharField(max_length=500)
    review_content = models.TextField(blank=True,
                                      null=True, default="")

    class Meta:
        ordering = ['product']

    def __str__(self):
        return self.review_title
