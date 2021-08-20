from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.base import TemplateView

from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Book, Proposal

# Create your views here.

class BookListView(ListView):

    model = Book
    paginate_by = 10
    template_name = "library/index.html"


class OwnedBooksListView(LoginRequiredMixin, ListView):

    model = Book
    paginate_by = 10
    template_name = "library/my-books.html"

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(owner=user)


class BookDetailView(DetailView):

    model = Book
    template_name = "library/detail.html"


class BookCreateView(LoginRequiredMixin, CreateView):

    model = Book
    fields = ['title', 'isbn', 'pub_date', 'description', 'number_of_pages',
            'author',  ]
    template_name = "library/add.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    def test_func(self):
        book = self.get_object()
        return book.owner == self.request.user

    model = Book
    fields = ['title', 'isbn', 'pub_date', 'description', 'number_of_pages',
            'author',]
    template_name = "library/update.html"


class ProposalListView(LoginRequiredMixin, TemplateView):

    template_name = "library/proposals.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['proposed_book_list'] = Proposal.objects.filter(proposed_book__owner=user)
        context['requested_book_list'] = Proposal.objects.filter(requested_book__owner=user)
        return context


class ProposalCreateView(LoginRequiredMixin, CreateView):

    model = Proposal
    fields = ['requested_book', 'proposed_book']
    template_name = "library/new-proposal.html"
    success_url = '/proposals/'


class ApproveProposalView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        proposal = Proposal.objects.get(pk=self.kwargs['pk'])
        return proposal.requested_book.owner == self.request.user

    def post(self, request, *args, **kwargs):
        proposal = get_object_or_404(Proposal, pk=self.kwargs['pk'])
        proposal.status = 1
        proposal.requested_book.status = -1
        proposal.proposed_book.status = -1
        proposal.save()
        return redirect(reverse_lazy('proposals'))


class RejectProposalView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        proposal = Proposal.objects.get(pk=self.kwargs['pk'])
        return proposal.requested_book.owner == self.request.user

    def post(self, request, *args, **kwargs):
        proposal = get_object_or_404(Proposal, pk=self.kwargs['pk'])
        proposal.status = -1
        proposal.save()
        return redirect(reverse_lazy('proposals'))
