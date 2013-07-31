# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from usermanager.models import User
from django.core.urlresolvers import reverse

class ListUserView(ListView):
	model = User
	template_name = 'user_list.html'

class CreateUserView(CreateView):

	model = User
	template_name = 'create_user.html'

	def get_success_url(self):
		return reverse('user-list')

class UpdateUserView(UpdateView):

	model = User
	template_name = 'edit_user.html'

	def get_success_url(self):
		return reverse('user-list')

class DeleteUserView(DeleteView):

	model = User
	template_name = 'delete_user.html'

	def get_success_url(self):
		return reverse('user-list')