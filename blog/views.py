from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, UpdateView

from blog.models import Post
from users.models import User
from . import forms


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'contents']
    template_name = 'blog/update.html'
    success_url = '/'

    def form_valid(self, form):
        post = Post.objects.filter(pk=self.kwargs['pk'], author=self.request.user)
        if not post.exists():  # 유효성 조건 통과
            form.add_erros('title', '수정에 실패하였습니다.')
            return super().form_invalid(form)
        return super().form_valid(form)


class PostDetailView(DetailView):
    template_name = 'blog/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class PostListView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    model = Post
    paginate_by = 7

    def get_queryset(self):
        return Post.objects.all().order_by('-create_at')


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
