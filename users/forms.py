from django import forms


class WithdrawalForm(forms.Form):
    password = forms.CharField(
        error_messages={
            'required': '비밀번호가 입력되지 않았습니다.'
        },
        widget=forms.PasswordInput,
        label='비밀번호 확인',
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일이 입력되지 않았습니다.'
        },
        label='이메일',
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호가 입력되지 않았습니다.'
        },
        widget=forms.PasswordInput,
        label='비밀번호',
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not (email and password):
            self.add_error('email', '이메일 값이 없습니다.')
            self.add_error('password', '비밀번호 값이 없습니다.')


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일이 입력되지 않았습니다.'
        },
        label='이메일',
    )
    username = forms.CharField(
        error_messages={
            'required': '유저이름이 입력되지 않았습니다.'
        },
        label='유저이름',
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호가 입력되지 않았습니다.'
        },
        widget=forms.PasswordInput,
        label='비밀번호',
    )
    confirm_password = forms.CharField(
        error_messages={
            'required': '비밀번호 확인이 입력되지 않았습니다.'
        },
        widget=forms.PasswordInput,
        label='비밀번호 확인',
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if not (email and username and password and confirm_password):
            if type(username) is not str and username:
                self.add_error('username', '유저이름 값이 없습니다.')
            if type(username) is not str and username:
                self.add_error('email', '이메일 값이 없습니다.')
            if type(username) is not str and username:
                self.add_error('password', '비밀번호 값이 없습니다.')
            if type(username) is not str and username:
                self.add_error('confirm_password', '비밀번호 확인 값이 없습니다.')

        if password != confirm_password:
            self.add_error('confirm_password', '비밀번호와 값이 일치하지 않습니다.')
