from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Donation, Institution
from django.db.models import Sum, Count

# Create your views here.

class LandingPage(View):
    def get(self, request):
        num_bags = Donation.objects.all().aggregate(Sum("quantity"))
        num_institutions = Donation.objects.all().annotate(num_institutions=Count('categories'))
        institutions = Institution.objects.all()
        pagination = Paginator(institutions, 5)
        page = request.GET.get('page')

        try:
            page_num = Paginator.page(page)
        except PageNotAnInteger:
            page_num = Paginator.page(1)
        except EmptyPage:
            page_num = Paginator.page(Paginator.num_pages)

        return render(request, 'charity/LandingPage.html',{
                "quantity": num_bags["quantity__sum"],
                "num_institutions": len(num_institutions),
                "institutions": institutions,
                })

class AddDonationView(View):
    def get(self, request):
        return render(request, 'charity/AddDonation.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'charity/Login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'charity/Register.html')