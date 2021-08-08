from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView,DetailView,TemplateView,UpdateView
from django.contrib.auth.forms import UserChangeForm
from .models import post
from .models import comment
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import edit_profile_form
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import feed
from .models import social_media_account
from .models import profile_picture
from .forms import social_form
from  adminpanel.views import feedback_form




class profile(ListView):
    template_name="profile.html"
    model=post
    ordering=['-id']

    def get_queryset(self):
        query_set=super().get_queryset()
        return query_set.select_related

    def get_context_data(self, *args, **kwargs):
        context = super(profile, self).get_context_data(*args, **kwargs)
        context['social_media_account_list'] = social_media_account.objects.all()
        context['profile_picture_list'] = profile_picture.objects.all()
        return context

def status_form(request):
        if request.method=="POST":
                username=request.POST['username']
                statuss=request.POST['status_name']
                name=request.POST['name']
                email=request.POST['email']
                if statuss=='':
                        return HttpResponse('404 not found.You must be write something!')
                else:
                        status_database=post(post_author=username,status=statuss,author_name=name,author_email=email)
                        status_database.save()
                        return redirect('profile')
               

def comment_form(request):
    if request.method=="POST":
        commentss=request.POST['comment_name']
        commenter=request.POST['commenter_name']
        commenter_username=request.POST['commenter_username']
        comment_id=request.POST['id']
        post_author_name=request.POST['post_author_name']
        comment_database=comment(comment=commentss,commenter_name=commenter,comment_id=comment_id,post_author_name=post_author_name,commenter_username=commenter_username)
        comment_database.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def profile_pic(request):
        return render (request,"profile_pic.html")



class edit_profile (generic.UpdateView):
        form_class=edit_profile_form
        template_name='edit_profile.html'
        success_url=reverse_lazy('edit_profile')


        def get_object(self):
                return self.request.user
        

class edit_social_media (UpdateView):
        form_class=social_form
        template_name='update_account_info.html'
        success_url=reverse_lazy('edit_social_media')


        def get_object(self):
                return self.request.user

      

def profile_pic_change(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        profile_picture_user=request.POST['user']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        profile_pic=profile_picture(profile_picture_user=profile_picture_user,user_profile_picture=myfile)
        if profile_picture.objects.filter(profile_picture_user=profile_picture_user).exists():
            return HttpResponse ("You have already upload your profile picture.")
        else:
            profile_pic.save()
            return render(request, 'profile_pic.html', {
                'uploaded_file_url': uploaded_file_url
            })









        



       




        


    

