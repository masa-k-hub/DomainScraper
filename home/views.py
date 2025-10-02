from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PageForm
from .forms import Page
from datetime import datetime
from zoneinfo import ZoneInfo


class IndexView(View):
    def get(self, request):
        datetime_now = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        return render(request, "home/index.html", {"datetime_now": datetime_now})
    
class PageCreateView(View):
    def get(self, request):
        form = PageForm()
        return render(request, "home/page_form.html", {"form": form})
    
    def post(self, request):
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("diary:index")
        return render(request, "home/page_form.html", {"form": form})
    
class PageListView(View):
    def get(self, request):
        page_list = Page.objects.order_by("page_date")
        return render(request, "home/page_list.html", {"page_list": page_list})
    
class PageDetailView(View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "home/page_detail.html", {"page": page})
    
class TestView(View):
    def get(self, request):
        return render(request, "home/test.html")
        


index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
test_view = TestView.as_view()