from django.contrib import messages
from django.views.generic.edit import FormView

from blog.models import Post
from users.models import User
from . import forms


class CreateForm(FormView):
    template_name = 'blog/create.html'
    form_class = forms.CreateForm
    success_url = '/'

    def form_valid(self, form):
        author = form.cleaned_data.get('author')
        title = form.cleaned_data.get('title')
        contents = form.cleaned_data.get('contents')

        user = User.objects.filter(pk=author)

        # 존재하지 않는 유저.
        if not user.exists():
            messages.error(self.request, '글쓰기에 실패하였습니다 탈퇴한 회원인지 확인해주세요.', extra_tags='danger')
            return super().form_invalid(form)

        post = Post(
            author=user[0],
            title=title,
            contents=contents,
        )
        post.save()

        return super().form_valid(form)
