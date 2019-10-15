from django import forms
from django_summernote.widgets import SummernoteWidget


class CreateForm(forms.Form):
    author = forms.CharField(
        error_messages={
            'required': '글쓴이 정보가 필요합니다.'
        },
        widget=forms.HiddenInput,
        label='글쓴이',
        required=True,
    )
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=255,
        label='제목',
        required=True,
    )
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요',
        },
        widget=SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
        label='내용',
    )

    def clean(self):
        cleand_data = super().clean()
        author = cleand_data.get('author')
        title = cleand_data.get('title')

        if not (author and title):
            self.add_error('author', '글쓴이가 없습니다.')
            self.add_error('title', '제목이 없습니다.')
