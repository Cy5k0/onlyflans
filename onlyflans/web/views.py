from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Flan
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required


def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {"flans": flanes_publicos})


def detalle_flan(request, flan_uuid):
    flan = get_object_or_404(Flan, flan_uuid=flan_uuid)
    return render(request, "detalle_flan.html", {"flan": flan})


def acerca(request):
    return render(request, "about.html")


@login_required
def bienvenida(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, "welcome.html", {"flans": flanes_privados})


def formulario_contacto(request):
    if request.method == "POST":
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()  # Esta es la ventaja del ModelForm - guarda directamente
            return HttpResponseRedirect("/exito")
    else:
        form = ContactFormModelForm()

    return render(request, "contactForm.html", {"form": form})


def success(request):
    return render(request, "exito.html", {})


@login_required
def gestionar_cuenta(request):
    if request.method == "POST":
        if "change_password" in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(
                    request, "Tu contraseña ha sido actualizada exitosamente!"
                )
                return redirect("gestionar_cuenta")
            else:
                messages.error(request, "Por favor corrige los errores abajo.")

        elif "delete_account" in request.POST:
            request.user.delete()
            logout(request)
            messages.success(request, "Tu cuenta ha sido eliminada exitosamente.")
            return redirect("/")

    else:
        password_form = PasswordChangeForm(request.user)

        # Configura los widgets del formulario
        for field_name, field in password_form.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "autocomplete": "new-password"}
            )

    return render(
        request,
        "account/gestionar_cuenta.html",
        {
            "password_form": password_form,
        },
    )
