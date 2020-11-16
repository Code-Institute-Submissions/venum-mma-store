from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages

from profiles.models import UserProfile
from reviews.forms import ReviewForm
from products.models import Product
from reviews.models import UserReview

# Create your views here.


def reviews(request):
    """
    Render Reviews Page.
    """
    product = Product.objects.all()
    reviews = UserReview.objects.all()
    review_form = ReviewForm()

    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        if request.user == user.user:
            context = {
                'user': user,
                'product': product,
                'reviews': reviews,
                'review_form': review_form,
            }
            return render(request, 'reviews/reviews.html', context)

    else:
        context = {
            'review_page': 'active',
            'product': product,
            'reviews': reviews,
        }
    return render(request, 'review/review.html', context)


def add_review(request):
    """
    Authenticated user may add a review.
    """
    user_profile = UserProfile.objects.get(user=request.user)

    if request.user.is_authenticated:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                if len(request.POST["review_content"]) <= 0 or len(
                        request.POST["product"]) <= 0:
                    messages.error(
                        request, "Please fill the review form!")
                    return redirect(reverse("reviews"))
                add_review = review_form.save(commit=False)
                add_review.user_profile = user_profile
                review_form.save()
                messages.success(request, 'Thank you for adding a review.')
                return redirect(reverse("reviews"))
            else:
                messages.error(
                    request, 'Oops, something went wrong. Try again later.')

    template = 'reviews/reviews.html'
    context = {
        'review_form': review_form,
    }

    return render(request, template, context)


def edit_review(request, review_id):
    """
    Authenticated users may edit reviews they added previously.
    Superusers may edit any review.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    review = get_object_or_404(UserReview, id=review_id)
    review_form = ReviewForm(instance=review)

    if request.user == user_profile.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                if len(request.POST["product" or "review_content"]) <= 0:
                    messages.error(
                        request, "You have not completed the review form. \
                                            Please add content and try again.")
                    return redirect(reverse("reviews"))
                else:
                    review = review_form.save(commit=False)
                    user_profile = user_profile
                    review_form.save()
                    messages.success(request, 'Thank you for updating your review.')
                    return redirect(reverse("reviews"))
        else:
            review_form = ReviewForm(instance=review)

    template = 'reviews/edit_review.html'
    context = {
        'review_form': review_form,
        'user_profile': user_profile,
        'review': review,
    }

    return render(request, template, context)


def delete_review(request, review_id):
    """
    Authenticated users may delete reviews they added previously.
    Superusers may delete any review.
    """
    review = get_object_or_404(UserReview, id=review_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.user.is_authenticated:
        if request.user == user_profile.user:
            review.delete()
            messages.success(request, 'Thank you for deleting your review.')
            return redirect(reverse("reviews"))

        elif request.user.is_superuser:
            review.delete()
            messages.success(request, 'Review was deleted.')
            return redirect(reverse("reviews"))

        else:
            messages.error(request, 'Oops, you are not authorized to delete this reviews.')
            return redirect(reverse("reviews"))

    else:
        messages.error(request, 'You must be signed in.')
        return redirect(reverse("reviews"))

    template = 'reviews/reviews.html'
    context = {
        'review': review,
        'user_profile': user_profile,
    }

    return render(request, template, context)
