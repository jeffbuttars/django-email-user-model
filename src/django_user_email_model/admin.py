class SignUpAdmin(admin.ModelAdmin):
    pass

admin.site.register(SignUp, SignUpAdmin)

# We need to override the base User creation and change forms
# because they are hard coded to use the User model, we just
# need to make them use our EmailUserModel model

# Override the forms:
class EmailUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class EmailUserChangeForm(UserChangeForm):
    """Docstring for EmailUserChangeForm """
    class Meta:
        model = get_user_model()


# Add the forms to our Admin class
class EmailUserAdmin(UserAdmin):

    form = EmailUserChangeForm
    add_form = EmailUserCreationForm

admin.site.register(EmailUserModel, EmailUserAdmin)
