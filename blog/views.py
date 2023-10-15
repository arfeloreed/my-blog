from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


# view routes
# sign up page
def sign_up(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("login"))

    return render(
        request,
        "registration/sign-up.html",
        {
            "form": form,
        },
    )


# logout route
def logout(request):
    auth.logout(request)

    messages.success(request, "Logout Successful")

    return redirect("home")
