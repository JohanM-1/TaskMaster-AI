from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.db.models import QuerySet
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView

from real_time_django.users.models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self) -> str:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user.get_absolute_url()

    def get_object(self, queryset: QuerySet | None = None) -> User:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self) -> str:
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})


user_redirect_view = UserRedirectView.as_view()


@require_http_methods(["POST"])
def newsletter_signup(request):
    email = request.POST.get("email")
    if email:
        try:
            # Enviar correo de confirmación
            subject = "Welcome to Our Newsletter!"
            message = """Thank you for subscribing to our newsletter!
            
We're excited to keep you updated with our latest news and updates.

Best regards,
The Team"""

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            messages.success(
                request, "Thank you for subscribing! Please check your email."
            )
        except Exception as e:
            messages.error(
                request,
                "There was an error sending the confirmation email. Please try again later.",
            )
    else:
        messages.error(request, "Please provide a valid email address.")

    return redirect("home")


@login_required
def custom_password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update the session to prevent logging out
            update_session_auth_hash(request, user)
            messages.success(request, _("Your password was successfully changed!"))
            # Log out the user
            logout(request)
            return redirect("account_login")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "account/password_change.html", {"form": form})
