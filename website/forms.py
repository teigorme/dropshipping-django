from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                "placeholder": "Seu Nome Completo",
            }
        ),
    )
 
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                "placeholder": "seu.email@gmail.com",
            }
        ),
    )
    
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                "placeholder": "••••••••",
            }
        ),
    )
    confirm_password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                "placeholder": "••••••••",
            }
        ),
    )


class LoginForm(forms.Form):

    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                "placeholder": "seu.email@gmail.com",
            }
        ),
    )

    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                "placeholder": "••••••••",
            }
        ),
    )
